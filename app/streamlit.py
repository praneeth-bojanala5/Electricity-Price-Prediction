import streamlit as st
import pandas as pd
import requests

st.title('Electricity Price Prediction')

def get_prediction(data):
    response = requests.post('http://localhost:5000/predict', json=data)
    return response.json()

# Define user inputs with default values and selectbox for Holiday
user_input = {
    "Holiday": st.selectbox('Holiday', ['None', 'New Year\'s Day', 'Christmas']),
    "DayOfWeek": st.number_input('Day of Week', min_value=1, max_value=7, value=1),
    "WeekOfYear": st.number_input('Week of Year', min_value=1, max_value=52, value=1),
    "Day": st.number_input('Day', min_value=1, max_value=31, value=1),
    "Month": st.number_input('Month', min_value=1, max_value=12, value=1),
    "Year": st.number_input('Year', min_value=2000, max_value=2100, value=2023),
    "PeriodOfDay": st.number_input('Period of Day', min_value=1, max_value=24, value=1),
    "ForecastWindProduction": st.number_input('Forecast Wind Production', min_value=0.0, value=0.0),
    "SystemLoadEA": st.number_input('System Load EA', min_value=0.0, value=0.0),
    "SMPEA": st.number_input('SMPEA', min_value=0.0, value=0.0),
    "ORKTemperature": st.number_input('ORK Temperature', min_value=-50.0, max_value=50.0, value=0.0),
    "ORKWindspeed": st.number_input('ORK Windspeed', min_value=0.0, value=0.0),
    "CO2Intensity": st.number_input('CO2 Intensity', min_value=0.0, value=0.0),
    "ActualWindProduction": st.number_input('Actual Wind Production', min_value=0.0, value=0.0),
    "SystemLoadEP2": st.number_input('System Load EP2', min_value=0.0, value=0.0)
}

if st.button('Predict'):
    # Send input data to Flask API
    prediction = get_prediction([user_input])
    st.write(f"Predicted Electricity Price: {prediction[0]}")
