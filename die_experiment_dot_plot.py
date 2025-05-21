import streamlit as st
import matplotlib.pyplot as plt
import random
from collections import Counter

def dot_plot(data, title="Dot Plot", xlabel="Values", ylabel="Frequency"):
    counts = Counter(data)
    x_vals = []
    y_vals = []

    dot_spacing = 0.25  # Controls vertical spacing between dots

    for x, count in sorted(counts.items()):
        for i in range(count):
            x_vals.append(x)
            y_vals.append((i + 1) * dot_spacing)

    fig, ax = plt.subplots(figsize=(6, 4))
    ax.scatter(x_vals, y_vals, s=80, edgecolors='black', color='skyblue')

    # Add count labels on top of each column
    for x, count in sorted(counts.items()):
        ax.text(x, (count + 1) * dot_spacing, str(count), ha='center', va='bottom', fontsize=9)

    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

    ax.set_xticks(sorted(counts.keys()))
    ax.set_yticks([])

    ax.set_xlim(min(counts.keys()) - 0.5, max(counts.keys()) + 0.5)
    ax.set_ylim(0, (max(counts.values()) + 2) * dot_spacing)

    ax.grid(axis='y', linestyle='--', alpha=0.3)
    fig.tight_layout()
    return fig

def main():
    st.title("Dot Plot of Die Rolls")

    st.write(
        "Enter the number of die rolls and click 'Roll Dice & Plot' to generate a dot plot."
    )

    num_trials = st.number_input(
        "Number of die rolls", min_value=1, max_value=500, value=20, step=1
    )
    roll_button = st.button("Roll Dice & Plot")

    if roll_button:
        results = [random.randint(1, 6) for _ in range(num_trials)]
        fig = dot_plot(
            results,
            title=f"Dot Plot of {num_trials} Die Rolls",
            xlabel="Die Face"
        )
        st.pyplot(fig)

if __name__ == "__main__":
    main()
