import streamlit as st
import matplotlib.pyplot as plt
import random
import numpy as np

def roll_die():
    """Simulate rolling a 6-sided die"""
    return random.randint(1, 6)

def create_dot_plot(results):
    """Create a dot plot of the die roll results"""
    # Count occurrences of each outcome
    counts = {i: results.count(i) for i in range(1, 7)}
    max_count = max(counts.values()) if any(counts.values()) else 1
    num_trials = len(results)
    
    # Dynamic sizing based on number of trials
    if num_trials <= 200:
        fig_width, fig_height = 10, 6
        dot_size = 50
        y_tick_interval = 1
    elif num_trials <= 500:
        fig_width, fig_height = 12, 8
        dot_size = 25
        y_tick_interval = max(1, max_count // 20)
    elif num_trials <= 1000:
        fig_width, fig_height = 14, 10
        dot_size = 15
        y_tick_interval = max(1, max_count // 15)
    else:
        fig_width, fig_height = 16, 12
        dot_size = 10
        y_tick_interval = max(1, max_count // 12)
    
    # Create the plot with dynamic size
    fig, ax = plt.subplots(figsize=(fig_width, fig_height))
    
    # For each die face, plot dots vertically
    for face, count in counts.items():
        if count > 0:
            # Create y-coordinates for dots (stacked vertically)
            y_coords = np.arange(1, count + 1)
            # Create x-coordinates (all at the same face value)
            x_coords = [face] * count
            
            # Plot dots with dynamic size
            ax.scatter(
                x_coords, 
                y_coords, 
                s=dot_size, 
                alpha=0.7, 
                color='blue',
                edgecolors='darkblue',
                linewidth=0.5
            )
    
    # Customize the plot
    ax.set_xlabel('Die Face', fontsize=12, fontweight='bold')
    ax.set_ylabel('Frequency', fontsize=12, fontweight='bold')
    ax.set_title(
        f'Dot Plot of Die Roll Results ({num_trials} trials)', 
        fontsize=14, 
        fontweight='bold'
    )
    
    # Set x-axis to show all die faces
    ax.set_xlim(0.5, 6.5)
    ax.set_xticks(range(1, 7))
    
    # Set y-axis with dynamic tick spacing
    ax.set_ylim(0, max_count + 1)
    
    # Create y-ticks with appropriate spacing to avoid crowding
    if max_count <= 20:
        y_ticks = range(0, max_count + 2)
    else:
        y_ticks = range(0, max_count + 1, y_tick_interval)
        if max_count not in y_ticks:
            y_ticks = list(y_ticks) + [max_count]
    
    ax.set_yticks(y_ticks)
    
    # Rotate y-axis labels if there are many ticks
    if len(y_ticks) > 15:
        ax.tick_params(axis='y', rotation=45)
    
    # Add grid for better readability
    ax.grid(True, alpha=0.3)
    
    # Remove top and right spines for cleaner look
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    # Add summary statistics as text
    expected_freq = num_trials / 6
    ax.text(
        0.02, 0.98, 
        f'Expected frequency per face: {expected_freq:.1f}',
        transform=ax.transAxes,
        verticalalignment='top',
        bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8)
    )
    
    plt.tight_layout()
    return fig

def main():
    """Main Streamlit app"""
    # Page configuration
    st.set_page_config(
        page_title="🎲 Die Rolling Simulator",
        page_icon="🎲",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # App title and description
    st.title("🎲 Die Rolling Simulation")
    st.markdown("---")
    
    # Instructions in sidebar
    with st.sidebar:
        st.header("📋 How to Use This App")
        st.markdown("""
        **Welcome to the Die Rolling Simulator!**
        
        This app simulates rolling a 6-sided die and creates a dot plot 
        to visualize the results.
        
        **Instructions:**
        1. Use the slider below to select the number of die rolls
        2. Click the "🎲 Roll the Die!" button to start the simulation
        3. View the results in the dot plot and statistics table
        4. Try different numbers of trials to see how the distribution changes
        
        **What to Expect:**
        - **Small trials (≤200)**: You'll see individual dots clearly
        - **Medium trials (201-500)**: Dots become smaller but remain visible
        - **Large trials (501+)**: Very small dots, focus on overall patterns
        
        **Educational Notes:**
        - With more trials, results should approach equal distribution (≈16.67% each face)
        - This demonstrates the Law of Large Numbers
        - Each face has a theoretical probability of 1/6 ≈ 16.67%
        """)
        
        st.markdown("---")
        st.markdown("**💡 Tip:** Try comparing results with different numbers of trials!")
    
    # Main content area
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.header("Simulation Parameters")
        
        # Number of trials input
        num_trials = st.slider(
            "Number of die rolls:",
            min_value=1,
            max_value=5000,
            value=100,
            step=1,
            help="Choose how many times to roll the die. More trials = more accurate results!"
        )
        
        # Display expected results
        expected_freq = num_trials / 6
        st.info(f"📊 Expected frequency per face: **{expected_freq:.1f}** rolls")
        
        # Roll button
        if st.button("🎲 Roll the Die!", type="primary", use_container_width=True):
            # Perform the simulation
            with st.spinner(f"Rolling the die {num_trials} times..."):
                results = []
                
                # Create progress bar for large simulations
                if num_trials > 500:
                    progress_bar = st.progress(0)
                    for i in range(num_trials):
                        roll = roll_die()
                        results.append(roll)
                        if (i + 1) % (num_trials // 100) == 0:
                            progress_bar.progress((i + 1) / num_trials)
                    progress_bar.empty()
                else:
                    for i in range(num_trials):
                        roll = roll_die()
                        results.append(roll)
            
            # Store results in session state
            st.session_state.results = results
            st.session_state.num_trials = num_trials
            st.success(f"✅ Completed {num_trials} die rolls!")
    
    with col2:
        st.header("Quick Stats")
        if 'results' in st.session_state:
            results = st.session_state.results
            
            # Calculate basic statistics
            total_rolls = len(results)
            unique_faces = len(set(results))
            most_common = max(set(results), key=results.count)
            most_common_count = results.count(most_common)
            
            # Display metrics
            st.metric("Total Rolls", total_rolls)
            st.metric("Unique Faces Rolled", f"{unique_faces}/6")
            st.metric("Most Common Face", f"{most_common} ({most_common_count} times)")
        else:
            st.info("👆 Click 'Roll the Die!' to see statistics")
    
    # Display results if available
    if 'results' in st.session_state:
        results = st.session_state.results
        num_trials = st.session_state.num_trials
        
        st.markdown("---")
        st.header("📊 Results")
        
        # Create two columns for plot and detailed stats
        plot_col, stats_col = st.columns([3, 1])
        
        with plot_col:
            st.subheader("Dot Plot Visualization")
            
            # Create and display the plot
            fig = create_dot_plot(results)
            st.pyplot(fig)
            plt.close(fig)  # Close figure to free memory
            
            # Plot information
            max_count = max([results.count(i) for i in range(1, 7)])
            if num_trials <= 200:
                dot_size = 50
            elif num_trials <= 500:
                dot_size = 25
            elif num_trials <= 1000:
                dot_size = 15
            else:
                dot_size = 10
            
            st.caption(f"Plot info: Max frequency = {max_count}, Dot size = {dot_size}")
        
        with stats_col:
            st.subheader("Detailed Statistics")
            
            # Create detailed statistics table
            stats_data = []
            for face in range(1, 7):
                count = results.count(face)
                percentage = (count / num_trials) * 100
                expected_pct = 16.67
                deviation = percentage - expected_pct
                stats_data.append({
                    "Face": f"⚀⚁⚂⚃⚄⚅"[face-1],
                    "Count": count,
                    "Percentage": f"{percentage:.1f}%",
                    "Deviation": f"{deviation:+.1f}%"
                })
            
            # Display as dataframe
            import pandas as pd
            df = pd.DataFrame(stats_data)
            st.dataframe(df, use_container_width=True, hide_index=True)
            
            # Additional insights
            st.markdown("**📈 Insights:**")
            total_deviation = sum(abs(results.count(i)/num_trials - 1/6) for i in range(1, 7))
            if total_deviation < 0.1:
                st.success("🎯 Very close to expected distribution!")
            elif total_deviation < 0.2:
                st.info("📊 Reasonably close to expected distribution")
            else:
                st.warning("📉 Some deviation from expected - try more trials!")
    
    # Footer
    st.markdown("---")
    st.markdown(
        """
        <div style='text-align: center; color: gray;'>
        Built with Streamlit 🚀 | Simulating probability and statistics
        </div>
        """, 
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
