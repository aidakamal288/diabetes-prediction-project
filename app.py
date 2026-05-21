import streamlit as st
import joblib
import pandas as pd

# Load model

model = joblib.load('diabetes_model.pkl')

# Title

st.title("Diabetes Prediction App")

st.write("Enter patient information below:")

# Inputs

BMI = st.number_input("BMI")

Age = st.number_input("Age")

HighBP = st.selectbox(
    "High Blood Pressure",
    [0, 1]
)

HighChol = st.selectbox(
    "High Cholesterol",
    [0, 1]
)

PhysActivity = st.selectbox(
    "Physical Activity",
    [0, 1]
)

LifestyleScore = st.number_input(
    "Lifestyle Score"
)

# Prediction Button

if st.button("Predict"):

    input_data = pd.DataFrame([[
        BMI,
        Age,
        HighBP,
        HighChol,
        PhysActivity,
        LifestyleScore
    ]],

    columns=[
        'BMI',
        'Age',
        'HighBP',
        'HighChol',
        'PhysActivity',
        'LifestyleScore'
    ])

    prediction = model.predict(input_data)

    if prediction[0] == 1:

        st.error("Diabetic")

    else:

        st.success("Non-Diabetic")
