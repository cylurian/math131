import streamlit as st
import random
import math
from textwrap import wrap
import matplotlib.pyplot as plt
import numpy as np

# Set page configuration
st.set_page_config(
    page_title="Statistical Data Analysis Generator",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Enhanced list with data type specifications and appropriate ranges
paragraphs = [
    {
        "title": "Fitness Center Exercise Durations",
        "text": "A local fitness center is tracking the number of minutes each member "
                "spends exercising during a single visit. The center wants to analyze "
                "the distribution of exercise durations among its members.",
        "data_type": "continuous",
        "min_val": 15,
        "max_val": 120,
        "decimals": 1
    },
    {
        "title": "Air Pollution Concentration Levels",
        "text": "A city's environmental agency is measuring the concentration of a "
                "certain pollutant in micrograms per cubic meter at various locations. "
                "The agency needs to summarize the spread and frequency of these "
                "pollution levels.",
        "data_type": "continuous",
        "min_val": 0.5,
        "max_val": 85.0,
        "decimals": 2
    },
    {
        "title": "Student Math Test Scores",
        "text": "A teacher records the scores of students on a math test. The teacher "
                "wants to visualize how the class performed overall.",
        "data_type": "discrete",
        "min_val": 45,
        "max_val": 100,
        "decimals": 0
    },
    {
        "title": "Apple Weights in a Supermarket",
        "text": "A supermarket is analyzing the weights of apples in a shipment. The "
                "store manager wants to understand the distribution of apple weights.",
        "data_type": "continuous",
        "min_val": 120,
        "max_val": 250,
        "decimals": 1
    },
    {
        "title": "Patient Ages in Emergency Room",
        "text": "A hospital is studying the ages of patients admitted to the emergency "
                "room over a month. The hospital wants to see the age distribution of "
                "their patients.",
        "data_type": "discrete",
        "min_val": 1,
        "max_val": 95,
        "decimals": 0
    },
    {
        "title": "Video Game Level Completion Times",
        "text": "A video game company is collecting data on the time it takes players "
                "to complete a level. The company wants to analyze player performance.",
        "data_type": "continuous",
        "min_val": 45.5,
        "max_val": 180.0,
        "decimals": 1
    },
    {
        "title": "Fish Lengths in a Lake",
        "text": "A wildlife biologist is recording the lengths of fish caught in a lake. "
                "The biologist wants to study the size distribution of the fish population.",
        "data_type": "continuous",
        "min_val": 8.2,
        "max_val": 35.7,
        "decimals": 1
    },
    {
        "title": "Machine Temperature Monitoring",
        "text": "A manufacturing plant is monitoring the temperature of a machine at "
                "regular intervals. The plant manager wants to assess the variability "
                "in machine temperature.",
        "data_type": "continuous",
        "min_val": 65.5,
        "max_val": 95.8,
        "decimals": 1
    },
    {
        "title": "Student Reading Challenge Pages Read",
        "text": "A school is tracking the number of pages students read for a reading "
                "challenge. The school librarian wants to see how much students are reading.",
        "data_type": "discrete",
        "min_val": 25,
        "max_val": 450,
        "decimals": 0
    },
    {
        "title": "Bus Route Travel Times",
        "text": "A transportation department is recording the travel times for buses on "
                "a particular route. The department wants to evaluate the consistency "
                "of bus travel times.",
        "data_type": "continuous",
        "min_val": 22.5,
        "max_val": 38.2,
        "decimals": 1
    },
    {
        "title": "Coffee Shop Daily Sales Amounts",
        "text": "A coffee shop owner is recording the total sales in dollars each day. "
                "The owner wants to analyze the variability in daily sales.",
        "data_type": "continuous",
        "min_val": 245.50,
        "max_val": 890.75,
        "decimals": 2
    },
    {
        "title": "Classroom Quiz Completion Times",
        "text": "A teacher is timing how long each student takes to finish a quiz. "
                "The teacher wants to see the distribution of completion times.",
        "data_type": "continuous",
        "min_val": 8.5,
        "max_val": 25.0,
        "decimals": 1
    },
    {
        "title": "Bakery Bread Loaf Weights",
        "text": "A bakery is weighing each loaf of bread produced in a day. The baker "
                "wants to ensure consistency in loaf weights.",
        "data_type": "continuous",
        "min_val": 485.2,
        "max_val": 520.8,
        "decimals": 1
    },
    {
        "title": "Hospital Blood Pressure Readings",
        "text": "A hospital is recording systolic blood pressure readings of patients "
                "during checkups. The staff wants to analyze the range of blood pressure values.",
        "data_type": "discrete",
        "min_val": 90,
        "max_val": 180,
        "decimals": 0
    },
    {
        "title": "Library Book Borrowing Durations (in hours)",
        "text": "A library is tracking how many hours each book is checked out before "
                "being returned. The librarian wants to study borrowing patterns.",
        "data_type": "mixed",
        "min_val": 24,
        "max_val": 336,
        "decimals": 1
    },
    {
        "title": "Factory Product Defect Rates",
        "text": "A factory is measuring the percentage of defects found in each batch of "
                "products. The quality control manager wants to monitor defect rates.",
        "data_type": "continuous",
        "min_val": 0.1,
        "max_val": 8.5,
        "decimals": 2
    },
    {
        "title": "Supermarket Customer Wait Times",
        "text": "A supermarket is measuring how long customers wait in line at checkout. "
                "The manager wants to reduce wait times.",
        "data_type": "continuous",
        "min_val": 0.5,
        "max_val": 12.8,
        "decimals": 1
    },
    {
        "title": "School Bus Arrival Times",
        "text": "A school is recording the arrival times of buses each morning. The "
                "administration wants to ensure buses are on schedule.",
        "data_type": "mixed",
        "min_val": 7.15,
        "max_val": 8.45,
        "decimals": 2
    },
    {
        "title": "Restaurant Meal Preparation Times",
        "text": "A restaurant is timing how long it takes to prepare each meal. The chef "
                "wants to improve kitchen efficiency.",
        "data_type": "continuous",
        "min_val": 8.5,
        "max_val": 35.0,
        "decimals": 1
    },
    {
        "title": "Athlete Sprint Times",
        "text": "A coach is recording the times it takes athletes to complete a 100-meter "
                "sprint. The coach wants to track improvements in speed.",
        "data_type": "continuous",
        "min_val": 10.85,
        "max_val": 15.42,
        "decimals": 2
    },
    {
        "title": "Movie Theater Ticket Revenue",
        "text": "A movie theater is recording the total revenue from ticket sales for each show. "
                "The manager wants to analyze attendance patterns.",
        "data_type": "continuous",
        "min_val": 125.50,
        "max_val": 1250.75,
        "decimals": 2
    },
    {
        "title": "Grocery Store Product Weights",
        "text": "A grocery store is weighing a popular product each day. The manager wants to monitor inventory levels.",
        "data_type": "continuous",
        "min_val": 0.8,
        "max_val": 2.5,
        "decimals": 2
    },
    {
        "title": "Pharmacy Prescription Fill Times",
        "text": "A pharmacy is measuring how long it takes to fill each prescription. "
                "The pharmacist wants to improve service speed.",
        "data_type": "continuous",
        "min_val": 3.5,
        "max_val": 18.2,
        "decimals": 1
    },
    {
        "title": "Hotel Room Occupancy Rates",
        "text": "A hotel is recording the percentage of rooms occupied each night. The manager "
                "wants to analyze occupancy trends.",
        "data_type": "continuous",
        "min_val": 35.5,
        "max_val": 98.2,
        "decimals": 1
    },
    {
        "title": "Park Visitor Stay Durations",
        "text": "A city park is measuring how long visitors stay in the park each day. The park "
                "director wants to understand usage patterns.",
        "data_type": "continuous",
        "min_val": 0.5,
        "max_val": 6.5,
        "decimals": 1
    },
    {
        "title": "Warehouse Package Weights",
        "text": "A warehouse is weighing packages before shipping. The supervisor wants "
                "to ensure packages meet weight requirements.",
        "data_type": "continuous",
        "min_val": 0.5,
        "max_val": 25.8,
        "decimals": 1
    },
    {
        "title": "Classroom Attendance Durations",
        "text": "A teacher is recording the number of minutes students are present each day. The "
                "school wants to monitor attendance rates.",
        "data_type": "mixed",
        "min_val": 180,
        "max_val": 420,
        "decimals": 0
    },
    {
        "title": "Taxi Ride Distances",
        "text": "A taxi company is measuring the distance of each ride in kilometers. "
                "The company wants to analyze trip lengths.",
        "data_type": "continuous",
        "min_val": 1.2,
        "max_val": 45.8,
        "decimals": 1
    },
    {
        "title": "Gym Member Monthly Exercise Hours",
        "text": "A gym is tracking how many hours each member exercises in a month. The "
                "manager wants to encourage frequent visits.",
        "data_type": "continuous",
        "min_val": 2.5,
        "max_val": 85.0,
        "decimals": 1
    },
    {
        "title": "Farm Crop Yield per Acre",
        "text": "A farmer is recording the yield in kilograms per acre for each field. "
                "The farmer wants to compare productivity across fields.",
        "data_type": "continuous",
        "min_val": 1250.5,
        "max_val": 3850.2,
        "decimals": 1
    }
]

def tukey_hinges(data):
    """Calculate Tukey's hinges for five-number summary"""
    n = len(data)
    median = np.median(data)
    if n % 2 == 0:
        lower_half = data[:n//2]
        upper_half = data[n//2:]
    else:
        lower_half = data[:n//2+1]
        upper_half = data[n//2:]
    q1 = np.median(lower_half)
    q3 = np.median(upper_half)
    return round(float(q1), 2), round(float(median), 2), round(float(q3), 2)

def generate_analysis():
    """Generate a complete statistical analysis"""
    
    # Randomly select a paragraph for this dataset
    problem = random.choice(paragraphs)
    title = problem["title"]
    problem_paragraph = problem["text"]
    data_type = problem["data_type"]
    min_val = problem["min_val"]
    max_val = problem["max_val"]
    decimals = problem["decimals"]

    # Choose sample size range: 50% chance for 25-49, 50% for 50-200
    if random.random() < 0.5:
        n = random.randint(25, 49)
    else:
        n = random.randint(50, 200)

    # Generate data based on the problem type
    data = []
    for _ in range(n):
        if data_type == "discrete":
            # Generate discrete values only
            data.append(random.randint(int(min_val), int(max_val)))
        elif data_type == "continuous":
            # Generate continuous values only
            value = random.uniform(min_val, max_val)
            data.append(round(value, decimals))
        elif data_type == "mixed":
            # Generate mix of discrete and continuous values
            if random.random() < 0.5:
                # Continuous value
                value = random.uniform(min_val, max_val)
                data.append(round(value, decimals))
            else:
                # Discrete value (rounded to nearest integer)
                data.append(round(random.uniform(min_val, max_val)))

    return problem, data

# Streamlit App
def main():
    st.title("📊 Statistical Data Analysis Generator")
    
    # Instructions in sidebar
    with st.sidebar:
        st.header("📋 How to Use This App")
        st.markdown("""
        **Welcome to the Statistical Data Analysis Generator!**
        
        This app generates realistic datasets with complete statistical analysis including:
        
        ✅ **Random realistic data** based on real-world scenarios  
        ✅ **Descriptive statistics** (mean, median, standard deviation)  
        ✅ **Five-number summary** using Tukey's hinges  
        ✅ **Frequency distribution table** with professional formatting  
        ✅ **Histogram visualization** with proper binning  
        
        ### 🚀 Getting Started:
        1. Click the **"Generate New Analysis"** button below
        2. View the generated scenario and data
        3. Examine the statistical summary
        4. Study the frequency table and histogram
        5. Click again for a new random dataset!
        
        ### 📚 Perfect for:
        - Statistics students and educators
        - Data analysis practice
        - Understanding distributions
        - Learning histogram construction
        - Exploring real-world data scenarios
        
        ### 🔄 Features:
        - **30+ realistic scenarios** from various industries
        - **Smart data generation** matching each context
        - **Professional formatting** for easy reading
        - **Interactive visualization** with matplotlib
        - **Proper statistical methods** (Sturges' rule, Tukey's hinges)
        """)
        
        st.markdown("---")
        st.markdown("**💡 Tip:** Each click generates completely new data with different scenarios!")

    # Main content area
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        if st.button("🎲 Generate New Analysis", type="primary", use_container_width=True):
            st.session_state.generate_new = True
    
    # Initialize session state
    if 'generate_new' not in st.session_state:
        st.session_state.generate_new = True
    
    if st.session_state.generate_new:
        # Generate new analysis
        problem, data = generate_analysis()
        
        # Store in session state
        st.session_state.problem = problem
        st.session_state.data = data
        st.session_state.generate_new = False
    
    # Use stored data
    if 'problem' in st.session_state and 'data' in st.session_state:
        problem = st.session_state.problem
        data = st.session_state.data
        
        title = problem["title"]
        problem_paragraph = problem["text"]
        data_type = problem["data_type"]
        decimals = problem["decimals"]
        
        # Display title and description
        st.header(f"📈 {title}")
        st.write(problem_paragraph)
        st.markdown("---")
        
        # Create two columns for data display
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("📊 Raw Data")
            # Display original data
            data_strs = [str(x) for x in data]
            joined = ', '.join(data_strs)
            st.text_area(f"Data points (n = {len(data)}):", joined, height=100)
        
        with col2:
            st.subheader("🔢 Sorted Data")
            # Display sorted data
            sorted_data_display = sorted(data)
            sorted_data_strs = [str(x) for x in sorted_data_display]
            sorted_joined = ', '.join(sorted_data_strs)
            st.text_area("Sorted data (lowest to highest):", sorted_joined, height=100)
        
        # Calculate statistics
        data_np = np.array(data)
        mean = round(np.mean(data_np), 2)
        median = round(np.median(data_np), 2)
        std = round(np.std(data_np, ddof=1), 2)
        
        # Tukey's Hinges for five-number summary
        sorted_data = np.sort(data_np)
        min_val_stat = round(float(sorted_data[0]), 2)
        max_val_stat = round(float(sorted_data[-1]), 2)
        
        q1, med, q3 = tukey_hinges(sorted_data)
        five_num = [min_val_stat, q1, med, q3, max_val_stat]
        
        # Display statistics
        st.markdown("---")
        st.subheader("📈 Statistical Summary")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.metric("Mean", mean)
            st.metric("Median", median)
            st.metric("Sample Standard Deviation", std)
        
        with col2:
            st.write("**Five Number Summary (Tukey's Hinges):**")
            st.write(f"• **Min:** {five_num[0]}")
            st.write(f"• **Q1:** {five_num[1]}")
            st.write(f"• **Median:** {five_num[2]}")
            st.write(f"• **Q3:** {five_num[3]}")
            st.write(f"• **Max:** {five_num[4]}")
        
        # Calculate bins
        k = math.ceil(1 + math.log2(len(data)))
        actual_min = min(data)
        actual_max = max(data)
        
        # Find appropriate starting point and range
        if data_type == "discrete":
            data_min = math.floor(actual_min)
            data_max = math.ceil(actual_max)
        else:
            data_range = actual_max - actual_min
            if data_range >= 100:
                data_min = math.floor(actual_min / 10) * 10
            elif data_range >= 10:
                data_min = math.floor(actual_min)
            else:
                if decimals == 0:
                    data_min = math.floor(actual_min)
                elif decimals == 1:
                    data_min = math.floor(actual_min * 10) / 10
                else:
                    data_min = math.floor(actual_min * 100) / 100
            data_max = actual_max
        
        # Calculate range and bin size
        data_range = data_max - data_min
        bin_size = data_range / k
        
        # Round bin size to a nice number
        if data_type == "discrete":
            bin_size = max(1, math.ceil(bin_size))
        else:
            if bin_size >= 10:
                bin_size = math.ceil(bin_size)
            elif bin_size >= 1:
                bin_size = math.ceil(bin_size * 10) / 10
            else:
                if decimals <= 1:
                    bin_size = math.ceil(bin_size * 10) / 10
                else:
                    bin_size = math.ceil(bin_size * 100) / 100
        
        # Recalculate k based on the nice bin size
        k = math.ceil(data_range / bin_size)
        
        # Create bin edges
        bin_edges = []
        current_edge = data_min
        for i in range(k + 1):
            bin_edges.append(current_edge)
            current_edge += bin_size
        
        # Ensure the last edge covers the maximum value
        if bin_edges[-1] < data_max:
            bin_edges[-1] = data_max + (bin_size * 0.01)
        
        # Build frequency table
        freqs = [0] * k
        for x in data:
            for i in range(k):
                if bin_edges[i] <= x < bin_edges[i + 1]:
                    freqs[i] += 1
                    break
                if i == k - 1 and x >= bin_edges[i]:
                    freqs[i] += 1
        
        # Display binning information
        st.markdown("---")
        st.subheader("📊 Histogram Analysis")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Number of bins", k)
        with col2:
            st.metric("Bin size", bin_size)
        with col3:
            st.metric("First bin starts at", data_min)
        
        # Create frequency table
        st.subheader("📋 Frequency Distribution Table")
        
        # Create table data
        table_data = []
        for i in range(k):
            left = bin_edges[i]
            right = bin_edges[i + 1]
            if data_type == "discrete":
                interval = f"[{int(left)}, {int(right)})"
            else:
                if decimals == 0:
                    interval = f"[{int(left)}, {int(right)})"
                elif decimals == 1:
                    interval = f"[{left:.1f}, {right:.1f})"
                else:
                    interval = f"[{left:.2f}, {right:.2f})"
            table_data.append({"Interval": interval, "Frequency": freqs[i]})
        
        # Display as dataframe
        import pandas as pd
        df = pd.DataFrame(table_data)
        st.dataframe(df, use_container_width=True, hide_index=True)
        
        # Create and display histogram
        st.subheader("📊 Histogram")
        
        fig, ax = plt.subplots(figsize=(10, 6))
        bar_lefts = bin_edges[:-1]
        ax.bar(
            bar_lefts,
            freqs,
            width=bin_size,
            align='edge',
            edgecolor='black',
            alpha=0.7,
            color='steelblue'
        )
        ax.set_xlabel('Value')
        ax.set_ylabel('Frequency')
        ax.set_title(title)
        ax.set_xticks(bin_edges)
        if max(len(f"{edge:.2f}") for edge in bin_edges) > 4:
            plt.xticks(rotation=45)
        ax.grid(axis='y', linestyle='--', alpha=0.7)
        plt.tight_layout()
        
        st.pyplot(fig)
        
        # Additional insights
        st.markdown("---")
        st.subheader("💡 Quick Insights")
        col1, col2 = st.columns(2)
        
        with col1:
            st.write(f"**Data Type:** {data_type.title()}")
            st.write(f"**Sample Size:** {len(data)} observations")
            st.write(f"**Range:** {max_val_stat - min_val_stat}")
        
        with col2:
            # Find mode (most frequent bin)
            max_freq = max(freqs)
            mode_bin = freqs.index(max_freq)
            st.write(f"**Most Frequent Bin:** {table_data[mode_bin]['Interval']}")
            st.write(f"**Highest Frequency:** {max_freq}")
            st.write(f"**Distribution Shape:** {'Roughly symmetric' if abs(mean - median) < std/2 else 'Skewed'}")

if __name__ == "__main__":
    main()
