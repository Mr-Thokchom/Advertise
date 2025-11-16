import streamlit as st
import pickle
import numpy as np

# Load the trained Logistic Regression model
with open('logistic_regression_model.pkl', 'rb') as file:
    model = pickle.load(file)

st.title("Ad Click Prediction App")

# User input fields
daily_time_spent = st.number_input("Daily Time Spent on Site (minutes):", min_value=0.0, format="%f")
age = st.number_input("Age:", min_value=0, format="%d")
area_income = st.number_input("Area Income (USD):", min_value=0.0, format="%f")
daily_internet_usage = st.number_input("Daily Internet Usage (minutes):", min_value=0.0, format="%f")
male = st.selectbox("Gender:", options=[("Female", 0), ("Male", 1)], format_func=lambda x: x[0])[1]
hour = st.number_input("Hour of Interaction (0-23):", min_value=0, max_value=23, format="%d")
day = st.number_input("Day of Interaction (1-31):", min_value=1, max_value=31, format="%d")

# Predict button
if st.button("Predict"):
    # Prepare input data
    input_data = np.array([[daily_time_spent, age, area_income, daily_internet_usage, male, hour, day]])
    
    # Make prediction
    prediction = model.predict(input_data)

    # Display result
    if prediction[0] == 1:
        st.success("The user is likely to click on the advertisement.")
    else:
        st.info("The user is not likely to click on the advertisement.")