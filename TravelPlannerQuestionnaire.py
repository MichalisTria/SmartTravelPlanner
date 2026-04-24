import streamlit as st
st.set_page_config(page_title="SmartTravel - Questionnaire", page_icon="❓")

import sys
sys.path.append('..')
from recommender import get_recommendations

#TravelPlanner Questionnaire
#Everything Here is just for testing purposes
# Questions and Answers SHOULD BE CHANGED based on Imported Databases

if st.button("Return Home", icon="🏠"):
    st.switch_page("TravelPlannerDemo.py")

st.title("Travel Planner Questionnaire")
st.subheader("Welcome to the Travel Planner Questionnaire! Please answer the following questions to help us plan your perfect trip.")

#selectboxes Travel Style
st.subheader("1. Travel Style")
tools = ["Luxury Traveler: Premium Experiences & Accomodations", "Adventure Seeker: Thrilling Activities & Outdoor Exploration", "Cultural Explorer: History, Art & Local Traditions", "Relaxation Focused: Beach Resorts & Peaceful Retreats", "Budget Backpacker: Affordable Travel & Authentic Experiences"]
travel_style = st.selectbox("What's your travel style?", tools)


# Multiselect Travel Interests
st.subheader("2. Your Travel Interests")
interest_options = [
    "Photography",
    "Food & Cuisine",
    "Wildlife",
    "Architecture",
    "Beaches",
    "Mountains",
    "History",
    "Nightlife",
    "Shopping", 
    "Art & Museums",
    "Hiking",
    "Water Sports",
]
selected_interests = st.multiselect("Select all that apply", interest_options)
for interest in selected_interests:
    st.write(f"- {interest}")


#Slider Daily Budget
st.subheader("3. What's your daily budget?")
daily_budget = st.slider("Per Person, including accomodation", min_value=0, max_value=1000, step=10, value=50)
st.write(f"Your daily budget is: ${daily_budget}")


#selectboxes Ideal Climate
st.subheader("4. Ideal Climate")
climates = ["Tropical", "Temperate", "Cold", "Desert", "Any Climate - Weather doesn't matter to me"]
ideal_climate = st.selectbox("Choose your preferred weather", climates)


#Slider Travel Duration
st.subheader("5. How Long is your trip?")
travel_duration = st.slider("How long is your trip?", min_value=1, max_value=60, step=1, value=7)

if travel_duration == 1:
    st.write(f"Your trip duration is: {travel_duration} day")   
else:
    st.write(f"Your trip duration is: {travel_duration} days")


#selectboxes Travel Pace
st.subheader("6. Your Travel Pace")
travel_pace = ["Relaxed: Take it slow, enjoy each moment", "Moderate: Balance of activities and rest", "Packed: See and do as much as possible"]
travel_pace = st.selectbox("How do you like to experience destinations?", travel_pace)

#Selectboxes Travel Accomodation
st.subheader("7. Your Travel Accommodation")
accomodation_options = ["Luxury Hotels", "Mid-range Hotels", "Budget Hotels", "Cabins", "Camping", "Hostels", "Vacation Rentals (Airbnb, etc.)", "Boutique Hotels", "Resorts", "Bed & Breakfasts"]

accommodation = st.multiselect("What type of accommodations do you like most?", accomodation_options) 
for accomodation in accommodation:
    st.write(f"- {accomodation}")

#selectboxes Travel Transportation
st.subheader("8. Your Travel Transportation")
transportation_options = ["Air Travel", "Train Travel", "Road Trips (Car Rental)", "Cruises", "Public Transportation (Buses, Subways)", "Biking", "Walking", "Domestic Flights", "International Flights"]
transportation = st.multiselect("What modes of transportation do you prefer?", transportation_options)
for transportation in transportation:
    st.write(f"- {transportation}")

#selectboxes Activities
st.subheader("9. Your Preferred Activities")
activities_options = ["City Tours", "Nature Hikes", "Cultural Experiences (Museums, Local Events)", "Adventure Activities (Ziplining, Rafting)", "Relaxation (Spas, Beach Days)", "Food & Drink Experiences (Cooking Classes, Wine Tasting)", "Nightlife (Bars, Clubs)", "Shopping", "Wildlife Encounters", "Historical Sites"]
activities = st.multiselect("What activities do you enjoy most while traveling?", activities_options)
for activity in activities:
    st.write(f"- {activity}")


#add spacing between buttons and stats with 150px distance (AI generated)
st.markdown("<div style='margin-top: 50px;'></div>", unsafe_allow_html=True)

st.button("View Results✔️")
    st.session_state.preferences = { #AI-generated
        "travel_style": travel_style,
        "ideal_climate": ideal_climate,
        "interests": selected_interests,
        "daily_budget": daily_budget,
        "activities": activities,
        "accommodation": accommodation,
        "travel_pace": travel_pace,
    }
    st.session_state.recommendations = get_recommendations(st.session_state.preferences)
    st.switch_page("pages/TravelPlannerResults.py")
