import streamlit as st
import requests
import pandas as pd

st.title("Electricity Price Prediction")

st.write("Enter the input parameters for prediction:")

DayOfWeek = st.number_input("DayOfWeek", min_value=0, max_value=6, value=0)
WeekOfYear = st.number_input("WeekOfYear", min_value=1, max_value=52, value=1)
Day = st.number_input("Day", min_value=1, max_value=31, value=1)
Month = st.number_input("Month", min_value=1, max_value=12, value=1)
Year = st.number_input("Year", min_value=2000, max_value=2100, value=2023)
PeriodOfDay = st.number_input("PeriodOfDay", min_value=0, max_value=23, value=0)
ForecastWindProduction = st.number_input("ForecastWindProduction", value=0.0)
SystemLoadEA = st.number_input("SystemLoadEA", value=0.0)
SMPEA = st.number_input("SMPEA", value=0.0)
ORKTemperature = st.number_input("ORKTemperature", value=0.0)
ORKWindspeed = st.number_input("ORKWindspeed", value=0.0)
CO2Intensity = st.number_input("CO2Intensity", value=0.0)
ActualWindProduction = st.number_input("ActualWindProduction", value=0.0)
SystemLoadEP2 = st.number_input("SystemLoadEP2", value=0.0)
Holiday = st.text_input("Holiday", value="None")

input_data = {
    "DayOfWeek": DayOfWeek,
    "WeekOfYear": WeekOfYear,
    "Day": Day,
    "Month": Month,
    "Year": Year,
    "PeriodOfDay": PeriodOfDay,
    "ForecastWindProduction": ForecastWindProduction,
    "SystemLoadEA": SystemLoadEA,
    "SMPEA": SMPEA,
    "ORKTemperature": ORKTemperature,
    "ORKWindspeed": ORKWindspeed,
    "CO2Intensity": CO2Intensity,
    "ActualWindProduction": ActualWindProduction,
    "SystemLoadEP2": SystemLoadEP2,
    "Holiday": Holiday
}

if st.button("Predict"):
    response = requests.post("http://137.184.146.246/predict", json={"inputs": [input_data]})
    if response.status_code == 200:
        prediction = response.json()["predictions"][0]
        st.success(f"The predicted electricity price is: {prediction}")
    else:
        st.error(f"Error: {response.status_code}, {response.text}")

