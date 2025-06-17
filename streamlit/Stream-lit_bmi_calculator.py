"""" 
Logic: 

User input height: in feeet
User input weight: in kg

bmi formula: bmi = weight/((height*3.82)**2)
obsity levels:
    bmi < 16: Extremely Underweight  --> Error
    16 <= bmi < 18.5: Underweight  --> Warning
    18.5 <= bmi < 25: Healthy  --> Success
    25 <= bmi < 30: Overweight --> Info
    bmi >= 30: Extremely Overweight --> Error
"""

import streamlit as st

st.title("This is bmi calculator.")
st.subheader("You should enter your weight in kgs and height in feet to calculate bmi.")

weight = st.number_input("Weight: ")
height = st.number_input("Height: ")
caculate_bmi = st.button("Calculate")

if calculate_btn:
    if weight and height:
        st.success("Calculating BMI...")
        BMI = weight / ((height/3.28)**2)
        st.success(f"Your NMI is: {BMI}")
    else:
        st.error("Please eneter both height and weight.")


# meta-llama/llama-4-scout-17b-16e-instruct
# meta-llama/llama-4-scout-17b-16e-instruct
