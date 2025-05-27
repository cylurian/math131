import streamlit as st
import random
import statistics

def tukey_quartiles(data_sorted):
    """
    Computes Q1 and Q3 using Tukey’s method (boxplot-style).
    For odd-length datasets, the median is excluded from both halves.
    For even-length datasets, each half is split equally.
    """
    n = len(data_sorted)
    if n % 2 == 1:
        median_index = n // 2
        lower_half = data_sorted[:median_index]
        upper_half = data_sorted[median_index + 1:]
    else:
        mid = n // 2
        lower_half = data_sorted[:mid]
        upper_half = data_sorted[mid:]
    q1 = statistics.median(lower_half)
    q3 = statistics.median(upper_half)
    return q1, q3

st.set_page_config(page_title="Tukey Five-Number Summary & Outlier Detection", layout="centered")

st.title("Tukey Five-Number Summary & Outlier Detection")
st.write(
    """
    This app generates a random dataset, optionally introduces an outlier, and calculates the five-number summary using Tukey's method.
    It also applies Tukey's outlier rule (1.5 × IQR) and highlights any outliers found.
    """
)

# Sidebar for controls (no seed for randomness)
st.sidebar.header("Controls")
force_outlier = st.sidebar.checkbox("Force an outlier", value=False)
n_base = st.sidebar.slider("Dataset size (n)", min_value=11, max_value=25, value=15)
value_range = st.sidebar.slider("Random values range", min_value=1, max_value=100, value=(10, 50))

# No random.seed() — dataset changes on every rerun/reload

# Step 1: Generate base dataset
data = [random.randint(value_range[0], value_range[1]) for _ in range(n_base)]
data_sorted = sorted(data)

# Outlier logic
outlier_injected = False
if force_outlier or random.random() < 0.3:
    data_sorted_base = data_sorted.copy()
    q1_base, q3_base = tukey_quartiles(data_sorted_base)
    iqr_base = q3_base - q1_base
    lower_bound_base = q1_base - 1.5 * iqr_base
    upper_bound_base = q3_base + 1.5 * iqr_base

    idx_to_replace = random.randint(0, n_base - 1)
    # Generate the outlier value (below or above bounds of base dataset)
    if random.choice([True, False]):
        new_value = int(lower_bound_base - abs(q3_base - q1_base))
    else:
        new_value = int(upper_bound_base + abs(q3_base - q1_base))

    data[idx_to_replace] = new_value
    data_sorted = sorted(data)
    outlier_injected = True

# Step 2: Five-number summary using Tukey's method
min_val = min(data_sorted)
max_val = max(data_sorted)
median_val = statistics.median(data_sorted)
q1_tukey, q3_tukey = tukey_quartiles(data_sorted)

# Step 3: Tukey's rule for outliers
iqr = q3_tukey - q1_tukey
lower_bound = q1_tukey - 1.5 * iqr
upper_bound = q3_tukey + 1.5 * iqr
outliers = [x for x in data_sorted if x < lower_bound or x > upper_bound]

# ---- Streamlit Output ----

st.subheader("Generated Data")
st.code(', '.join(map(str, data_sorted)), language="python")
st.write(f"n = {len(data_sorted)}")
if outlier_injected:
    st.warning("Outlier injected into this dataset.")

st.subheader("Five-Number Summary (Tukey Method)")
st.write(
    f"""
    - **Minimum:** {min_val}  
    - **Q1:** {q1_tukey:.2f}  
    - **Median (Q2):** {median_val}  
    - **Q3:** {q3_tukey:.2f}  
    - **Maximum:** {max_val}
    """
)

st.subheader("Tukey's Outlier Analysis & Calculations")
with st.expander("Show calculations for bounds and IQR"):
    st.write(f"**Q1 (First Quartile):** {q1_tukey:.2f}")
    st.write(f"**Q3 (Third Quartile):** {q3_tukey:.2f}")
    st.write(f"**IQR = Q3 - Q1 = {q3_tukey:.2f} - {q1_tukey:.2f} = {iqr:.2f}**")
    st.write(f"**Lower Bound = Q1 - 1.5 × IQR = {q1_tukey:.2f} - 1.5 × {iqr:.2f} = {lower_bound:.2f}**")
    st.write(f"**Upper Bound = Q3 + 1.5 × IQR = {q3_tukey:.2f} + 1.5 × {iqr:.2f} = {upper_bound:.2f}**")

st.subheader("Outliers")
if not outliers:
    st.success("No outliers found in the dataset.")
else:
    for x in outliers:
        if x < lower_bound:
            st.error(f"Outlier {x} is **below** the lower bound ({lower_bound:.2f}).")
        else:
            st.error(f"Outlier {x} is **above** the upper bound ({upper_bound:.2f}).")

st.caption("App by Frank – uses Tukey's method (boxplot convention) for quartiles and outlier detection.")
