import random
import streamlit as st
import matplotlib.pyplot as plt

num_trials = st.number_input("Enter the number of die rolls:", min_value=1, value=60, step=1)

if st.button("Roll the die"):
    results = [random.randint(1, 6) for _ in range(num_trials)]
    st.write("**Results:**")
    res_lines = []
    for i in range(0, num_trials, 25):
        res_lines.append(" ".join(str(x) for x in results[i:i+25]))
    st.code("\n".join(res_lines))

    # Frequency table
    freq = {x: 0 for x in range(1, 7)}
    for result in results:
        freq[result] += 1
    table = "x  |  f\n" + "--------\n"
    for x in range(1, 7):
        table += f"{x}  |  {freq[x]}\n"
    st.code(table)

    # Matplotlib dot plot
    st.write("**Vertical Dot Plot:**")
    fig, ax = plt.subplots(figsize=(6, 4))
    for x in range(1, 7):
        y = range(1, freq[x]+1)
        ax.plot([x]*freq[x], y, 'o', color='black')
    ax.set_xticks([1,2,3,4,5,6])
    ax.set_yticks(range(1, max(freq.values())+1))
    ax.set_xlabel("x")
    ax.set_ylabel("Frequency")
    ax.set_title("Vertical Dot Plot of Die Rolls")
    ax.set_xlim(0.5, 6.5)
    ax.grid(axis='y', linestyle=':')
    st.pyplot(fig)
