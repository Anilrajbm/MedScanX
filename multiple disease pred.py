# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 13:55:45 2023

@author: hp
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# Loading the saved model

diabetes_model=pickle.load(open('diabetes_model.sav','rb'))

heart_model=pickle.load(open('heart_model.sav','rb'))

parkinsins_model=pickle.load(open('parkinsins_model.sav','rb'))


# SideBar for navigation

with st.sidebar:
    
    selected= option_menu('Multiple Disease Prediction System',
                          ['Diabetes Prediction',
                           'Heart Disease Prediction',
                           'Parkinsons Prediction'],
                          
                           icons = ['activity','heart','person'],
                           
                           default_index=0 )
    

# Diabetes prediction page

if(selected== 'Diabetes Prediction'):
    
    #page title
    st.title('Diabetes Prediction using ML')
    
    #Getting the Input Data from user
    #Colums for input fileds
    
    col1,col2,col3=st.columns(3)
    
    with col1:
        Pregnancies=st.text_input('Number of Pregnancies')
    with col2:
         Glucose=st.text_input('Glucose Level')
    with col3:
        BlooadPressure=st.text_input('Blood Pressure value')
    with col1:
        SkinThickness=st.text_input('Skin Thickness value')
    with col2:
        Insulin=st.text_input('Insulin Level')
    with col3:
        BMI=st.text_input('BMI value')
    with col1:
        DiabetesPedigreeFunction=st.text_input('Diabetes Pedigree Function value')
    with col2:
        Age=st.text_input('Age of the Person')
   
    
   
    
    
    #code for Prediction
    diab_dignosis= ''
    
    # Creating the button for prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction=diabetes_model.predict([[Pregnancies,Glucose,BlooadPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
        
        if(diab_prediction[0]==1):
            diab_dignosis='The Person is Diabetic'
        else:
            diab_dignosis='The Person is Not Diabetic'
            
   
    
    st.success(diab_dignosis)

    
    
if(selected=='Heart Disease Prediction'):
    
    #page ttitle
    st.title('Heart Disease Prediction using ML')
    
    
    #Getting the Input Data from user
    #Colums for input fileds
    
    col1,col2,col3,col4=st.columns(4)
    
    with col1:
        age=st.text_input('Age of Person')
    with col2:
         sex=st.text_input('Sex')
    with col3:
        cp=st.text_input('Chest Pain types')
    with col4:
        trestbps=st.text_input('Resting Blooad Pressure')
    with col1:
        chol=st.text_input('Serum Cholestoral in mg/dl')
    with col2:
        fbs=st.text_input('FBS>120 mg/dl')
    with col3:
        restecg=st.text_input('Resting ECG results')
    with col4:
        thalach=st.text_input('Maximum heart rate')
    with col1:
           exang=st.text_input('Exercise induced angina')
    with col2:
           oldpeak=st.text_input('ST depression peak')
    with col3:
            slope=st.text_input('Peak of exercise ST segment')
    with col4:
            ca=st.text_input('No of major vessels(0-3)')
    with col1:
           thal=st.text_input('Enter the Thal Value')
    
    
   
    
    
    #code for Prediction
    heart_dignosis= ''
    
    # Creating the button for prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction=heart_model.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
        
        if(heart_prediction[0]==1):
            heart_dignosis='The Person is having Heart Disease'
        else:
           heart_dignosis='The Person is Not having Heart Disease'
            
   
    
    st.success(heart_dignosis)

    
if(selected=='Parkinsons Prediction'):
    
    #page title
    st.title('Parkinsons Predction using ML')
    
    #Getting the Input Data from user
    #Colums for input fileds
    
    col1,col2,col3,col4,col5=st.columns(5)
    
    with col1:
        MDVP_Fo=st.text_input(' MDVP_Fo(Hz)')
    with col2:
         MDVP_Fhi=st.text_input('MDVP_Fhi(Hz)')
    with col3:
       MDVP_Flo=st.text_input('MDVP_Flo(Hz)')
    with col4:
        MDVP_Jitter=st.text_input('MDVP_Jitter(%)')
    with col5:
       MDVP_JitterABS=st.text_input('MDVP_Jitter(Abs)')
    with col1:
        MDVP_RAP=st.text_input(' MDVP_RAP')
    with col2:
        MDVP_PPQ=st.text_input(' MDVP_PPQ')
    with col3:
       Jitter_DDP=st.text_input(' Jitter_DDP')
    with col4:
         MDVP_Shimmer=st.text_input(' MDVP_Shimmer')
    with col5:
        MDVP_ShimmerDB=st.text_input('MDVP_Shimmer(dB)')
    with col1:
        Shimmer_APQ3=st.text_input('Shimmer_APQ3')
    with col2:
       Shimmer_APQ5 =st.text_input(' Shimmer_APQ5')
    with col3:
         MDVP_APQ=st.text_input(' MDVP_APQ')
    with col4:
         Shimmer_DDA=st.text_input(' Shimmer_DDA')
    with col5:
         NHR=st.text_input('NHR')
    with col1:
         HNR=st.text_input('HNR')
    with col2:
         RPDE=st.text_input('RPDE')
    with col3:
         DFA=st.text_input('DFA')
    with col4:
         spread1=st.text_input('spread1')
    with col5:
         spread2=st.text_input('spread2')
    with col1:
         D2=st.text_input('D2')
    with col2:
         PPE=st.text_input('PPE')
    
    
   
    
    
    #code for Prediction
    par_dignosis= ''
    
    # Creating the button for prediction
    
    if st.button('Parkinsons Disease Test Result'):
        par_prediction=parkinsins_model.predict([[ MDVP_Fo, MDVP_Fhi,MDVP_Flo,MDVP_Jitter, MDVP_JitterABS, MDVP_RAP,MDVP_PPQ,Jitter_DDP,MDVP_Shimmer,MDVP_ShimmerDB,Shimmer_APQ3,Shimmer_APQ5,MDVP_APQ,Shimmer_DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])
        
        if(par_prediction[0]==1):
            par_dignosis='The Person is having Parkinsons Disease'
        else:
           par_dignosis='The Person is Not having Parkinsons Disease'
            
   
    
    st.success(par_dignosis)
    
    