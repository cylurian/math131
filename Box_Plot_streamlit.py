import random
import math
from textwrap import wrap
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter
import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Statistics Learning Tool",
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
        margin-bottom: 2rem;
    }
    .section-header {
        font-size: 1.5rem;
        color: #ff7f0e;
        margin-top: 2rem;
        margin-bottom: 1rem;
    }
    .stat-box {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #1f77b4;
        margin: 0.5rem 0;
    }
    .formula-box {
        background-color: #e8f4fd;
        padding: 1rem;
        border-radius: 0.5rem;
        border: 1px solid #1f77b4;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

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
    },
    {
        "title": "Daily Step Counts",
        "text": "A health app is tracking the number of steps users take each day. The developer wants to study user activity patterns.",
        "data_type": "discrete",
        "min_val": 800,
        "max_val": 20000,
        "decimals": 0
    },
    {
        "title": "Smartphone Screen Time",
        "text": "A digital wellness program records how many hours participants spend on their smartphones daily. The coordinator wants to monitor screen habits.",
        "data_type": "continuous",
        "min_val": 0.5,
        "max_val": 15.0,
        "decimals": 1
    },
    {
        "title": "Grocery Store Checkout Totals",
        "text": "A grocery store logs the total dollar amount spent by each customer during checkout. The manager wants to analyze purchase patterns.",
        "data_type": "continuous",
        "min_val": 3.50,
        "max_val": 350.75,
        "decimals": 2
    },
    {
        "title": "Children’s Heights",
        "text": "A pediatrician measures the heights of children visiting the clinic. The doctor wants to compare the growth rates by age group.",
        "data_type": "continuous",
        "min_val": 60.2,
        "max_val": 174.9,
        "decimals": 1
    },
    {
        "title": "Annual Car Mileage",
        "text": "A survey records the annual mileage driven by participants. The researcher wants to study travel habits.",
        "data_type": "continuous",
        "min_val": 1500,
        "max_val": 34000,
        "decimals": 0
    },
    {
        "title": "Coffee Temperature Preference",
        "text": "A coffee shop asks customers to select their preferred beverage temperature in degrees Fahrenheit. The shop owner wants to offer more precise options.",
        "data_type": "continuous",
        "min_val": 120,
        "max_val": 180,
        "decimals": 1
    },
    {
        "title": "Class Absences Per Semester",
        "text": "A college tracks the number of times students are absent each semester. The administration wants to identify attendance trends.",
        "data_type": "discrete",
        "min_val": 0,
        "max_val": 22,
        "decimals": 0
    },
    {
        "title": "Gallon Usage in Car Wash",
        "text": "A car wash facility records the gallons of water used per wash. The owner wants to monitor water efficiency.",
        "data_type": "continuous",
        "min_val": 15.0,
        "max_val": 68.2,
        "decimals": 1
    },
    {
        "title": "Hospital Wait Time (Minutes)",
        "text": "A hospital records the wait times in minutes for patients at the emergency room. Administrators want to reduce delays.",
        "data_type": "continuous",
        "min_val": 2,
        "max_val": 210,
        "decimals": 0
    },
    {
        "title": "Books Read Over Summer",
        "text": "A librarian records the number of books each child reads during a summer program. The goal is to promote reading.",
        "data_type": "discrete",
        "min_val": 1,
        "max_val": 45,
        "decimals": 0
    },
    {
        "title": "Dog Weight at Animal Shelter",
        "text": "An animal shelter keeps track of the weight of dogs admitted. The staff wants to monitor health trends.",
        "data_type": "continuous",
        "min_val": 3.2,
        "max_val": 89.7,
        "decimals": 1
    },
    {
        "title": "Online Purchase Delivery Time",
        "text": "An online store records the delivery time in days for each order. The logistics team wants to minimize delays.",
        "data_type": "continuous",
        "min_val": 1,
        "max_val": 18,
        "decimals": 0
    },
    {
        "title": "Gym Class Attendance",
        "text": "A fitness center tracks the number of participants in each group class. The manager wants to adjust the class schedule.",
        "data_type": "discrete",
        "min_val": 1,
        "max_val": 45,
        "decimals": 0
    },
    {
        "title": "Plant Growth (cm per week)",
        "text": "A botanist records the weekly growth in centimeters for plants in an experiment. The aim is to compare fertilizer effectiveness.",
        "data_type": "continuous",
        "min_val": 0.2,
        "max_val": 8.6,
        "decimals": 1
    },
    {
        "title": "Blood Donation Volume",
        "text": "A blood bank measures the volume in milliliters donated by each donor. The coordinator wants to ensure consistency.",
        "data_type": "continuous",
        "min_val": 400,
        "max_val": 700,
        "decimals": 1
    },
    {
        "title": "Parking Lot Occupancy",
        "text": "A mall manager records the number of cars parked at noon each day. The goal is to analyze peak shopping times.",
        "data_type": "discrete",
        "min_val": 10,
        "max_val": 380,
        "decimals": 0
    },
    {
        "title": "Student Commute Distance",
        "text": "A university surveys students about their daily commute distance in miles. Administrators want to improve campus accessibility.",
        "data_type": "continuous",
        "min_val": 0.5,
        "max_val": 42.5,
        "decimals": 1
    },
    {
        "title": "Weekly Grocery Budget",
        "text": "A consumer research group collects data on the weekly grocery budgets of households. The aim is to study spending patterns.",
        "data_type": "continuous",
        "min_val": 20,
        "max_val": 320,
        "decimals": 2
    },
    {
        "title": "Email Count Per Day",
        "text": "An IT department logs the number of emails sent by employees daily. The company wants to optimize communication efficiency.",
        "data_type": "discrete",
        "min_val": 1,
        "max_val": 115,
        "decimals": 0
    },
    {
        "title": "Laptop Battery Life (Hours)",
        "text": "A technology magazine tests new laptops for battery life in hours. The reviewers want to compare endurance across brands.",
        "data_type": "continuous",
        "min_val": 2.1,
        "max_val": 22.8,
        "decimals": 1
    },
    {
        "title": "Number of Social Media Followers",
        "text": "A marketing agency tracks the number of followers on clients’ social media accounts. The agency wants to study online influence.",
        "data_type": "discrete",
        "min_val": 40,
        "max_val": 120000,
        "decimals": 0
    },
    {
        "title": "Class Test Completion Time",
        "text": "A teacher records how many minutes it takes each student to finish a test. The data helps adjust time limits.",
        "data_type": "continuous",
        "min_val": 8,
        "max_val": 62,
        "decimals": 0
    },
    {
        "title": "Number of App Downloads",
        "text": "A developer monitors the number of downloads per day for a new mobile app. The goal is to study launch performance.",
        "data_type": "discrete",
        "min_val": 1,
        "max_val": 10000,
        "decimals": 0
    },
    {
        "title": "Miles Run by Marathon Participants",
        "text": "A race organizer records the number of miles run by each marathon participant during training. The aim is to spot training patterns.",
        "data_type": "continuous",
        "min_val": 5,
        "max_val": 120,
        "decimals": 1
    },
    {
        "title": "Water Consumption per Household",
        "text": "A city collects the number of gallons of water consumed monthly per household. The goal is to manage resources.",
        "data_type": "continuous",
        "min_val": 300,
        "max_val": 16000,
        "decimals": 0
    },
    {
        "title": "Pages Written in a Novel",
        "text": "A publishing company tracks the number of pages in manuscripts submitted by writers. The aim is to understand trends in novel length.",
        "data_type": "discrete",
        "min_val": 100,
        "max_val": 780,
        "decimals": 0
    },
    {
        "title": "Daily Temperature in a City",
        "text": "A meteorologist records the daily high temperature for a city over a year. The goal is to observe seasonal variations.",
        "data_type": "continuous",
        "min_val": -10,
        "max_val": 112,
        "decimals": 1
    },
    {
        "title": "Movie Review Star Ratings",
        "text": "A website collects the number of stars (1 to 5) given by users to movies. The platform wants to summarize viewer satisfaction.",
        "data_type": "discrete",
        "min_val": 1,
        "max_val": 5,
        "decimals": 0
    },
    {
        "title": "Children’s Toothbrush Use",
        "text": "A dental survey asks how many times per week children use their toothbrush. Dentists want to encourage healthy habits.",
        "data_type": "discrete",
        "min_val": 0,
        "max_val": 21,
        "decimals": 0
    },
    {
        "title": "Ice Cream Cone Weights",
        "text": "An ice cream shop measures the weight of each cone served. The owner wants to maintain consistent serving sizes.",
        "data_type": "continuous",
        "min_val": 48,
        "max_val": 188,
        "decimals": 1
    },
    {
        "title": "Pet Age at Adoption",
        "text": "An animal shelter records the age in months of each pet at the time of adoption. The staff wants to encourage timely placements.",
        "data_type": "continuous",
        "min_val": 2,
        "max_val": 168,
        "decimals": 0
    },
    {
        "title": "Restaurant Check Amount",
        "text": "A restaurant logs the total dollar amount of each customer check. The owner wants to analyze spending trends.",
        "data_type": "continuous",
        "min_val": 8.50,
        "max_val": 295.60,
        "decimals": 2
    },
    {
        "title": "Household Internet Speed",
        "text": "A service provider records the download speed in Mbps for households in a region. The goal is to study service quality.",
        "data_type": "continuous",
        "min_val": 2.1,
        "max_val": 850.7,
        "decimals": 1
    },
    {
        "title": "Lightbulb Lifespan",
        "text": "A manufacturer tests the number of hours each lightbulb lasts. Engineers want to improve product durability.",
        "data_type": "continuous",
        "min_val": 200,
        "max_val": 2500,
        "decimals": 0
    },
    {
        "title": "Flight Delay (Minutes)",
        "text": "An airport tracks the delay in minutes for arriving flights. The administration wants to improve punctuality.",
        "data_type": "continuous",
        "min_val": 0,
        "max_val": 185,
        "decimals": 0
    },
    {
        "title": "Hours Worked Per Week",
        "text": "A company records how many hours employees work each week. Management wants to ensure a healthy work-life balance.",
        "data_type": "continuous",
        "min_val": 12,
        "max_val": 80,
        "decimals": 1
    },
    {
        "title": "Soup Can Volume",
        "text": "A food manufacturer measures the volume in milliliters of soup in cans. The company wants to meet labeling requirements.",
        "data_type": "continuous",
        "min_val": 290.0,
        "max_val": 530.0,
        "decimals": 1
    },
    {
        "title": "Birthday Party Guest Count",
        "text": "A party planner tracks the number of guests at each birthday party. The business wants to optimize party packages.",
        "data_type": "discrete",
        "min_val": 5,
        "max_val": 65,
        "decimals": 0
    },
    {
        "title": "Shoe Size Distribution",
        "text": "A shoe store records the shoe size for each customer purchase. The manager wants to adjust inventory.",
        "data_type": "discrete",
        "min_val": 3,
        "max_val": 16,
        "decimals": 0
    },
    {
        "title": "Grocery Items Per Visit",
        "text": "A cashier records the number of items purchased per customer at checkout. The store owner wants to improve checkout flow.",
        "data_type": "discrete",
        "min_val": 1,
        "max_val": 105,
        "decimals": 0
    },
    {
        "title": "Calories Burned in Zumba Class",
        "text": "A fitness instructor logs calories burned per participant in a Zumba class. The goal is to study workout effectiveness.",
        "data_type": "continuous",
        "min_val": 150,
        "max_val": 950,
        "decimals": 0
    },
    {
        "title": "Fish Tank pH Levels",
        "text": "A pet store measures the pH levels in their fish tanks. The staff wants to maintain a healthy environment.",
        "data_type": "continuous",
        "min_val": 5.9,
        "max_val": 8.7,
        "decimals": 2
    },
    {
        "title": "Time Spent Shopping (Minutes)",
        "text": "A mall surveys customers on how many minutes they spend shopping during each visit. Management wants to maximize engagement.",
        "data_type": "continuous",
        "min_val": 8,
        "max_val": 330,
        "decimals": 0
    },
    {
        "title": "Trees Planted by Volunteers",
        "text": "An environmental group counts the number of trees planted by each volunteer. The organization wants to recognize top contributors.",
        "data_type": "discrete",
        "min_val": 1,
        "max_val": 55,
        "decimals": 0
    },
    {
        "title": "Number of Siblings",
        "text": "A family therapist records how many siblings each client has. The data is used for family dynamics studies.",
        "data_type": "discrete",
        "min_val": 0,
        "max_val": 7,
        "decimals": 0
    },
    {
        "title": "Speed of Cyclists in Race",
        "text": "A coach measures the average speed in km/h of cyclists during a race. The aim is to track performance improvement.",
        "data_type": "continuous",
        "min_val": 14.2,
        "max_val": 52.5,
        "decimals": 1
    },
    {
        "title": "Baby Birth Weight",
        "text": "A hospital records the weight in grams of each newborn. The staff wants to monitor neonatal health.",
        "data_type": "continuous",
        "min_val": 1800,
        "max_val": 5100,
        "decimals": 0
    },
    {
        "title": "Stairs Climbed Daily",
        "text": "A smartwatch app logs the number of flights of stairs climbed per user per day. The goal is to promote activity.",
        "data_type": "discrete",
        "min_val": 0,
        "max_val": 120,
        "decimals": 0
    },
    {
        "title": "Distance Thrown in Shot Put",
        "text": "A track coach measures the distance in meters thrown in the shot put event. The goal is to monitor training progress.",
        "data_type": "continuous",
        "min_val": 5.8,
        "max_val": 24.3,
        "decimals": 2
    },
    {
        "title": "Number of Houses Sold Monthly",
        "text": "A real estate agency records the number of homes sold each month. The manager wants to track sales trends.",
        "data_type": "discrete",
        "min_val": 0,
        "max_val": 95,
        "decimals": 0
    },
    {
        "title": "Taxi Fare Per Ride",
        "text": "A taxi company records the fare in dollars for each ride. The company wants to study price distribution.",
        "data_type": "continuous",
        "min_val": 3.5,
        "max_val": 130.5,
        "decimals": 2
    },
    {
        "title": "Sugar Content in Sodas",
        "text": "A beverage company measures the grams of sugar per can of soda. The nutritionist wants to monitor health compliance.",
        "data_type": "continuous",
        "min_val": 18,
        "max_val": 62,
        "decimals": 1
    },
    {
        "title": "Rainfall Per Month",
        "text": "A weather station tracks the rainfall in millimeters per month. The goal is to analyze seasonal patterns.",
        "data_type": "continuous",
        "min_val": 0.0,
        "max_val": 430.0,
        "decimals": 1
    },
    {
        "title": "Printer Pages Used Per Day",
        "text": "An office records the number of pages printed each day. The admin wants to manage paper consumption.",
        "data_type": "discrete",
        "min_val": 0,
        "max_val": 800,
        "decimals": 0
    },
    {
        "title": "Average Grade in Course",
        "text": "A university reports the average percentage grade in an introductory course. The department wants to study grade distribution.",
        "data_type": "continuous",
        "min_val": 50.0,
        "max_val": 99.9,
        "decimals": 1
    },
    {
        "title": "Kids' Allowance Per Week",
        "text": "A parenting magazine surveys the amount of weekly allowance in dollars given to children. The aim is to spot financial trends.",
        "data_type": "continuous",
        "min_val": 0,
        "max_val": 80,
        "decimals": 2
    },
    {
        "title": "Rainy Days Per Year",
        "text": "A city records the number of days it rains in a year. Planners use the data for flood control.",
        "data_type": "discrete",
        "min_val": 2,
        "max_val": 181,
        "decimals": 0
    },
    {
        "title": "Table Tennis Rally Length",
        "text": "A coach logs the number of consecutive hits in each table tennis rally. The goal is to train consistency.",
        "data_type": "discrete",
        "min_val": 1,
        "max_val": 67,
        "decimals": 0
    },
    {
        "title": "Sleep Duration Per Night",
        "text": "A wellness study tracks the number of hours participants sleep per night. Researchers want to analyze rest patterns.",
        "data_type": "continuous",
        "min_val": 2.3,
        "max_val": 12.2,
        "decimals": 1
    },
    {
        "title": "Medication Dosage (mg)",
        "text": "A pharmacist records the dosage in milligrams prescribed for patients. The aim is to monitor prescription patterns.",
        "data_type": "continuous",
        "min_val": 2.5,
        "max_val": 800,
        "decimals": 1
    },
    {
        "title": "Electricity Used Per Month",
        "text": "A utility company tracks the kilowatt-hours used per household monthly. The data supports conservation programs.",
        "data_type": "continuous",
        "min_val": 50,
        "max_val": 4400,
        "decimals": 0
    },
    {
        "title": "Points Scored in Basketball Game",
        "text": "A coach records the points scored by each player in a basketball game. The data helps assess performance.",
        "data_type": "discrete",
        "min_val": 0,
        "max_val": 52,
        "decimals": 0
    },
    {
        "title": "Charity Donation Amount",
        "text": "A fundraiser logs the dollar amount of each donation. The charity wants to analyze giving trends.",
        "data_type": "continuous",
        "min_val": 1,
        "max_val": 2000,
        "decimals": 2
    },
    {
        "title": "Packets Processed Per Second",
        "text": "A network engineer measures how many data packets are processed per second. The aim is to monitor bandwidth.",
        "data_type": "discrete",
        "min_val": 100,
        "max_val": 100000,
        "decimals": 0
    },
    {
        "title": "Miles Biked Per Week",
        "text": "A cycling club logs the weekly miles biked per member. The data helps organize group rides.",
        "data_type": "continuous",
        "min_val": 3.5,
        "max_val": 212.7,
        "decimals": 1
    },
    {
        "title": "Final Exam Scores",
        "text": "A teacher records the score for each student on the final exam. The results are used to evaluate instruction.",
        "data_type": "discrete",
        "min_val": 32,
        "max_val": 100,
        "decimals": 0
    },
    {
        "title": "Cups of Coffee Sold Daily",
        "text": "A coffee shop tracks how many cups of coffee are sold each day. The goal is to manage stock.",
        "data_type": "discrete",
        "min_val": 10,
        "max_val": 780,
        "decimals": 0
    },
    {
        "title": "Savings Account Interest Rate",
        "text": "A bank tracks the annual interest rate offered for new savings accounts. The finance team wants to study competition.",
        "data_type": "continuous",
        "min_val": 0.1,
        "max_val": 7.5,
        "decimals": 2
    },
    {
        "title": "Bus Stops per Route",
        "text": "A transportation planner logs the number of stops on each bus route. The aim is to optimize coverage.",
        "data_type": "discrete",
        "min_val": 3,
        "max_val": 88,
        "decimals": 0
    },
    {
        "title": "Inches of Snowfall",
        "text": "A weather service measures the total inches of snow fallen per storm. The goal is to help city response.",
        "data_type": "continuous",
        "min_val": 0.0,
        "max_val": 39.2,
        "decimals": 1
    },
    {
        "title": "Number of Chapters per Book",
        "text": "A publisher counts how many chapters are in each book. Editors want to study writing trends.",
        "data_type": "discrete",
        "min_val": 1,
        "max_val": 68,
        "decimals": 0
    },
    {
        "title": "Heartbeats Per Minute",
        "text": "A wearable device records users’ heart rates in beats per minute. The company analyzes fitness patterns.",
        "data_type": "continuous",
        "min_val": 42,
        "max_val": 210,
        "decimals": 0
    },
    {
        "title": "Time Spent on Homework",
        "text": "A teacher asks students how many minutes they spend on homework nightly. The data is used to plan assignments.",
        "data_type": "continuous",
        "min_val": 10,
        "max_val": 180,
        "decimals": 0
    },
    {
        "title": "Glass of Water Consumed",
        "text": "A nutritionist records how many glasses of water people drink daily. The aim is to promote healthy habits.",
        "data_type": "discrete",
        "min_val": 0,
        "max_val": 21,
        "decimals": 0
    },
    {
        "title": "Bread Slices in a Loaf",
        "text": "A bakery logs the number of slices in each loaf. The aim is to control product consistency.",
        "data_type": "discrete",
        "min_val": 10,
        "max_val": 32,
        "decimals": 0
    },
    {
        "title": "Oven Temperature Setting",
        "text": "A chef notes the temperature in degrees Fahrenheit for each recipe baked. The kitchen staff wants to ensure proper cooking.",
        "data_type": "continuous",
        "min_val": 200,
        "max_val": 550,
        "decimals": 0
    },
    {
        "title": "Sales Calls Made Per Day",
        "text": "A sales manager records the number of calls made by each representative daily. The data helps set targets.",
        "data_type": "discrete",
        "min_val": 0,
        "max_val": 62,
        "decimals": 0
    },
    {
        "title": "Length of River Sections",
        "text": "A geographer measures the length in miles of various sections of a river. The aim is to study river geography.",
        "data_type": "continuous",
        "min_val": 0.8,
        "max_val": 28.5,
        "decimals": 2
    },
    {
        "title": "Candies in a Jar",
        "text": "A contest asks participants to guess the number of candies in a jar. The organizer records the actual count for each contest.",
        "data_type": "discrete",
        "min_val": 10,
        "max_val": 2800,
        "decimals": 0
    },
    {
        "title": "Music Track Length (Seconds)",
        "text": "A streaming service records the length in seconds of each song in its database. The goal is to analyze listener trends.",
        "data_type": "continuous",
        "min_val": 60,
        "max_val": 800,
        "decimals": 0
    },
    {
        "title": "Reading Speed (Words Per Minute)",
        "text": "A literacy study measures reading speed in words per minute for participants. The aim is to design literacy interventions.",
        "data_type": "continuous",
        "min_val": 60,
        "max_val": 580,
        "decimals": 1
    },
    {
        "title": "Movie Theater Seat Occupancy",
        "text": "A theater logs the number of seats filled per show. The manager wants to optimize screening schedules.",
        "data_type": "discrete",
        "min_val": 10,
        "max_val": 320,
        "decimals": 0
    },
    {
        "title": "Minutes Spent Commuting",
        "text": "A transport survey collects the number of minutes spent commuting daily. Planners use it for public transit improvements.",
        "data_type": "continuous",
        "min_val": 3,
        "max_val": 195,
        "decimals": 0
    },
    {
        "title": "Apple Orchard Yield (Bushels)",
        "text": "A farmer tracks the number of bushels of apples picked per day. The data is used for yield optimization.",
        "data_type": "continuous",
        "min_val": 5.5,
        "max_val": 75.4,
        "decimals": 1
    },
    {
        "title": "Weekly Hours Spent Streaming",
        "text": "A media company surveys how many hours people spend streaming shows weekly. The aim is to analyze viewing patterns.",
        "data_type": "continuous",
        "min_val": 0.5,
        "max_val": 65,
        "decimals": 1
    },
    {
        "title": "Minutes of Phone Conversation",
        "text": "A telecommunications company logs the duration of phone calls in minutes. The data helps design pricing plans.",
        "data_type": "continuous",
        "min_val": 1,
        "max_val": 215,
        "decimals": 0
    },
    {
        "title": "Handshakes at a Conference",
        "text": "An event organizer records the number of handshakes each attendee makes. The aim is to study networking behavior.",
        "data_type": "discrete",
        "min_val": 0,
        "max_val": 88,
        "decimals": 0
    },
    {
        "title": "Energy Drink Caffeine Content",
        "text": "A lab measures the milligrams of caffeine in energy drinks. Health authorities want to enforce safe levels.",
        "data_type": "continuous",
        "min_val": 30,
        "max_val": 370,
        "decimals": 1
    },
    {
        "title": "Bicycle Tire Pressure (PSI)",
        "text": "A bike shop checks the PSI in customers' tires before each ride. The data is used for safety checks.",
        "data_type": "continuous",
        "min_val": 28,
        "max_val": 125,
        "decimals": 1
    },
    {
        "title": "Books Published Per Author",
        "text": "A literary agency logs the number of books published by each client. The agency wants to reward prolific writers.",
        "data_type": "discrete",
        "min_val": 1,
        "max_val": 90,
        "decimals": 0
    },
    {
        "title": "Height of Roller Coasters",
        "text": "An amusement park measures the height in feet of its roller coasters. The marketing team wants to promote the tallest rides.",
        "data_type": "continuous",
        "min_val": 28,
        "max_val": 415,
        "decimals": 1
    },
    {
        "title": "Students Per Dorm Room",
        "text": "A college tracks the number of students assigned to each dorm room. The data helps optimize housing assignments.",
        "data_type": "discrete",
        "min_val": 1,
        "max_val": 5,
        "decimals": 0
    },
    {
        "title": "ATM Withdrawals Per Day",
        "text": "A bank records the number of ATM withdrawals made per customer each day. The data is used for cash supply planning.",
        "data_type": "discrete",
        "min_val": 0,
        "max_val": 12,
        "decimals": 0
    },
    {
        "title": "Blood Sugar Level",
        "text": "A health study measures participants' blood sugar levels in mg/dL after fasting. Researchers want to assess diabetes risk.",
        "data_type": "continuous",
        "min_val": 60,
        "max_val": 300,
        "decimals": 1
    },
    {
        "title": "Volunteers at Food Bank",
        "text": "A food bank records the number of volunteers working each shift. The director wants to improve scheduling.",
        "data_type": "discrete",
        "min_val": 1,
        "max_val": 40,
        "decimals": 0
    },
    {
        "title": "Hours of Sunlight Per Day",
        "text": "A weather station measures the number of sunlight hours per day. Scientists use the data for climate analysis.",
        "data_type": "continuous",
        "min_val": 0.1,
        "max_val": 14.9,
        "decimals": 1
    },
    {
        "title": "Bus Passengers Per Trip",
        "text": "A transit company logs the number of passengers per bus trip. The goal is to optimize route planning.",
        "data_type": "discrete",
        "min_val": 0,
        "max_val": 95,
        "decimals": 0
    },
    {
        "title": "Car Rental Duration (Days)",
        "text": "A rental agency records the number of days each car is rented. The data helps plan fleet utilization.",
        "data_type": "discrete",
        "min_val": 1,
        "max_val": 42,
        "decimals": 0
    },
    {
        "title": "Milk Production Per Cow (Liters)",
        "text": "A dairy farm tracks the liters of milk produced daily per cow. The data is used to optimize nutrition.",
        "data_type": "continuous",
        "min_val": 8.2,
        "max_val": 53.7,
        "decimals": 1
    },
    {
        "title": "Car Engine Size (Liters)",
        "text": "An auto show measures the engine displacement in liters for displayed cars. The organizers want to highlight diversity.",
        "data_type": "continuous",
        "min_val": 0.8,
        "max_val": 8.1,
        "decimals": 2
    },
    {
        "title": "Time Between Trains (Minutes)",
        "text": "A railway operator records the interval in minutes between train arrivals. The goal is to improve scheduling.",
        "data_type": "continuous",
        "min_val": 2.5,
        "max_val": 60,
        "decimals": 1
    },
    {
        "title": "Paperclips in a Box",
        "text": "A stationery company counts the number of paperclips in each box produced. The quality team wants to reduce errors.",
        "data_type": "discrete",
        "min_val": 20,
        "max_val": 105,
        "decimals": 0
    }
]


# Sidebar for controls
st.sidebar.title("📊 Statistics Learning Tool")
st.sidebar.markdown("---")

# Generate new dataset button
if st.sidebar.button("🎲 Generate New Dataset", type="primary"):
    st.session_state.regenerate = True

# Sample size selection
st.sidebar.subheader("Dataset Options")
sample_size_option = st.sidebar.selectbox(
    "Sample Size Range:",
    ["Random (25-200)", "Small (25-49)", "Medium (50-100)", "Large (101-200)"]
)

# Educational sidebar content
st.sidebar.markdown("---")
st.sidebar.subheader("📚 Learning Guide")

with st.sidebar.expander("📈 Measures of Central Tendency"):
    st.markdown("""
    **Mean**: Average of all values
    \( \\bar{x} = \\frac{\\sum x_i}{n} \)
    
    **Median**: Middle value when sorted
    
    **Mode**: Most frequently occurring value(s)
    """)

with st.sidebar.expander("📏 Measures of Spread"):
    st.markdown("""
    **Standard Deviation**: Measures variability
    \( s = \\sqrt{\\frac{\\sum(x_i - \\bar{x})^2}{n-1}} \)
    
    **Five-Number Summary**: Min, Q1, Median, Q3, Max
    """)

with st.sidebar.expander("📊 Histograms"):
    st.markdown("""
    **Sturges' Rule**: \( k = \\lceil 1 + \\log_2(n) \\rceil \)
    
    Where k = number of bins, n = sample size
    
    **Bin Size**: \( \\text{Range} ÷ k \)
    """)

# Initialize session state
if 'regenerate' not in st.session_state:
    st.session_state.regenerate = True

# Main content
st.markdown('<h1 class="main-header">📊 Interactive Statistics Learning Tool</h1>', 
            unsafe_allow_html=True)

st.markdown("""
Welcome to the Statistics Learning Tool! This interactive application generates 
random datasets and demonstrates key statistical concepts including measures of 
central tendency, variability, and data visualization techniques.
""")

# Generate or regenerate data
if st.session_state.regenerate:
    # Randomly select a paragraph for this dataset
    problem = random.choice(paragraphs)
    
    # Store in session state
    st.session_state.problem = problem
    st.session_state.regenerate = False

# Get problem from session state
problem = st.session_state.problem
title = problem["title"]
problem_paragraph = problem["text"]
data_type = problem["data_type"]
min_val = problem["min_val"]
max_val = problem["max_val"]
decimals = problem["decimals"]

# Determine sample size based on selection
if sample_size_option == "Small (25-49)":
    n = random.randint(25, 49)
elif sample_size_option == "Medium (50-100)":
    n = random.randint(50, 100)
elif sample_size_option == "Large (101-200)":
    n = random.randint(101, 200)
else:  # Random
    if random.random() < 0.5:
        n = random.randint(25, 49)
    else:
        n = random.randint(50, 200)

# Generate data based on the problem type
random.seed(42)  # For reproducibility in demo
data = []
for _ in range(n):
    if data_type == "discrete":
        data.append(random.randint(int(min_val), int(max_val)))
    elif data_type == "continuous":
        value = random.uniform(min_val, max_val)
        data.append(round(value, decimals))
    elif data_type == "mixed":
        if random.random() < 0.5:
            value = random.uniform(min_val, max_val)
            data.append(round(value, decimals))
        else:
            data.append(round(random.uniform(min_val, max_val)))

# Display the scenario
st.markdown(f'<h2 class="section-header">📋 Scenario: {title}</h2>', 
            unsafe_allow_html=True)
st.info(problem_paragraph)

# Create tabs for better organization
tab1, tab2, tab3, tab4 = st.tabs(["📊 Data & Statistics", "📈 Histogram", "📦 Box Plot", "🧮 Calculations"])

with tab1:
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("📋 Raw Data")
        st.markdown(f"**Sample Size (n):** {n}")
        st.markdown(f"**Data Type:** {data_type.title()}")
        
        # Display data in a more readable format
        data_display = ", ".join([str(x) for x in data])
        st.text_area("Data Points:", data_display, height=150)
        
        # Sorted data
        sorted_data_display = sorted(data)
        sorted_display = ", ".join([str(x) for x in sorted_data_display])
        st.text_area("Sorted Data (Low to High):", sorted_display, height=150)
    
    with col2:
        st.subheader("📊 Descriptive Statistics")
        
        # Calculate statistics
        data_np = np.array(data)
        mean = round(np.mean(data_np), 2)
        median = round(np.median(data_np), 2)
        std = round(np.std(data_np, ddof=1), 2)
        
        # Calculate mode
        def calculate_mode(data):
            counter = Counter(data)
            max_count = max(counter.values())
            modes = [value for value, count in counter.items() if count == max_count]
            
            if len(modes) == len(data):
                return "No mode (all values appear once)"
            elif len(modes) == 1:
                return str(modes[0])
            else:
                modes.sort()
                return ", ".join(str(mode) for mode in modes)
        
        mode = calculate_mode(data)
        
        # Five-number summary using Tukey's Hinges
        def tukey_hinges(data):
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
        
        sorted_data = np.sort(data_np)
        min_val_stat = round(float(sorted_data[0]), 2)
        max_val_stat = round(float(sorted_data[-1]), 2)
        q1, med, q3 = tukey_hinges(sorted_data)
        
        # Display statistics in styled boxes
        st.markdown(f"""
        <div class="stat-box">
            <strong>Mean:</strong> {mean}<br>
            <strong>Median:</strong> {median}<br>
            <strong>Mode:</strong> {mode}<br>
            <strong>Standard Deviation:</strong> {std}
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("**Five-Number Summary (Tukey's Hinges):**")
        st.markdown(f"""
        <div class="stat-box">
            <strong>Minimum:</strong> {min_val_stat}<br>
            <strong>Q1 (25th percentile):</strong> {q1}<br>
            <strong>Median (50th percentile):</strong> {med}<br>
            <strong>Q3 (75th percentile):</strong> {q3}<br>
            <strong>Maximum:</strong> {max_val_stat}
        </div>
        """, unsafe_allow_html=True)

with tab2:
    st.subheader("📈 Histogram Analysis")
    
    # Calculate bins using Sturges' Rule
    k = math.ceil(1 + math.log2(len(data)))
    
    # Determine bin size and bin edges
    actual_min = min(data)
    actual_max = max(data)
    
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
    
    data_range = data_max - data_min
    bin_size = data_range / k
    
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
    
    k = math.ceil(data_range / bin_size)
    
    # Display bin information
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Number of Bins (k)", k)
    with col2:
        st.metric("Bin Size", bin_size)
    with col3:
        st.metric("Starting Point", data_min)
    
    # Create bin edges
    bin_edges = []
    current_edge = data_min
    for i in range(k + 1):
        bin_edges.append(current_edge)
        current_edge += bin_size
    
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
    
    # Display frequency table
    st.subheader("📋 Frequency Table")
    freq_data = []
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
        freq_data.append({"Interval": interval, "Frequency": freqs[i]})
    
    st.table(freq_data)
    
    # Plot histogram
    fig, ax = plt.subplots(figsize=(10, 6))
    bar_lefts = bin_edges[:-1]
    ax.bar(bar_lefts, freqs, width=bin_size, align='edge', 
           edgecolor='black', alpha=0.7, color='skyblue')
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')
    ax.set_title(f'Histogram: {title}')
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    plt.xticks(bin_edges, rotation=45 if max(len(f"{edge:.2f}") for edge in bin_edges) > 4 else 0)
    plt.tight_layout()
    st.pyplot(fig)

with tab3:
    st.subheader("📦 Box Plot Analysis")
    
    st.markdown("""
    A box plot (box-and-whisker plot) provides a visual summary of the five-number summary:
    - **Box**: Shows the interquartile range (IQR) from Q1 to Q3
    - **Line in box**: Represents the median
    - **Whiskers**: Extend to the minimum and maximum values
    - **Outliers**: Points beyond the whiskers (if any)
    """)
    
    # Create box plot
    fig, ax = plt.subplots(figsize=(10, 6))
    box_plot = ax.boxplot(data, vert=False, patch_artist=True)
    box_plot['boxes'][0].set_facecolor('lightblue')
    box_plot['boxes'][0].set_edgecolor('black')
    ax.set_xlabel('Value')
    ax.set_title(f'Box Plot: {title}')
    ax.set_yticks([])
    ax.grid(axis='x', linestyle='--', alpha=0.7)
    plt.tight_layout()
    st.pyplot(fig)
    
    # Interpretation
    st.markdown("### 🔍 Box Plot Interpretation")
    iqr = q3 - q1
    st.markdown(f"""
    - **Interquartile Range (IQR):** {iqr:.2f}
    - **Range:** {max_val_stat - min_val_stat:.2f}
    - **Skewness:** {'Right-skewed' if mean > median else 'Left-skewed' if mean < median else 'Approximately symmetric'}
    """)

with tab4:
    st.subheader("🧮 Step-by-Step Calculations")
    
    st.markdown("### 📊 Sturges' Rule for Number of Bins")
    st.markdown(f"""
    <div class="formula-box">
    <strong>Formula:</strong> k = ⌈1 + log₂(n)⌉<br>
    <strong>Calculation:</strong> k = ⌈1 + log₂({n})⌉ = ⌈1 + {math.log2(n):.2f}⌉ = {k}
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 📏 Mean Calculation")
    st.markdown(f"""
    <div class="formula-box">
    <strong>Formula:</strong> x̄ = Σxᵢ / n<br>
    <strong>Sum of all values:</strong> {sum(data)}<br>
    <strong>Sample size:</strong> {n}<br>
    <strong>Mean:</strong> {sum(data)} ÷ {n} = {mean}
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 📊 Standard Deviation Calculation")
    variance = round(np.var(data_np, ddof=1), 2)
    st.markdown(f"""
    <div class="formula-box">
    <strong>Sample Variance (s²):</strong> {variance}<br>
    <strong>Sample Standard Deviation (s):</strong> √{variance} = {std}
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666;'>
    <p>📚 Statistics Learning Tool | Built with Streamlit | 
    <a href='#' style='color: #1f77b4;'>Learn More About Statistics</a></p>
</div>
""", unsafe_allow_html=True)
