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

    # Vertical dot plot, fixed-width columns
    y_label = "FREQUENCY"
    max_height = max(freq.values())
    label_padding = max_height - len(y_label)
    vertical_label = [' '] * label_padding + list(y_label)

    # Find max label width (for alignment)
    y_num_width = len(str(max_height))
    label_col_width = max(len(y_label), y_num_width + 1) + 1  # +1 for space after label

    # Generate plot lines
    dot_plot_lines = []
    for idx, row in enumerate(range(max_height, 0, -1)):
        # Y label or blank
        label = vertical_label[idx] if idx < len(vertical_label) else ' '
        # y value
        y_val = f"{row}".rjust(y_num_width)
        line = f"{label} {y_val} |"
        # Dots
        for x in range(1, 7):
            line += " ● " if freq[x] >= row else "   "
        dot_plot_lines.append(line)
    # X-axis (aligned)
    x_axis = " " * (len(y_label) + y_num_width + 2) + "+" + "---"*6
    dot_plot_lines.append(x_axis)
    x_ticks = " " * (len(y_label) + y_num_width + 3) + "1  2  3  4  5  6 (x)"
    dot_plot_lines.append(x_ticks)

    st.write("**Vertical Dot Plot:**")
    st.code("\
