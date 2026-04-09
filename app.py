import streamlit as st
import numpy as np
import pickle
import os

model = pickle.load(open(os.path.join(os.path.dirname(__file__), "model.pkl"), "rb"))

st.set_page_config(page_title="Crop Advisor", layout="centered")

st.title("🌾 Smart Crop Recommendation System")

N = st.number_input("Nitrogen", 0, 200)
P = st.number_input("Phosphorus", 0, 200)
K = st.number_input("Potassium", 0, 200)
temperature = st.number_input("Temperature", 0.0, 50.0)
humidity = st.number_input("Humidity", 0.0, 100.0)
ph = st.number_input("pH", 0.0, 14.0)
rainfall = st.number_input("Rainfall", 0.0, 300.0)

if st.button("Predict"):
    data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
    result = model.predict(data)[0]
    st.success(f"Recommended Crop: {result}")
