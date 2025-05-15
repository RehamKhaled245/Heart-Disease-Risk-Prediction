# app.py

import streamlit as st
import joblib
import pandas as pd

st.set_page_config(page_title="Heart Disease Risk Prediction", page_icon="❤️", layout="wide")

st.markdown("""
    <style>
            .img1{
            display:flex;
            justify-content:space-between;
            padding:30px
            }
            *{
            
            margin:0px;
            padding:0px
            }
        .main, .block-container, .stApp {
            background-color: #ffffff !important;
        }

        * {
            color: #000000 !important;
        }

        html, body, [class*="css"] {
            font-size:20px !important;
            font-family: 'Arial', sans-serif !important;
        }


        label, .stRadio, .stSelectbox, .stSlider {
            font-size: 70px !important;
            font-weight: bold;
        }

        .stTitle {
            font-size: 35px !important;
            font-weight: bold !important;
        }

      
        .stButton>button {
            background-color: #cc0000;
            color: white;
            font-size: 20px;
            padding: 0.5em 2em;
            border: none;
            border-radius: 8px;
            
        }
        .title{
            background-color:#f0f6f0;
            }  
        .title2{
            padding-bottom:20px;
            margin-bottom:20px;
            padding-left:45px;
            }   
    </style>
""", unsafe_allow_html=True)



left_col, right_col = st.columns([3, 1])  

with left_col:
    
    st.markdown("""
        <div class="title style='padding:30px; '">
        <h1 class="title1" style='color: black;padding-left:40px; higth:300px'>Heart Disease Risk Prediction ❤️</h1>
        <p class="title2" style='font-size:20px';padding-bottom:20px; margin-bottom:20px; padding-left:45px; color: black;'>
        This app uses <strong>Heart Disease Prediction</strong> based on several symptoms and factors.<br>
        Select the symptoms, and we will tell you if you're at risk of heart disease.
        </p>   
        </div>
    """, unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    chest_pain = st.radio("Do you have Chest pain?", ('Yes', 'No'))
    fatigue = st.radio("Do you have Fatigue?", ('Yes', 'No'))
    dizziness = st.radio("Do you have Dizziness?", ('Yes', 'No'))
    pain_arms_jaw_back = st.radio("Do you have Pain in arms/jaw/back?", ('Yes', 'No'))
    high_cholesterol = st.radio("Do you have High cholesterol?", ('Yes', 'No'))
    smoking = st.radio("Do you smoke?", ('Yes', 'No'))
    family_history = st.radio("Do you have Family history of heart disease?", ('Yes', 'No'))
    gender = st.radio("What is your Gender?", ["Male", "Female"])
with col2:
    shortness_breath = st.radio("Do you have Shortness of breath?", ('Yes', 'No'))
    palpitations = st.radio("Do you have Palpitations?", ('Yes', 'No'))
    swelling = st.radio("Do you have Swelling (legs or ankles)?", ('Yes', 'No'))
    cold_sweats_nausea = st.radio("Do you have Cold sweats or nausea?", ('Yes', 'No'))
    high_bp = st.radio("Do you have High blood pressure?", ('Yes', 'No'))
    diabetes = st.radio("Do you have Diabetes?", ('Yes', 'No'))
    sedentary_lifestyle = st.radio("Do you have Sedentary lifestyle?", ('Yes', 'No'))
    chronic_stress = st.radio("Do you have Chronic stress?", ('Yes', 'No'))
    Obesity = st.radio("Do you have obesity?", ('Yes', 'No'))



age = st.slider("Enter your age:", 18, 100, 50)



def map_input(value):
    return 1 if value == 'Yes' else 0

input_data = {
    'Chest_Pain': map_input(chest_pain),
    'Shortness_of_Breath': map_input(shortness_breath),
    'Fatigue': map_input(fatigue),
    'Palpitations': map_input(palpitations),
    'Dizziness': map_input(dizziness),
    'Swelling': map_input(swelling),
    'Pain_Arms_Jaw_Back': map_input(pain_arms_jaw_back),
    'Cold_Sweats_Nausea': map_input(cold_sweats_nausea),
    'High_BP': map_input(high_bp),
    'High_Cholesterol': map_input(high_cholesterol),
    'Diabetes': map_input(diabetes),
    'Smoking': map_input(smoking),
    'Sedentary_Lifestyle': map_input(sedentary_lifestyle),
    'Family_History': map_input(family_history),
    'Chronic_Stress': map_input(chronic_stress),
    'Obesity': map_input(Obesity),
    'Age': age,
    'Gender': 1 if gender == 'Male' else 0
}

try:
    model = joblib.load('final_logistic_regression_model.pkl')
except FileNotFoundError:
    st.error("❌ Model file not found. Please make sure 'final_logistic_regression_model.pkl' exists.")
    st.stop()
features=['Chest_Pain', 'Shortness_of_Breath', 'Fatigue', 'Palpitations',
       'Dizziness', 'Swelling', 'Pain_Arms_Jaw_Back', 'Cold_Sweats_Nausea',
       'High_BP', 'High_Cholesterol', 'Diabetes', 'Smoking', 'Obesity',
       'Sedentary_Lifestyle', 'Family_History', 'Chronic_Stress', 'Gender',
       'Age']
if st.button("Predict"):

    input_df = pd.DataFrame([input_data])[features]

    prediction = model.predict(input_df)

    if prediction[0] == 1:
        st.markdown("### ❗ **The person is at risk of heart disease.**")
    else:
        st.markdown("### ✅ **The person is not at risk of heart disease.**")
        st.balloons()
