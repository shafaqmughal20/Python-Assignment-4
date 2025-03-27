import streamlit as st  # Importing Streamlit for creating the web app

def calculate_bmi(weight, height):
    """Calculates BMI using the formula: BMI = weight (kg) / (height (m) ^ 2)"""
    return weight / (height ** 2)

# Streamlit UI
st.title("🏋️‍♂️ BMI Calculator")  # Title of the app
st.write("Calculate your Body Mass Index (BMI) easily.")

# User inputs
weight = st.number_input("Enter your weight (kg):", min_value=1.0, format="%.2f")
height = st.number_input("Enter your height (meters):", min_value=0.5, format="%.2f")

if st.button("Calculate BMI"):
    if weight > 0 and height > 0:
        bmi = calculate_bmi(weight, height)  # Calculate BMI
        st.success(f"📝 Your BMI is: {bmi:.2f}")  # Display result

        # BMI Category Classification
        if bmi < 18.5:
            st.warning("🔹 You are underweight.")
        elif 18.5 <= bmi < 24.9:
            st.success("✅ You have a normal weight.")
        elif 25 <= bmi < 29.9:
            st.warning("⚠️ You are overweight.")
        else:
            st.error("🚨 You are obese. Consider consulting a doctor.")
    else:
        st.error("❌ Please enter valid values for weight and height.")
