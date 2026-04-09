import streamlit as st
import numpy as np
import pickle

# Load model
import os
import pickle

model_path = os.path.join(os.path.dirname(__file__), "model.pkl")

with open(model_path, "rb") as f:
    model = pickle.load(f)
# Page config
st.set_page_config(page_title="Smart Crop Advisor", layout="wide")

# Custom CSS (🔥 premium look)
st.markdown("""
    <style>
    .main {
        background-color: #f5f7fa;
    }
    .title {
        font-size: 40px;
        font-weight: bold;
        color: #2c7a7b;
        text-align: center;
    }
    .card {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<p class="title">🌾 Smart Crop Recommendation System</p>', unsafe_allow_html=True)

st.write("### Enter Soil & Environmental Conditions")

# Layout (2 columns)
col1, col2 = st.columns(2)

with col1:
    N = st.slider("Nitrogen (N)", 0, 140, 50)
    P = st.slider("Phosphorus (P)", 0, 140, 40)
    K = st.slider("Potassium (K)", 0, 200, 40)
    ph = st.slider("pH Value", 0.0, 14.0, 6.5)

with col2:
    temperature = st.slider("Temperature (°C)", 0.0, 50.0, 25.0)
    humidity = st.slider("Humidity (%)", 0.0, 100.0, 80.0)
    rainfall = st.slider("Rainfall (mm)", 0.0, 300.0, 200.0)

# Button
if st.button("🌱 Predict Crop"):
    input_data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
    prediction = model.predict(input_data)[0]

    st.success(f"✅ Recommended Crop: **{prediction.upper()}**")

    # Advisory section
    st.markdown("## 🌿 Agricultural Advisory")

    if prediction == "rice":
        st.info("💧 High water requirement | Use nitrogen fertilizers")
    elif prediction == "maize":
        st.info("🌾 Moderate irrigation | Balanced NPK fertilizers")
    elif prediction == "cotton":
        st.info("🌱 Needs warm climate | Use potassium-rich fertilizers")
    else:
        st.info("🌿 Follow balanced fertilization and proper irrigation")

# Footer
st.markdown("---")
st.caption("Built using Machine Learning 🌱 | Smart Farming Solution")