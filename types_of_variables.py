{\rtf1\ansi\ansicpg1252\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import random
import streamlit as st\
\
# ----- Embedded Data Dictionaries -----\
\
nominal = \{\
    "Favorite color": [\
        "Red", "Blue", "Green", "Yellow", "Purple",\
        "Orange", "Pink", "Brown", "Black", "White"\
    ],\
    "Type of pet": [\
        "Dog", "Cat", "Fish", "Bird", "Hamster",\
        "Rabbit", "Lizard", "Turtle", "Snake", "Guinea Pig"\
    ],\
    "Country of origin": [\
        "USA", "Canada", "Mexico", "UK", "India",\
        "China", "Brazil", "Australia", "Germany", "Japan"\
    ],\
    "Blood type": [\
        "A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-", "A", "B"\
    ],\
    "Car brand": [\
        "Toyota", "Ford", "BMW", "Honda", "Tesla",\
        "Chevrolet", "Nissan", "Volkswagen", "Hyundai", "Kia"\
    ],\
    "Fruit preference": [\
        "Apple", "Banana", "Orange", "Grape", "Mango",\
        "Pineapple", "Strawberry", "Watermelon", "Peach", "Cherry"\
    ],\
    "Marital status": [\
        "Single", "Married", "Divorced", "Widowed", "Separated",\
        "In a relationship", "Engaged", "Domestic partnership", "Annulled", "It's complicated"\
    ],\
    "Eye color": [\
        "Brown", "Blue", "Green", "Hazel", "Gray",\
        "Amber", "Black", "Violet", "Red", "Heterochromia"\
    ],\
    "Music genre": [\
        "Rock", "Pop", "Jazz", "Classical", "Hip-Hop",\
        "Country", "Electronic", "Reggae", "Blues", "Metal"\
    ],\
    "Language spoken": [\
        "English", "Spanish", "French", "German", "Chinese",\
        "Hindi", "Arabic", "Russian", "Portuguese", "Japanese"\
    ],\
    "Favorite sport": [\
        "Soccer", "Basketball", "Baseball", "Tennis", "Golf",\
        "Cricket", "Rugby", "Hockey", "Volleyball", "Swimming"\
    ],\
    "Ice cream flavor": [\
        "Vanilla", "Chocolate", "Strawberry", "Mint", "Cookie Dough",\
        "Pistachio", "Rocky Road", "Butter Pecan", "Mango", "Coffee"\
    ],\
    "Flower type": [\
        "Rose", "Tulip", "Lily", "Daisy", "Orchid",\
        "Sunflower", "Carnation", "Peony", "Iris", "Lavender"\
    ],\
    "Shoe brand": [\
        "Nike", "Adidas", "Puma", "Reebok", "Converse",\
        "Vans", "New Balance", "Skechers", "Asics", "Under Armour"\
    ],\
    "Beverage": [\
        "Water", "Coffee", "Tea", "Juice", "Soda",\
        "Milk", "Beer", "Wine", "Smoothie", "Energy Drink"\
    ],\
    "Dessert": [\
        "Cake", "Pie", "Ice Cream", "Brownie", "Cookie",\
        "Pudding", "Tart", "Mousse", "Cupcake", "Donut"\
    ],\
    "Animal": [\
        "Lion", "Tiger", "Bear", "Wolf", "Elephant",\
        "Giraffe", "Zebra", "Kangaroo", "Panda", "Leopard"\
    ],\
    "City": [\
        "New York", "London", "Paris", "Tokyo", "Sydney",\
        "Dubai", "Rome", "Berlin", "Toronto", "Moscow"\
    ],\
    "Season": [\
        "Spring", "Summer", "Autumn", "Winter", "Rainy",\
        "Dry", "Monsoon", "Pre-winter", "Pre-summer", "Harvest"\
    ],\
    "Superhero": [\
        "Superman", "Batman", "Wonder Woman", "Spider-Man", "Iron Man",\
        "Captain America", "Hulk", "Thor", "Black Panther", "Flash"\
    ],\
    "Board game": [\
        "Chess", "Monopoly", "Scrabble", "Clue", "Risk",\
        "Catan", "Checkers", "Uno", "Battleship", "Life"\
    ],\
    "Pizza topping": [\
        "Pepperoni", "Mushroom", "Onion", "Sausage", "Bacon",\
        "Extra cheese", "Black olives", "Green pepper", "Pineapple", "Spinach"\
    ],\
    "Sandwich type": [\
        "Ham", "Turkey", "Chicken", "Tuna", "Egg",\
        "Veggie", "BLT", "Grilled Cheese", "Meatball", "Club"\
    ],\
    "Clothing style": [\
        "Casual", "Formal", "Sporty", "Bohemian", "Vintage",\
        "Chic", "Preppy", "Punk", "Goth", "Business"\
    ],\
    "Holiday": [\
        "Christmas", "Easter", "Halloween", "Thanksgiving", "New Year",\
        "Hanukkah", "Diwali", "Ramadan", "Valentine's Day", "Independence Day"\
    ],\
    "Instrument": [\
        "Guitar", "Piano", "Violin", "Drums", "Flute",\
        "Saxophone", "Trumpet", "Cello", "Clarinet", "Harp"\
    ],\
    "TV genre": [\
        "Drama", "Comedy", "Thriller", "Action", "Documentary",\
        "Reality", "Fantasy", "Sci-Fi", "Mystery", "Animation"\
    ],\
    "Mobile brand": [\
        "Apple", "Samsung", "Huawei", "Xiaomi", "Oppo",\
        "Vivo", "OnePlus", "Motorola", "Nokia", "Sony"\
    ],\
    "Social media platform": [\
        "Facebook", "Instagram", "Twitter", "Snapchat", "TikTok",\
        "LinkedIn", "Reddit", "Pinterest", "YouTube", "WhatsApp"\
    ],\
    "Programming language": [\
        "Python", "Java", "C++", "JavaScript", "Ruby",\
        "Go", "Swift", "Kotlin", "PHP", "C#"\
    ],\
    "Operating system": [\
        "Windows", "macOS", "Linux", "Android", "iOS",\
        "Ubuntu", "Fedora", "Debian", "Red Hat", "Chrome OS"\
    ],\
    "Browser": [\
        "Chrome", "Firefox", "Safari", "Edge", "Opera",\
        "Brave", "Vivaldi", "Internet Explorer", "Tor", "UC Browser"\
    ],\
    "Continent": [\
        "Africa", "Asia", "Europe", "North America", "South America",\
        "Australia", "Antarctica", "Eurasia", "Oceania", "Central America"\
    ],\
    "Currency": [\
        "Dollar", "Euro", "Yen", "Pound", "Rupee",\
        "Won", "Franc", "Peso", "Lira", "Ruble"\
    ],\
    "Planet": [\
        "Mercury", "Venus", "Earth", "Mars", "Jupiter",\
        "Saturn", "Uranus", "Neptune", "Pluto", "Ceres"\
    ],\
    "Dog breed": [\
        "Labrador", "Poodle", "Bulldog", "Beagle", "Chihuahua",\
        "Dachshund", "Boxer", "Shih Tzu", "Pug", "Rottweiler"\
    ],\
    "Cat breed": [\
        "Siamese", "Persian", "Maine Coon", "Ragdoll", "Bengal",\
        "Sphynx", "British Shorthair", "Abyssinian", "Birman", "Russian Blue"\
    ],\
    "Bird species": [\
        "Parrot", "Sparrow", "Eagle", "Owl", "Penguin",\
        "Flamingo", "Peacock", "Canary", "Crow", "Swan"\
    ],\
    "Tree type": [\
        "Oak", "Maple", "Pine", "Birch", "Willow",\
        "Cedar", "Redwood", "Palm", "Spruce", "Cherry"\
    ],\
    "Seafood": [\
        "Shrimp", "Crab", "Lobster", "Salmon", "Tuna",\
        "Oyster", "Clam", "Mussel", "Scallop", "Squid"\
    ],\
    "Cheese type": [\
        "Cheddar", "Mozzarella", "Swiss", "Brie", "Gouda",\
        "Parmesan", "Feta", "Blue", "Goat", "Provolone"\
    ],\
    "Snack": [\
        "Chips", "Popcorn", "Pretzels", "Nuts", "Granola Bar",\
        "Fruit Snack", "Crackers", "Cookies", "Jerky", "Trail Mix"\
    ],\
    "Pastry": [\
        "Croissant", "Danish", "Eclair", "Macaron", "Baklava",\
        "Strudel", "Tart", "Turnover", "Profiterole", "Scone"\
    ],\
    "Soup": [\
        "Chicken Noodle", "Tomato", "Minestrone", "Clam Chowder", "Lentil",\
        "Pumpkin", "Broccoli Cheddar", "French Onion", "Miso", "Gazpacho"\
    ],\
    "Salad": [\
        "Caesar", "Greek", "Cobb", "Waldorf", "Caprese",\
        "Pasta", "Potato", "Fruit", "Tuna", "Chicken"\
    ],\
    "Breakfast food": [\
        "Pancakes", "Waffles", "Omelette", "Cereal", "Toast",\
        "Bagel", "Muffin", "Yogurt", "Smoothie Bowl", "Granola"\
    ],\
    "Fast food chain": [\
        "McDonald's", "Burger King", "KFC", "Subway", "Wendy's",\
        "Taco Bell", "Domino's", "Pizza Hut", "Chick-fil-A", "Dunkin'"\
    ],\
\}\
\
ordinal = \{\
    "Education level": [\
        "No Schooling", "Elementary", "Middle School", "High School", "Associate",\
        "Bachelor", "Master", "Professional", "Doctorate", "Post-Doctorate"\
    ],\
    "Customer satisfaction": [\
        "Extremely Unsatisfied", "Very Unsatisfied", "Unsatisfied", "Somewhat Unsatisfied", "Neutral",\
        "Somewhat Satisfied", "Satisfied", "Very Satisfied", "Extremely Satisfied", "No Opinion"\
    ],\
    "T-shirt size": [\
        "XXS", "XS", "S", "M", "L",\
        "XL", "XXL", "3XL", "4XL", "5XL"\
    ],\
    "Spiciness level": [\
        "Not Spicy", "Mild", "Medium", "Medium-Hot", "Hot",\
        "Very Hot", "Extra Hot", "Super Hot", "Extreme", "Nuclear"\
    ],\
    "Movie rating": [\
        "0 stars", "0.5 stars", "1 star", "2 stars", "3 stars",\
        "3.5 stars", "4 stars", "4.5 stars", "5 stars", "Unrated"\
    ],\
    "Agreement level": [\
        "Strongly Disagree", "Disagree", "Somewhat Disagree", "Neutral", "Somewhat Agree",\
        "Agree", "Strongly Agree", "No Opinion", "Refused", "Not Applicable"\
    ],\
    "Job position": [\
        "Intern", "Trainee", "Junior", "Mid", "Senior",\
        "Lead", "Supervisor", "Manager", "Director", "Executive"\
    ],\
    "Pain severity": [\
        "None", "Very Mild", "Mild", "Moderate", "Somewhat Severe",\
        "Severe", "Very Severe", "Extreme", "Unbearable", "Worst Possible"\
    ],\
    "Priority level": [\
        "Very Low", "Low", "Below Normal", "Normal", "Above Normal",\
        "High", "Very High", "Urgent", "Critical", "Immediate"\
    ],\
    "Class rank": [\
        "Freshman", "Sophomore", "Junior", "Senior", "5th Year",\
        "Graduate", "Postgraduate", "Doctoral", "Alumni", "Exchange"\
    ],\
    "Fitness level": [\
        "Very Poor", "Poor", "Below Average", "Average", "Above Average",\
        "Good", "Very Good", "Excellent", "Elite", "World Class"\
    ],\
    "Sleep quality": [\
        "Very Poor", "Poor", "Fair", "Average", "Good",\
        "Very Good", "Excellent", "Outstanding", "Perfect", "Unmeasured"\
    ],\
    "Stress level": [\
        "None", "Very Low", "Low", "Moderate", "High",\
        "Very High", "Extreme", "Overwhelmed", "Burnout", "Unknown"\
    ],\
    "Happiness level": [\
        "Very Unhappy", "Unhappy", "Somewhat Unhappy", "Neutral", "Somewhat Happy",\
        "Happy", "Very Happy", "Ecstatic", "Euphoric", "No Response"\
    ],\
    "Risk level": [\
        "No Risk", "Very Low", "Low", "Moderate", "High",\
        "Very High", "Severe", "Critical", "Extreme", "Unknown"\
    ],\
    "Health status": [\
        "Critical", "Very Poor", "Poor", "Fair", "Good",\
        "Very Good", "Excellent", "Recovered", "Remission", "Cured"\
    ],\
    "Income bracket": [\
        "Very Low", "Low", "Lower-Middle", "Middle", "Upper-Middle",\
        "High", "Very High", "Affluent", "Wealthy", "Ultra Wealthy"\
    ],\
    "Credit rating": [\
        "Very Poor", "Poor", "Fair", "Average", "Good",\
        "Very Good", "Excellent", "Prime", "Super Prime", "Exceptional"\
    ],\
    "Performance rating": [\
        "Unsatisfactory", "Needs Improvement", "Fair", "Meets Expectations", "Good",\
        "Very Good", "Excellent", "Outstanding", "Exceptional", "Legendary"\
    ],\
    "Seniority level": [\
        "Entry", "Junior", "Associate", "Mid", "Senior",\
        "Lead", "Principal", "Director", "VP", "C-level"\
    ],\
    "Reading proficiency": [\
        "Non-reader", "Beginner", "Basic", "Intermediate", "Proficient",\
        "Advanced", "Expert", "Master", "Scholar", "Savant"\
    ],\
    "Writing proficiency": [\
        "Non-writer", "Beginner", "Basic", "Intermediate", "Proficient",\
        "Advanced", "Expert", "Master", "Scholar", "Savant"\
    ],\
    "Math proficiency": [\
        "Non-mathematician", "Beginner", "Basic", "Intermediate", "Proficient",\
        "Advanced", "Expert", "Master", "Scholar", "Savant"\
    ],\
    "Language proficiency": [\
        "None", "Beginner", "Elementary", "Intermediate", "Upper Intermediate",\
        "Advanced", "Proficient", "Fluent", "Native", "Bilingual"\
    ],\
    "Driving skill": [\
        "Non-driver", "Beginner", "Novice", "Intermediate", "Competent",\
        "Proficient", "Advanced", "Expert", "Master", "Racing Pro"\
    ],\
    "Cooking skill": [\
        "Non-cook", "Beginner", "Novice", "Intermediate", "Competent",\
        "Proficient", "Advanced", "Expert", "Chef", "Master Chef"\
    ],\
    "Swimming skill": [\
        "Non-swimmer", "Beginner", "Novice", "Intermediate", "Competent",\
        "Proficient", "Advanced", "Expert", "Lifeguard", "Olympian"\
    ],\
    "Language test score": [\
        "A1", "A2", "B1", "B2", "C1",\
        "C2", "Native", "Fluent", "Proficient", "Bilingual"\
    ],\
    "Project phase": [\
        "Initiation", "Planning", "Design", "Development", "Testing",\
        "Deployment", "Maintenance", "Review", "Closure", "Archived"\
    ],\
    "Weather severity": [\
        "None", "Very Mild", "Mild", "Moderate", "Severe",\
        "Very Severe", "Extreme", "Disaster", "Catastrophic", "Unknown"\
    ],\
    "Earthquake intensity": [\
        "Not Felt", "Weak", "Light", "Moderate", "Strong",\
        "Very Strong", "Severe", "Violent", "Extreme", "Catastrophic"\
    ],\
    "Hurricane category": [\
        "Tropical Depression", "Tropical Storm", "Category 1", "Category 2", "Category 3",\
        "Category 4", "Category 5", "Super Typhoon", "Mega Cyclone", "Hypercane"\
    ],\
    "Flood risk": [\
        "None", "Very Low", "Low", "Moderate", "High",\
        "Very High", "Severe", "Critical", "Extreme", "Unknown"\
    ],\
    "Fire danger": [\
        "No Danger", "Low", "Moderate", "High", "Very High",\
        "Severe", "Extreme", "Catastrophic", "Disaster", "Unknown"\
    ],\
    "Air quality": [\
        "Excellent", "Good", "Moderate", "Poor", "Very Poor",\
        "Unhealthy", "Very Unhealthy", "Hazardous", "Toxic", "Deadly"\
    ],\
    "Noise level": [\
        "Silent", "Very Quiet", "Quiet", "Moderate", "Loud",\
        "Very Loud", "Extremely Loud", "Deafening", "Painful", "Unmeasured"\
    ],\
    "Light intensity": [\
        "Pitch Dark", "Very Dim", "Dim", "Moderate", "Bright",\
        "Very Bright", "Blinding", "Dazzling", "Extreme", "Unmeasured"\
    ],\
    "Battery level": [\
        "Empty", "Critical", "Low", "Medium", "High",\
        "Very High", "Full", "Overcharged", "Supercharged", "Infinite"\
    ],\
    "Signal strength": [\
        "No Signal", "Very Weak", "Weak", "Moderate", "Good",\
        "Very Good", "Excellent", "Full", "Max", "Infinite"\
    ],\
    "Internet speed": [\
        "No Connection", "Very Slow", "Slow", "Moderate", "Fast",\
        "Very Fast", "Super Fast", "Ultra Fast", "Lightning", "Quantum"\
    ],\
    "Game level": [\
        "Tutorial", "Easy", "Normal", "Hard", "Very Hard",\
        "Expert", "Master", "Legendary", "Mythic", "Impossible"\
    ],\
    "Ranking": [\
        "Bronze", "Silver", "Gold", "Platinum", "Diamond",\
        "Master", "Grandmaster", "Challenger", "Legend", "Immortal"\
    ],\
    "Medal": [\
        "Participant", "Honorable Mention", "Bronze", "Silver", "Gold",\
        "Platinum", "Diamond", "Champion", "Grand Champion", "Legend"\
    ],\
\}\
\
continuous = \{\
    "Height of students (cm)": [round(random.uniform(140, 200), 2) for _ in range(10)],\
    "Weight of adults (kg)": [round(random.uniform(50, 120), 2) for _ in range(10)],\
    "Temperature in a city (\'b0C)": [round(random.uniform(-10, 40), 2) for _ in range(10)],\
    "Length of fish (cm)": [round(random.uniform(2, 100), 2) for _ in range(10)],\
    "Time to run 100m (seconds)": [round(random.uniform(9.5, 20), 2) for _ in range(10)],\
    "Amount of rainfall (mm)": [round(random.uniform(0, 200), 2) for _ in range(10)],\
    "Speed of a car (km/h)": [round(random.uniform(0, 200), 2) for _ in range(10)],\
    "Blood pressure (mmHg)": [round(random.uniform(80, 180), 2) for _ in range(10)],\
    "Body temperature (\'b0C)": [round(random.uniform(35, 42), 2) for _ in range(10)],\
    "Length of pencils (cm)": [round(random.uniform(5, 20), 2) for _ in range(10)],\
    "Volume of water in a glass (ml)": [round(random.uniform(100, 500), 2) for _ in range(10)],\
    "Distance to school (km)": [round(random.uniform(0.1, 20), 2) for _ in range(10)],\
    "Age of trees (years)": [round(random.uniform(1, 100), 2) for _ in range(10)],\
    "Diameter of coins (mm)": [round(random.uniform(15, 40), 2) for _ in range(10)],\
    "Width of a desk (cm)": [round(random.uniform(40, 120), 2) for _ in range(10)],\
    "Depth of a lake (m)": [round(random.uniform(1, 300), 2) for _ in range(10)],\
    "Price of a meal ($)": [round(random.uniform(3, 50), 2) for _ in range(10)],\
    "Length of a movie (minutes)": [round(random.uniform(60, 210), 2) for _ in range(10)],\
    "Concentration of salt (g/L)": [round(random.uniform(0, 100), 2) for _ in range(10)],\
    "Height of buildings (m)": [round(random.uniform(3, 300), 2) for _ in range(10)],\
    "Weight of newborns (kg)": [round(random.uniform(2, 5), 2) for _ in range(10)],\
    "Time spent on homework (hours)": [round(random.uniform(0.1, 5), 2) for _ in range(10)],\
    "Length of cables (m)": [round(random.uniform(0.5, 100), 2) for _ in range(10)],\
    "Depth of snow (cm)": [round(random.uniform(0, 200), 2) for _ in range(10)],\
    "Volume of a balloon (L)": [round(random.uniform(0.1, 10), 2) for _ in range(10)],\
    "Speed of wind (m/s)": [round(random.uniform(0, 40), 2) for _ in range(10)],\
    "Amount of sugar in a drink (g)": [round(random.uniform(0, 60), 2) for _ in range(10)],\
    "Length of a river (km)": [round(random.uniform(10, 7000), 2) for _ in range(10)],\
    "Time to cook pasta (minutes)": [round(random.uniform(5, 20), 2) for _ in range(10)],\
    "Diameter of a pizza (cm)": [round(random.uniform(20, 50), 2) for _ in range(10)],\
    "Height of mountains (m)": [round(random.uniform(100, 9000), 2) for _ in range(10)],\
    "Weight of luggage (kg)": [round(random.uniform(1, 32), 2) for _ in range(10)],\
    "Time to charge a phone (hours)": [round(random.uniform(0.5, 4), 2) for _ in range(10)],\
    "Width of a road (m)": [round(random.uniform(2, 50), 2) for _ in range(10)],\
    "Depth of a swimming pool (m)": [round(random.uniform(1, 5), 2) for _ in range(10)],\
    "Price of gasoline ($/L)": [round(random.uniform(0.8, 2.5), 2) for _ in range(10)],\
    "Length of a song (minutes)": [round(random.uniform(1.5, 7), 2) for _ in range(10)],\
    "Temperature of coffee (\'b0C)": [round(random.uniform(40, 95), 2) for _ in range(10)],\
    "Weight of a cat (kg)": [round(random.uniform(2, 10), 2) for _ in range(10)],\
    "Time to solve a puzzle (minutes)": [round(random.uniform(1, 120), 2) for _ in range(10)],\
\}\
\
discrete = \{\
    "Students in a classroom": [random.randint(15, 35) for _ in range(10)],\
    "Cars in a parking lot": [random.randint(0, 50) for _ in range(10)],\
    "Books on a shelf": [random.randint(5, 40) for _ in range(10)],\
    "Pets in a household": [random.randint(0, 6) for _ in range(10)],\
    "Chairs in a room": [random.randint(1, 20) for _ in range(10)],\
    "Siblings a person has": [random.randint(0, 5) for _ in range(10)],\
    "Houses on a street": [random.randint(5, 50) for _ in range(10)],\
    "Employees in a company": [random.randint(1, 100) for _ in range(10)],\
    "Tickets sold for a concert": [random.randint(50, 500) for _ in range(10)],\
    "Goals scored in a soccer match": [random.randint(0, 10) for _ in range(10)],\
    "Computers in a lab": [random.randint(5, 40) for _ in range(10)],\
    "Apples in a basket": [random.randint(1, 30) for _ in range(10)],\
    "Flights departing from an airport": [random.randint(5, 100) for _ in range(10)],\
    "Questions on a test": [random.randint(5, 50) for _ in range(10)],\
    "Light bulbs in a building": [random.randint(10, 200) for _ in range(10)],\
    "Coins in a jar": [random.randint(1, 100) for _ in range(10)],\
    "Phone calls received in a day": [random.randint(0, 30) for _ in range(10)],\
    "Steps in a staircase": [random.randint(5, 30) for _ in range(10)],\
    "Votes in an election": [random.randint(100, 10000) for _ in range(10)],\
    "Pages in a book": [random.randint(50, 800) for _ in range(10)],\
    "Floors in a building": [random.randint(1, 100) for _ in range(10)],\
    "Shoes in a closet": [random.randint(1, 50) for _ in range(10)],\
    "Patients in a hospital ward": [random.randint(1, 40) for _ in range(10)],\
    "Parking spaces in a lot": [random.randint(5, 200) for _ in range(10)],\
    "Candies in a bag": [random.randint(5, 100) for _ in range(10)],\
    "Windows in a house": [random.randint(1, 30) for _ in range(10)],\
    "Trees in a park": [random.randint(5, 200) for _ in range(10)],\
    "Emails received per day": [random.randint(0, 100) for _ in range(10)],\
    "Questions answered correctly": [random.randint(0, 50) for _ in range(10)],\
    "Buses in a fleet": [random.randint(1, 100) for _ in range(10)],\
    "Pencils in a box": [random.randint(5, 50) for _ in range(10)],\
    "Fish in an aquarium": [random.randint(1, 40) for _ in range(10)],\
    "Matches in a box": [random.randint(20, 100) for _ in range(10)],\
    "Children in a family": [random.randint(0, 8) for _ in range(10)],\
    "Tables in a restaurant": [random.randint(5, 50) for _ in range(10)],\
    "Lockers in a gym": [random.randint(10, 200) for _ in range(10)],\
    "Awards won by a team": [random.randint(0, 20) for _ in range(10)],\
    "Visitors to a museum": [random.randint(10, 1000) for _ in range(10)],\
    "Errors in a document": [random.randint(0, 20) for _ in range(10)],\
    "Movies watched in a month": [random.randint(0, 30) for _ in range(10)],\
\}\
\
type_dicts = [\
    ("nominal", nominal),\
    ("ordinal", ordinal),\
    ("discrete", discrete),\
    ("continuous", continuous),\
]\
\
def choose_and_sample(dictionary):\
    category = random.choice(list(dictionary.keys()))\
    data_points = dictionary[category]\
    if len(data_points) >= 5:\
        sampled_points = random.sample(data_points, 5)\
    else:\
        sampled_points = random.choices(data_points, k=5)\
    return category, sampled_points\
\
def format_values(values):\
    return ', '.join(str(x) for x in values)\
\
def main():\
    st.write("Identify what type of variable each data set is below.")  \
    st.write()  \
\
    # Always one of each type first\
    used = []\
    for name, dictionary in type_dicts:\
        category, values = choose_and_sample(dictionary)\
        used.append((name, category, values))\
\
    # For the three random extras, allow any type (including repeats)\
    all_dicts = [\
        ("nominal", nominal),\
        ("ordinal", ordinal),\
        ("discrete", discrete),\
        ("continuous", continuous),\
    ]\
    extra = []\
    for _ in range(3):\
        name, dictionary = random.choice(all_dicts)\
        category, values = choose_and_sample(dictionary)\
        extra.append((name, category, values))\
\
    # Combine and shuffle for randomness\
    total = used + extra\
    random.shuffle(total)\
\
    # Output data sets\
    for name, category, values in total:\
        st.write(f"\{category\}")  \
        st.write(f"\{format_values(values)\}")  \
        st.write()  \
\
    # Output answer key\
    st.write("Answer Key:")  \
    for idx, (name, category, _) in enumerate(total, 1):\
        st.write(f"\{category\}: \{name\}")  \
\
if __name__ == "__main__":\
    main()\
}