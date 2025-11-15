import streamlit as st 

st.title('CALCULATE YOUR BMI')
wt = st.number_input('Enter your weight in KGs:')
ht = st.number_input('Enter your height in Ms:')
if ht==0:
    bmi = 0
else:
    bmi = wt/ht**2
st.success(f'Your BMI is {round(bmi,2)}kg/m^2')