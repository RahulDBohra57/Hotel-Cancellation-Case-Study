import numpy as np
import pandas as pd
import streamlit as st 
import joblib

# Lets load all the instances required over here
with open('transformer.joblib','rb') as file:
    transformer = joblib.load(file)
    
# Lets load the model
with open('final_model.joblib','rb') as file:
    model = joblib.load(file)

st.title('INN HOTEL GROUP')
st.header(':blue[This application will predict the chances of booking cancellation]')

# Lets Take input from the user
amnth = st.slider('Select your month of arrival.',min_value=1,max_value=12,step=1)
wkd_lambda = (lambda x: 0 if x == 'Monday' else 
              1 if x =='Tuesday' else 
              2 if x == 'Wednesday' else 
              3 if x == 'Thursday' else 
              4 if x == 'Friday' else 
              5 if x == 'Saturday'else 
              6)
awkd = wkd_lambda(st.selectbox('Select your weekday of arrival.',['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']))
dwkd = wkd_lambda(st.selectbox('Select your weekday of departure.',['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']))
wkend = st.number_input('Enter how many weekend nights are there in stay.',min_value=1)
wk = st.number_input('Enter how many weekday nights are there in stay.',min_value=1)
totn = wkend + wk
mkt = (lambda x: 0 if x=='Offline' else 1) (st.selectbox('How the booking is made?',['Offline','Online']))
lt = st.number_input('How many days prior the booking was made?',min_value=1)
price = st.number_input('What is average price per room.',min_value=0)
adults = st.number_input('How many adult members in booking.')
spcl = st.selectbox('Select the number of special request made.',[0,1,2,3,4,5])
park = (lambda x: 0 if x=='No' else 1)(st.selectbox('Does guest need parking space?',['Yes','No']))

# Transform the data
lt_t,price_t = transformer.transform([[lt,price]])[0]

# Create the input list
input_list = [lt_t,spcl,price_t,adults,wkend,park,wk,mkt,amnth,awkd,totn,dwkd]

# Make prediction

prediction = model.predict_proba([input_list])[:,1][0]

# Lets show the probability
if st.button('Predict'):
    st.success(f'Cancellation chances: {round(prediction,3) *100}%')