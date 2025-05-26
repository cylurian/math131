import streamlit as st
import random
from datetime import datetime

# Set page config
st.set_page_config(
    page_title="Variable Type Identification Practice",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 1rem;
        font-weight: bold;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #ff7f0e;
        margin-top: 2rem;
        margin-bottom: 1rem;
        font-weight: bold;
    }
    .question-box {
        background-color: #f0f2f6;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #1f77b4;
        margin: 1rem 0;
    }
    .answer-box {
        background-color: #e8f5e8;
        padding: 1rem;
        border-radius: 10px;
        border-left: 5px solid #2ca02c;
        margin: 0.5rem 0;
    }
    .context-text {
        font-style: italic;
        color: #666;
        margin-bottom: 1rem;
    }
    .variable-type {
        font-weight: bold;
        font-size: 1.1rem;
    }
    .explanation {
        color: #666;
        font-size: 0.9rem;
        margin-top: 0.5rem;
    }
    .tip-box {
        background-color: #fff3cd;
        padding: 1rem;
        border-radius: 10px;
        border-left: 5px solid #ffc107;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# ----- Data Dictionaries -----
nominal = {
    "Favorite color": {
        "values": [
            "Red", "Blue", "Green", "Yellow", "Purple",
            "Orange", "Pink", "Brown", "Black", "White"
        ],
        "context": "A survey asked 100 people about their favorite color, and the responses were recorded as follows:"
    },
    "Type of pet": {
        "values": [
            "Dog", "Cat", "Fish", "Bird", "Hamster",
            "Rabbit", "Lizard", "Turtle", "Snake", "Guinea Pig"
        ],
        "context": "Pet owners at a veterinary clinic were asked what type of pet they own, with these responses:"
    },
    "Country of origin": {
        "values": [
            "USA", "Canada", "Mexico", "UK", "India",
            "China", "Brazil", "Australia", "Germany", "Japan"
        ],
        "context": "International students at a university were asked about their country of origin:"
    },
    "Blood type": {
        "values": [
            "A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-", "A", "B"
        ],
        "context": "Blood donors at a medical center had their blood types recorded as:"
    },
    "Car brand": {
        "values": [
            "Toyota", "Ford", "BMW", "Honda", "Tesla",
            "Chevrolet", "Nissan", "Volkswagen", "Hyundai", "Kia"
        ],
        "context": "Car owners in a parking garage were surveyed about their vehicle brand:"
    },
    "Hair color": {
        "values": [
            "Black", "Brown", "Blonde", "Red", "Gray",
            "White", "Auburn", "Chestnut", "Platinum", "Silver"
        ],
        "context": "Salon clients were categorized by their natural hair color:"
    },
    "Nationality": {
        "values": [
            "American", "Canadian", "British", "French", "German",
            "Italian", "Spanish", "Australian", "Japanese", "Korean"
        ],
        "context": "Passport holders at an airport were classified by nationality:"
    },
    "Occupation": {
        "values": [
            "Teacher", "Doctor", "Engineer", "Lawyer", "Artist",
            "Chef", "Nurse", "Accountant", "Programmer", "Designer"
        ],
        "context": "Job fair attendees listed their current occupation:"
    },
    "College major": {
        "values": [
            "Computer Science", "Biology", "Psychology", "Business", "English",
            "Mathematics", "History", "Art", "Chemistry", "Physics"
        ],
        "context": "University students declared these academic majors:"
    },
    "Gaming console": {
        "values": [
            "PlayStation", "Xbox", "Nintendo Switch", "PC", "Steam Deck",
            "Atari", "Sega", "Game Boy", "PSP", "Mobile"
        ],
        "context": "Gamers at a convention indicated their preferred gaming platform:"
    }
}

ordinal = {
    "Education level": {
        "values": [
            "No Schooling", "Elementary", "Middle School", "High School", "Associate",
            "Bachelor", "Master", "Professional", "Doctorate", "Post-Doctorate"
        ],
        "context": "Job applicants reported their highest level of education completed:"
    },
    "Customer satisfaction": {
        "values": [
            "Extremely Unsatisfied", "Very Unsatisfied", "Unsatisfied", "Somewhat Unsatisfied", "Neutral",
            "Somewhat Satisfied", "Satisfied", "Very Satisfied", "Extremely Satisfied", "No Opinion"
        ],
        "context": "Hotel guests rated their satisfaction with their stay:"
    },
    "T-shirt size": {
        "values": [
            "XXS", "XS", "S", "M", "L",
            "XL", "XXL", "3XL", "4XL", "5XL"
        ],
        "context": "Customers at a clothing store selected these t-shirt sizes:"
    },
    "Spiciness level": {
        "values": [
            "Not Spicy", "Mild", "Medium", "Medium-Hot", "Hot",
            "Very Hot", "Extra Hot", "Super Hot", "Extreme", "Nuclear"
        ],
        "context": "Restaurant diners chose these spiciness levels for their curry:"
    },
    "Movie rating": {
        "values": [
            "0 stars", "0.5 stars", "1 star", "2 stars", "3 stars",
            "3.5 stars", "4 stars", "4.5 stars", "5 stars", "Unrated"
        ],
        "context": "Film critics gave these star ratings to new movie releases:"
    },
    "Agreement level": {
        "values": [
            "Strongly Disagree", "Disagree", "Somewhat Disagree", "Neutral", "Somewhat Agree",
            "Agree", "Strongly Agree", "No Opinion", "Refused", "Not Applicable"
        ],
        "context": "Survey participants indicated their level of agreement with a policy statement:"
    },
    "Job position": {
        "values": [
            "Intern", "Trainee", "Junior", "Mid", "Senior",
            "Lead", "Supervisor", "Manager", "Director", "Executive"
        ],
        "context": "Employees at a tech company hold these job position levels:"
    },
    "Pain severity": {
        "values": [
            "None", "Very Mild", "Mild", "Moderate", "Somewhat Severe",
            "Severe", "Very Severe", "Extreme", "Unbearable", "Worst Possible"
        ],
        "context": "Patients at a medical clinic rated their pain severity as:"
    },
    "Difficulty level": {
        "values": [
            "Very Easy", "Easy", "Somewhat Easy", "Moderate", "Somewhat Hard",
            "Hard", "Very Hard", "Extremely Hard", "Nearly Impossible", "Impossible"
        ],
        "context": "Video game players rated the difficulty level of different game modes:"
    },
    "Quality rating": {
        "values": [
            "Terrible", "Poor", "Below Average", "Average", "Above Average",
            "Good", "Very Good", "Excellent", "Outstanding", "Perfect"
        ],
        "context": "Product reviewers gave these quality ratings to electronic devices:"
    }
}

continuous = {
    "Height of students (cm)": {
        "values": [round(random.uniform(140, 200), 2) for _ in range(10)],
        "context": "The heights of students in a high school class were measured in centimeters:"
    },
    "Weight of adults (kg)": {
        "values": [round(random.uniform(50, 120), 2) for _ in range(10)],
        "context": "Adults at a fitness center had their weights recorded in kilograms:"
    },
    "Temperature in a city (°C)": {
        "values": [round(random.uniform(-10, 40), 2) for _ in range(10)],
        "context": "Daily temperatures in a city were recorded in degrees Celsius over a week:"
    },
    "Time to run 100m (seconds)": {
        "values": [round(random.uniform(9.5, 20), 2) for _ in range(10)],
        "context": "Track athletes' times for running 100 meters were recorded in seconds:"
    },
    "Amount of rainfall (mm)": {
        "values": [round(random.uniform(0, 200), 2) for _ in range(10)],
        "context": "Monthly rainfall amounts were measured in millimeters across different regions:"
    },
    "Speed of a car (km/h)": {
        "values": [round(random.uniform(0, 200), 2) for _ in range(10)],
        "context": "Traffic cameras recorded vehicle speeds in kilometers per hour:"
    },
    "Blood pressure (mmHg)": {
        "values": [round(random.uniform(80, 180), 2) for _ in range(10)],
        "context": "Patients' systolic blood pressure readings were measured in mmHg:"
    },
    "Body temperature (°C)": {
        "values": [round(random.uniform(35, 42), 2) for _ in range(10)],
        "context": "Hospital patients had their body temperatures recorded in degrees Celsius:"
    },
    "Salary per year ($)": {
        "values": [round(random.uniform(25000, 150000), 2) for _ in range(10)],
        "context": "Employees at various companies reported their annual salaries in dollars:"
    },
    "Heart rate (bpm)": {
        "values": [round(random.uniform(60, 180), 2) for _ in range(10)],
        "context": "Fitness tracker users recorded their heart rates in beats per minute during exercise:"
    }
}

discrete = {
    "Students in a classroom": {
        "values": [random.randint(15, 35) for _ in range(10)],
        "context": "The number of students present in different classrooms was counted:"
    },
    "Cars in a parking lot": {
        "values": [random.randint(0, 50) for _ in range(10)],
        "context": "Security guards counted the number of cars in various parking lots:"
    },
    "Books on a shelf": {
        "values": [random.randint(5, 40) for _ in range(10)],
        "context": "Librarians counted the number of books on different shelves:"
    },
    "Pets in a household": {
        "values": [random.randint(0, 6) for _ in range(10)],
        "context": "Families were surveyed about the number of pets they own:"
    },
    "Siblings a person has": {
        "values": [random.randint(0, 5) for _ in range(10)],
        "context": "Survey participants reported the number of siblings they have:"
    },
    "Employees in a company": {
        "values": [random.randint(1, 100) for _ in range(10)],
        "context": "Small businesses reported the total number of employees they have:"
    },
    "Goals scored in a soccer match": {
        "values": [random.randint(0, 10) for _ in range(10)],
        "context": "Soccer teams recorded the total number of goals scored in their matches:"
    },
    "Apps on a smartphone": {
        "values": [random.randint(10, 200) for _ in range(10)],
        "context": "Smartphone users counted the number of apps installed on their devices:"
    },
    "Likes on a post": {
        "values": [random.randint(0, 1000) for _ in range(10)],
        "context": "Content creators tracked the number of likes their posts received:"
    },
    "Downloads of an app": {
        "values": [random.randint(100, 100000) for _ in range(10)],
        "context": "App developers monitored the number of downloads their apps received:"
    }
}

# Dictionary mapping for easy access
type_dicts = [
    ("Nominal", nominal),
    ("Ordinal", ordinal),
    ("Continuous", continuous),
    ("Discrete", discrete)
]

def choose_and_sample(dictionary):
    """Choose a random category and sample 5 data points from it."""
    category = random.choice(list(dictionary.keys()))
    data_info = dictionary[category]
    data_points = data_info["values"]
    context = data_info["context"]
    
    if len(data_points) >= 5:
        sampled_points = random.sample(data_points, 5)
    else:
        sampled_points = random.choices(data_points, k=5)
    return category, sampled_points, context

def generate_questions():
    """Generate a set of questions ensuring one from each type."""
    # Ensure we have one question from each type
    used = []
    for name, dictionary in type_dicts:
        category, sample, context = choose_and_sample(dictionary)
        used.append((category, sample, context, name))
    
    # Add 3 more random questions
    extra = []
    for _ in range(3):
        name, dictionary = random.choice(type_dicts)
        category, sample, context = choose_and_sample(dictionary)
        extra.append((category, sample, context, name))
    
    # Combine and limit to 7 questions
    total = used + extra
    total = total[:7]
    
    # Shuffle the order
    random.shuffle(total)
    
    return total

def main():
    # App title and description
    st.markdown('<h1 class="main-header">📊 Variable Type Identification Practice</h1>', unsafe_allow_html=True)
    
    # Sidebar with instructions
    with st.sidebar:
        st.markdown("## 📋 How to Use This App")
        st.markdown("""
        **Step 1:** Click "Generate New Questions" to create a practice set
        
        **Step 2:** Read each question carefully and identify the variable type
        
        **Step 3:** Make your selection from the dropdown menu
        
        **Step 4:** Click "Show Answers" to see the correct answers and explanations
        
        **Step 5:** Click "Generate New Questions" for more practice!
        """)
        
        st.markdown("---")
        
        st.markdown("## 🎯 Variable Types")
        st.markdown("""
        **NOMINAL** 📝
        - Categories with no natural order
        - Examples: Colors, names, brands
        
        **ORDINAL** 📊  
        - Categories with natural order
        - Examples: Ratings, sizes, grades
        
        **DISCRETE** 🔢
        - Countable whole numbers
        - Examples: Number of students, cars
        
        **CONTINUOUS** 📏
        - Measurable values with decimals
        - Examples: Height, weight, temperature
        """)
        
        st.markdown("---")
        
        st.markdown("## 💡 Tips")
        st.markdown("""
        - **Qualitative** = Nominal + Ordinal
        - **Quantitative** = Discrete + Continuous
        - Ask: "Can this be ordered?" (Ordinal vs Nominal)
        - Ask: "Can this be a fraction?" (Continuous vs Discrete)
        """)

    # Initialize session state
    if 'questions' not in st.session_state:
        st.session_state.questions = []
    if 'show_answers' not in st.session_state:
        st.session_state.show_answers = False
    if 'user_answers' not in st.session_state:
        st.session_state.user_answers = {}

    # Main content area
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        if st.button("🎲 Generate New Questions", type="primary", use_container_width=True):
            st.session_state.questions = generate_questions()
            st.session_state.show_answers = False
            st.session_state.user_answers = {}
            st.rerun()

    if st.session_state.questions:
        st.markdown('<h2 class="sub-header">📝 Practice Questions</h2>', unsafe_allow_html=True)
        
        # Display timestamp
        timestamp = datetime.now().strftime("%B %d, %Y at %I:%M %p")
        st.markdown(f"*Generated on: {timestamp}*")
        
        # Display questions
        for idx, (category, values, context, var_type) in enumerate(st.session_state.questions, 1):
            with st.container():
                st.markdown(f"""
                <div class="question-box">
                    <h3>Question {idx}</h3>
                    <p class="context-text">{context}</p>
                    <p><strong>Data Set:</strong> {category}</p>
                    <p><strong>Sample Values:</strong> {{{', '.join(map(str, values))}}}</p>
                </div>
                """, unsafe_allow_html=True)
                
                # User answer selection
                if not st.session_state.show_answers:
                    user_answer = st.selectbox(
                        f"Select the variable type for Question {idx}:",
                        ["Select an answer...", "Nominal", "Ordinal", "Discrete", "Continuous"],
                        key=f"q{idx}"
                    )
                    if user_answer != "Select an answer...":
                        st.session_state.user_answers[idx] = user_answer
                
                # Show answer if answers are revealed
                if st.session_state.show_answers:
                    explanations = {
                        "Nominal": "Categories with no natural order or ranking",
                        "Ordinal": "Categories with a natural order or ranking", 
                        "Discrete": "Countable whole numbers (can't be fractional)",
                        "Continuous": "Measurable values that can take any value within a range"
                    }
                    
                    user_answer = st.session_state.user_answers.get(idx, "Not answered")
                    is_correct = user_answer == var_type
                    
                    if is_correct:
                        st.success(f"✅ Correct! Your answer: {user_answer}")
                    else:
                        st.error(f"❌ Incorrect. Your answer: {user_answer}")
                    
                    st.markdown(f"""
                    <div class="answer-box">
                        <p class="variable-type">Correct Answer: {var_type.upper()}</p>
                        <p class="explanation">{explanations[var_type]}</p>
                    </div>
                    """, unsafe_allow_html=True)
                
                st.markdown("---")
        
        # Show answers button
        if not st.session_state.show_answers:
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                if st.button("🔍 Show Answers & Explanations", type="secondary", use_container_width=True):
                    st.session_state.show_answers = True
                    st.rerun()
        
        # Score calculation
        if st.session_state.show_answers and st.session_state.user_answers:
            correct_count = sum(1 for idx, (_, _, _, var_type) in enumerate(st.session_state.questions, 1) 
                              if st.session_state.user_answers.get(idx) == var_type)
            total_answered = len(st.session_state.user_answers)
            
            if total_answered > 0:
                score_percentage = (correct_count / total_answered) * 100
                st.markdown(f"""
                <div class="tip-box">
                    <h3>📊 Your Score: {correct_count}/{total_answered} ({score_percentage:.1f}%)</h3>
                    <p>Great job practicing! Click "Generate New Questions" to try more examples.</p>
                </div>
                """, unsafe_allow_html=True)

    else:
        st.markdown("""
        <div class="tip-box">
            <h3>👋 Welcome to Variable Type Identification Practice!</h3>
            <p>This app helps you practice identifying different types of variables in statistics.</p>
            <p><strong>Click "Generate New Questions" to get started!</strong></p>
        </div>
        """, unsafe_allow_html=True)

    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #666; font-size: 0.8rem;">
        📚 Educational Tool for Statistics Practice | 
        🔄 Generate new questions anytime | 
        💡 Perfect for students and educators
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
