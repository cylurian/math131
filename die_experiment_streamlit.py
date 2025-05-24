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
    
    # Create the plot
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # For each die face, plot dots vertically
    for face, count in counts.items():
        if count > 0:
            # Create y-coordinates for dots (stacked vertically)
            y_coords = np.arange(1, count + 1)
            # Create x-coordinates (all at the same face value)
            x_coords = [face] * count
            
            # Plot dots
            ax.scatter(x_coords, y_coords, s=50, alpha=0.7, color='blue')
    
    # Customize the plot
    ax.set_xlabel('Die Face', fontsize=12, fontweight='bold')
    ax.set_ylabel('Frequency', fontsize=12, fontweight='bold')
    ax.set_title('Dot Plot of Die Roll Results', fontsize=14, fontweight='bold')
    
    # Set x-axis to show all die faces
    ax.set_xlim(0.5, 6.5)
    ax.set_xticks(range(1, 7))
    
    # Set y-axis to start from 0
    max_count = max(counts.values()) if any(counts.values()) else 1
    ax.set_ylim(0, max_count + 1)
    ax.set_yticks(range(0, max_count + 2))
    
    # Add grid for better readability
    ax.grid(True, alpha=0.3)
    
    # Remove top and right spines for cleaner look
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    plt.tight_layout()
    return fig

def main():
    """Main Streamlit app"""
    st.set_page_config(
        page_title="Die Rolling Simulation",
        page_icon="🎲",
        layout="wide"
    )
    
    st.title("🎲 Die Rolling Simulation")
    st.markdown("---")
    
    # Sidebar for input
    st.sidebar.header("Simulation Settings")
    num_trials = st.sidebar.number_input(
        "How many times would you like to roll the die?",
        min_value=1,
        max_value=10000,
        value=100,
        step=1
    )
    
    # Button to run simulation
    if st.sidebar.button("Roll the Dice!", type="primary"):
        # Store results in session state
        st.session_state.results = []
        st.session_state.num_trials = num_trials
        
        # Create progress bar
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        # Perform the trials
        for i in range(num_trials):
            roll = roll_die()
            st.session_state.results.append(roll)
            
            # Update progress bar
            progress = (i + 1) / num_trials
            progress_bar.progress(progress)
            status_text.text(f"Rolling... {i + 1}/{num_trials}")
        
        # Clear progress indicators
        progress_bar.empty()
        status_text.empty()
        
        st.success(f"✅ Completed {num_trials} rolls!")
    
    # Display results if they exist
    if hasattr(st.session_state, 'results') and st.session_state.results:
        results = st.session_state.results
        num_trials = st.session_state.num_trials
        
        # Create two columns for layout
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.subheader("Dot Plot")
            fig = create_dot_plot(results)
            st.pyplot(fig)
        
        with col2:
            st.subheader("Results Summary")
            
            # Create summary table
            summary_data = []
            for face in range(1, 7):
                count = results.count(face)
                percentage = (count / num_trials) * 100
                summary_data.append({
                    "Die Face": f"⚀⚁⚂⚃⚄⚅"[face-1],
                    "Count": count,
                    "Percentage": f"{percentage:.1f}%"
                })
            
            st.table(summary_data)
            
            # Additional statistics
            st.subheader("Statistics")
            mean_roll = np.mean(results)
            median_roll = np.median(results)
            mode_roll = max(set(results), key=results.count)
            
            st.metric("Mean Roll", f"{mean_roll:.2f}")
            st.metric("Median Roll", f"{median_roll:.1f}")
            st.metric("Mode Roll", f"{mode_roll}")
        
        # Raw data section (collapsible)
        with st.expander("View Raw Data"):
            st.write("All roll results:")
            # Display results in a more readable format
            rolls_per_row = 20
            for i in range(0, len(results), rolls_per_row):
                row_results = results[i:i + rolls_per_row]
                st.write(" ".join(map(str, row_results)))
        
        # Download option
        st.subheader("Download Results")
        results_text = "\n".join([
            f"Die Rolling Simulation Results",
            f"Number of trials: {num_trials}",
            f"Date: {st.session_state.get('timestamp', 'N/A')}",
            "",
            "Summary:",
        ] + [
            f"Face {face}: {results.count(face)} times "
            f"({(results.count(face) / num_trials) * 100:.1f}%)"
            for face in range(1, 7)
        ] + [
            "",
            "Raw data:",
            " ".join(map(str, results))
        ])
        
        st.download_button(
            label="Download Results as Text File",
            data=results_text,
            file_name=f"die_rolls_{num_trials}_trials.txt",
            mime="text/plain"
        )
    
    else:
        # Initial state - show instructions
        st.info("👈 Set the number of trials in the sidebar and click 'Roll the Dice!' to begin the simulation.")
        
        # Show example
        st.subheader("Example")
        st.write("This app will:")
        st.write("- Simulate rolling a 6-sided die for your specified number of trials")
        st.write("- Create a dot plot showing the frequency of each outcome")
        st.write("- Provide summary statistics and raw data")
        st.write("- Allow you to download the results")

if __name__ == "__main__":
    main()
