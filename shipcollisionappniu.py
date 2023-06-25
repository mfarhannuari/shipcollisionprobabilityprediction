import pickle

import numpy as np
import streamlit as st

st.title("Ship Collision Probability Prediction app")
model = pickle.load(open("model.pkl", "rb"))

Daylight = st.number_input("Daylight (Day = 1, Night = 0)")
Inexperience = st.number_input("Inexperience (Yes = 1, No = 0)")
NumberOfCrew = st.number_input("Number Of Crew (Proper = 1, Unproper = 0)")
UnderstandingOfShipCharacteristic = st.number_input("Understanding Of Ship Characteristic (Good = 1, Bad= 0)")
UnderstandingOfWaterCondition = st.number_input("Understanding Of Water Condition (Good = 1, Bad= 0)")
DualTask = st.number_input("Dual Task (Yes = 1, No = 0)")
VisualObservation = st.number_input("Visual Observation (Good = 1, Bad= 0)")
Master = st.number_input("Master (Available = 1, Unavailable = 2")
ShipCommunication = st.number_input("Ship Communication (Good = 1, Bad= 0)")
Pilot = st.number_input("Pilot (Available = 0, Charlie = 1, Not Available = 2, Not Required = 3)")
CrewCompetence = st.number_input("Crew Competence (Good = 1, Bad= 0)")
Uncertain = st.number_input("Uncertain (Yes = 1, No = 0)")
Fatigue = st.number_input("Fatigue (Yes = 1, No = 0)")
CrewHealth = st.number_input("CrewHealth (Fit = 1, Unfit = 0)")
NavcomEquipment = st.number_input("Navcom Equipment (Proper = 1, Unproper = 0)")
NavcomUtilized = st.number_input("NavcomUtilized (Yes = 1, No = 0)")
UnderstandingofNavcomSign = st.number_input("Understanding of Navcom Sign (Good = 1, Bad= 0)")
Manuveurability = st.number_input("Manuveurability (Good = 1, Limited= 0)")
DecisionMaking = st.number_input("Decision Making (Good = 1, Bad= 0)")
SituationalAwareness = st.number_input("Situational Awareness (Good = 1, Bad= 0)")
GoodSeamanship = st.number_input("Good Seamanship (Yes = 1, No = 0)")
PreventiveTiming = st.number_input("Preventive Timing (Good = 1, Bad= 0)")
TechnicalFailure = st.number_input("Technical Failure (Yes = 1, No = 0)")
btn = st.button("predict")

if btn:
    pred = model.predict(np.array([Daylight,Inexperience,NumberOfCrew,UnderstandingOfShipCharacteristic,UnderstandingOfWaterCondition,DualTask,VisualObservation,Master,ShipCommunication,Pilot,CrewCompetence,Uncertain,Fatigue,CrewHealth,NavcomEquipment,NavcomUtilized,UnderstandingOfNavcomSign,Manuveurability,DecisionMaking,SituationalAwareness,GoodSeamanship,PreventiveTiming,TechnicalFailure]).reshape(1,-1))
    st.write(f"Your Ship will have: {pred}" )