import streamlit as st
import random
from collections import Counter

# Set page configuration
st.set_page_config(
    page_title="Mean, Median, Mode Calculator",
    page_icon="📊",
    layout="wide"
)

# Custom CSS for strikethrough text and red bold highlighting
st.markdown("""
<style>
.strikethrough {
    text-decoration: line-through;
    color: #888;
}
.red-bold {
    color: #ff0000;
    font-weight: bold;
}
.monospace {
    font-family: 'Courier New', monospace;
}
</style>
""", unsafe_allow_html=True)

# App title and instructions
st.title("📊 Mean, Median, and Mode Calculator")

st.markdown("""
### Instructions:
1. Click the **"Generate New Dataset"** button to create a random dataset
2. The app will automatically calculate and show step-by-step solutions for:
   - **Mean** (average)
   - **Median** (middle value)
   - **Mode** (most frequent value)
3. Use this as practice for statistics problems or to check your work!

---
""")

# Initialize session state for the dataset
if 'dataset_generated' not in st.session_state:
    st.session_state.dataset_generated = False

# Generate dataset button
if st.button("🎲 Generate New Dataset", type="primary"):
    # Randomly choose sample size between 10 and 25
    sample_size = random.randint(10, 25)
    
    # Decide whether to force multiple modes (20% probability)
    force_multiple_modes = random.random() < 0.20
    
    if force_multiple_modes:
        mode1, mode2 = random.sample(range(3, 55), 2)
        values = [random.randint(3, 54) for _ in range(sample_size - 4)]
        values += [mode1, mode1, mode2, mode2]
    else:
        values = [random.randint(3, 54) for _ in range(sample_size)]
    
    # Store in session state
    st.session_state.values = values
    st.session_state.dataset_generated = True

# Display calculations if dataset has been generated
if st.session_state.dataset_generated:
    values = st.session_state.values
    
    st.markdown("### 📝 Problem:")
    st.markdown("**Find the mean, median, and mode for the following data set:**")
    
    # Original values
    st.markdown("**Original values:**")
    st.code(" ".join(map(str, values)), language=None)
    
    # Sorted values
    sorted_values = sorted(values)
    st.markdown("**Sorted values:**")
    st.code(" ".join(map(str, sorted_values)), language=None)
    
    # Mean calculation
    st.markdown("### 🧮 Mean Calculation:")
    
    count = len(sorted_values)
    numerator = " + ".join(str(x) for x in sorted_values)
    total = sum(sorted_values)
    
    st.markdown("**Step-by-step mean calculation:**")
    
    # Create the fraction display
    max_width = max(len(numerator), len(str(count)))
    
    mean_calc = f"""mean = {numerator}
       {'─' * max_width}
       {str(count):^{max_width}}

mean = {total}
       {'─' * max(len(str(total)), len(str(count)))}
       {str(count):^{max(len(str(total)), len(str(count)))}}

mean = {total / count:.2f}"""
    
    st.code(mean_calc, language=None)
    
    # Median calculation
    st.markdown("### 📍 Median Calculation:")
    
    working_list = sorted_values.copy()
    left = 0
    right = len(working_list) - 1
    
    # Strike values until we reach the middle
    while right - left >= 2:
        left += 1
        right -= 1
    
    # Create display with strikethrough and highlighting
    display_parts = []
    for i, val in enumerate(working_list):
        if i < left or i > right:
            display_parts.append(f'<span class="strikethrough">{val}</span>')
        else:
            display_parts.append(f'<span class="red-bold">{val}</span>')
    
    st.markdown(
        f'**After striking outer values:** <span class="monospace">{" ".join(display_parts)}</span>',
        unsafe_allow_html=True
    )
    
    if right == left:
        st.write(f"Only one number remains: **{working_list[left]}**")
        st.write(f"**Median = {working_list[left]}**")
        median_value = working_list[left]
    else:
        st.write(f"Two numbers remain: **{working_list[left]}** and **{working_list[right]}**")
        median_calc = (working_list[left] + working_list[right]) / 2
        st.write(f"**Median = ({working_list[left]} + {working_list[right]}) ÷ 2 = {median_calc:.2f}**")
        median_value = median_calc
    
    # Mode calculation
    st.markdown("### 🎯 Mode Calculation:")
    
    counts = Counter(sorted_values)
    max_count = max(counts.values())
    
    if max_count == 1:
        mode_result = "**No mode** (all values appear only once)"
    else:
        modes = [x for x, c in counts.items() if c == max_count]
        if len(modes) == 1:
            mode_result = f"**Mode: {modes[0]}** (appears {max_count} times)"
        else:
            mode_result = f"**Modes: {', '.join(map(str, modes))}** (each appears {max_count} times)"
    
    st.markdown(mode_result)
    
    # Summary
    st.markdown("### 📋 Summary:")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Mean", f"{total / count:.2f}")
    
    with col2:
        if isinstance(median_value, float):
            st.metric("Median", f"{median_value:.2f}")
        else:
            st.metric("Median", str(median_value))
    
    with col3:
        if max_count == 1:
            st.metric("Mode", "None")
        else:
            if len(modes) == 1:
                st.metric("Mode", str(modes[0]))
            else:
                st.metric("Modes", f"{len(modes)} values")

else:
    st.info("👆 Click the 'Generate New Dataset' button above to start!")

# Footer
st.markdown("---")
st.markdown("*This app generates random datasets and shows step-by-step calculations for mean, median, and mode. Perfect for statistics practice!*")
