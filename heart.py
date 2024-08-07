import numpy as np 
import pandas as pd 
import streamlit as st 
import pickle as pk 
  

loaded_model = pk.load(open('C:/Users/shekhar suman/Desktop/projectML/Deploying machine learning/heart_model/model.pkl','rb'))


heart_data = pd.read_csv("C:/Users/shekhar suman/Desktop/Class notes/pandas/Dataset1/heart_disease.csv")


st.header('Heart Disease Predictor')

gender = st.selectbox('Choose Gender',heart_data['Gender'].unique())

if gender == 'Male':
    gen = 1 
else:
    gen = 0

age = st.slider('Enter your age',0,120)   
currentSmoker = st.number_input('Is patient  currentSmoker') 
cigsPerDay = st.slider(' cigsPerDay consumption',0,50) 
BPMeds = st.number_input('Is patient on  BPMeds') 
prevalentStroke = st.number_input(' Is patient had stroke') 
prevalentHyp = st.number_input('Enter prevalentHyp status') 
diabetes = st.number_input('Enter diabetes status') 
totChol = st.slider('Enter  totChol',50,500) 
sysBP = st.slider('Enter  sysBP',50,500) 
diaBP = st.slider('Enter  diaBP',20,300) 
BMI = st.slider('Enter  BMI',10,100) 
heartRate = st.slider('Enter  heartRate',20,300) 
glucose = st.slider('Enter  glucose leval',50,400)


if st.button('Predict'):
    input = np.array([[gen,age,currentSmoker,cigsPerDay,BPMeds,prevalentStroke,prevalentHyp,diabetes,totChol,sysBP,diaBP,BMI,heartRate,glucose]])

    output = loaded_model.predict(input)

    if output[0] == 0:
        stn = "Patient is Healthy,No heart disease"
    
    else:
        stn = "Patient May have heart disease"
        
    st.markdown(stn)    

