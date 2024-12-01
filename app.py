import streamlit as st
import numpy as np
import pandas as pd
import pickle
import base64

# Load the trained Gradient Boosting model
with open("gradient_boosting_best_model.pkl", "rb") as file:
    best_regressor = pickle.load(file)

# Function to make predictions
def pred(Gender, Age, Height, Weight, Duration, Heart_rate, Body_temp):
    # Convert inputs to a NumPy array
    features = np.array([[Gender, Age, Height, Weight, Duration, Heart_rate, Body_temp]])
    prediction = best_regressor.predict(features)
    return prediction[0]


# Encode the background image
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

encoded_image = get_base64_image("image.png")  # Add your background image here

# Add CSS for darkened background and branding
page_bg = f"""
<style>
.stApp {{
    background: linear-gradient(rgba(0, 0, 0, 0.6), rgba(0, 0, 0, 0.6)), 
                url("data:image/png;base64,{encoded_image}");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
    color: #ffffff;  /* Make text white for better contrast */
}}
h1 {{
    font-family: 'Arial Black', sans-serif;
    color: #FFD700;  /* Gold for the main title */
}}
h2, h3 {{
    font-family: 'Verdana', sans-serif;
    color: #FF7F50;  /* Coral for section headers */
}}
p {{
    font-size: 16px;
    line-height: 1.6;
}}
button {{
    background-color: #FF7F50;
    color: #ffffff;
}}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# Branding and Header
st.title("🔥 FitBurnTrack")
st.markdown("""
Welcome to **FitBurnTrack**, your **AI-powered companion** for tracking calorie burn and fitness progress.

🧠 **Powered by Machine Learning**  
📊 **Accurate Calorie Insights**  
💪 **Built for Your Fitness Journey**

""")

# Create input form
with st.form("prediction_form"):
    st.header("📋 Enter Your Details Below:")
    
    Gender = st.selectbox('👤 Gender', ['Male', 'Female'], help="Select your gender.")
    Age = st.slider('🎂 Age', 10, 100, value=25, step=1, help="Enter your age in years.")
    Height = st.number_input('📏 Height (cm)', min_value=100, max_value=250, value=170, step=1, help="Enter your height in centimeters.")
    Weight = st.number_input('⚖️ Weight (kg)', min_value=30, max_value=200, value=70, step=1, help="Enter your weight in kilograms.")
    Duration = st.slider('⏱️ Exercise Duration (minutes)', 1, 240, value=30, step=1, help="Enter the duration of your exercise.")
    Heart_rate = st.slider('💓 Heart Rate (bpm)', 50, 200, value=100, step=1, help="Enter your average heart rate during the exercise.")
    Body_temp = st.slider('🌡️ Body Temperature (°C)', 35.0, 50.0    , value=37.0, step=0.1, help="Enter your body temperature.")

    # Submit button
    submitted = st.form_submit_button("🚀 Predict Calories Burned")

# Prediction logic
if submitted:
    # Convert gender to numeric for model input
    Gender_numeric = 1 if Gender == "Male" else 0
    result = pred(Gender_numeric, Age, Height, Weight, Duration, Heart_rate, Body_temp)
    st.markdown(f"""
    ## 🎉 Prediction Results:
    🔥 You have burned approximately **{result:.2f} calories** during your exercise session!  
    Stay consistent, and track your fitness progress with **FitBurnTrack**. 💪
    """)
    st.snow()
