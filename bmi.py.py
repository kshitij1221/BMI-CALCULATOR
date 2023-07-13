import streamlit as st

def calculate_bmi(weight, height):
    height_m = height / 100  # Convert height from cm to m
    bmi = weight / (height_m ** 2)
    return bmi

# Page layout
st.title("BMI Calculator")
st.subheader("Enter Your Details")

# Name
name = st.text_input("Name")

# Gender
gender = st.radio("Gender", ("Male", "Female", "Other"))

# Age
age = st.number_input("Age", min_value=0, max_value=150, step=1)

# Address
address = st.text_area("Address")

# Hobbies
hobbies = st.multiselect("Hobbies", ["Reading", "Sports", "Music", "Traveling"])

# Weight
weight = st.number_input("Weight (kg)", min_value=0.0, step=0.1)

# Height
height = st.number_input("Height (cm)", min_value=0.0, step=0.1)

# Calculate BMI
if st.button("Calculate BMI"):
    bmi = calculate_bmi(weight, height)
    st.write(f"**BMI:** {bmi:.2f}")

# Display entered details
st.subheader("Entered Details")
st.write(f"**Name:** {name}")
st.write(f"**Gender:** {gender}")
st.write(f"**Age:** {age}")
st.write(f"**Address:** {address}")
st.write(f"**Hobbies:** {', '.join(hobbies)}")
st.write(f"**Weight (kg):** {weight}")
st.write(f"**Height (cm):** {height}")
