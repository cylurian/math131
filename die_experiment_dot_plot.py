import random
import streamlit as st

st.title("Die Roll Simulation")

st.write("Enter the number of die rolls.  The results, frequency table, and a vertical dot plot will be shown below.  ")

# User input for number of trials
num_trials = st.number_input("Number of die rolls:  ", min_value=1, value=100)

if st.button("Roll Dice"):
    # Roll the die
    results = [random.randint(1, 6) for _ in range(num_trials)]

    # Show results, 25 per line
    st.subheader("Results:  ")
    res_lines = []
    line = ""
    for i, val in enumerate(results):
        line += f"{val}  "
        if (i + 1) % 25 == 0:
            res_lines.append(line)
            line = ""
    if line:
        res_lines.append(line)
    for l in res_lines:
        st.text(l)

    # Frequency table
    freq = {x: 0 for x in range(1, 7)}
    for result in results:
        freq[result] += 1

    st.subheader("Frequency Table:  ")
    table = "x  |  f  \n--------  \n"
    for x in range(1, 7):
        table += f"{x}  |  {freq[x]}  \n"
    st.text(table)

    # Vertical label setup
    y_label = "FREQUENCY"
    max_height = max(freq.values())
    label_start = (max_height - len(y_label)) // 2
    vertical_label = [' '] * max(0, label_start) + list(y_label)
    while len(vertical_label) < max_height:
        vertical_label.append(' ')

    # Build dot plot as a string
    dot_plot = "\nVertical Dot Plot:  \n\n"
    for idx, row in enumerate(range(max_height, 0, -1)):
        dot_plot += f"{vertical_label[idx]} {row:2} |  "
        for x in range(1, 7):
            if freq[x] >= row:
                dot_plot += '●  '
            else:
                dot_plot += '   '
        dot_plot += '\n'
    dot_plot += "   +" + "---"*6 + "\n"
    dot_plot += "    1  2  3  4  5  6 (x)  "

    st.text(dot_plot)
