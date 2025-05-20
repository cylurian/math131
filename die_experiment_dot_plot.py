import random
import streamlit as st

num_trials = st.number_input("Enter the number of die rolls:", min_value=1, value=60, step=1)

if st.button("Roll the die"):
    results = [random.randint(1, 6) for _ in range(num_trials)]

    # Show results 25 per line
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

    # Vertical dot plot, monospaced for Streamlit
    y_label = "FREQUENCY"
    max_height = max(freq.values())
    label_padding = max_height - len(y_label)
    vertical_label = [' '] * label_padding + list(y_label)

    dot_plot_lines = []
    for idx, row in enumerate(range(max_height, 0, -1)):
        label = vertical_label[idx] if idx < len(vertical_label) else ' '
        line = f"{label} {row:2} |"
        for x in range(1, 7):
            line += " ● " if freq[x] >= row else "   "
        dot_plot_lines.append(line)
    dot_plot_lines.append("   +" + "---"*6)
    dot_plot_lines.append("    1  2  3  4  5  6 (x)")

    st.write("**Vertical Dot Plot:**")
    st.code("\n".join(dot_plot_lines))
