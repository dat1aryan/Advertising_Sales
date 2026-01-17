import streamlit as st
import pickle
import numpy as np

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Sales Prediction",
    page_icon="📈",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ---------------- CUSTOM DARK THEME ----------------
st.markdown("""
    <style>
        body {
            background-color: #0e1117;
            color: #ffffff;
        }
        .main {
            background-color: #0e1117;
        }
        h1, h2, h3 {
            color: #ffffff;
        }
        .card {
            background: #161b22;
            padding: 25px;
            border-radius: 15px;
            margin-bottom: 20px;
            box-shadow: 0 0 15px rgba(0,0,0,0.4);
        }
        .prediction {
            font-size: 32px;
            font-weight: bold;
            color: #00ffcc;
            text-align: center;
        }
        footer {
            visibility: hidden;
        }
    </style>
""", unsafe_allow_html=True)

# ---------------- LOAD MODEL ----------------
with open("hr.pkl", "rb") as file:
    model = pickle.load(file)

# ---------------- TITLE ----------------
st.markdown("<h1 style='text-align: center;'>📊 Advertising Sales Predictor</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #9ba3af;'>Machine Learning Powered Sales Estimation</p>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ---------------- INPUT CARD ----------------
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.markdown("<h3>Enter Advertising Budget</h3>", unsafe_allow_html=True)

tv = st.slider("📺 TV Budget", 0.0, 300.0, 100.0)
radio = st.slider("📻 Radio Budget", 0.0, 50.0, 20.0)
newspaper = st.slider("📰 Newspaper Budget", 0.0, 120.0, 30.0)

st.markdown("</div>", unsafe_allow_html=True)

# ---------------- PREDICTION CARD ----------------
st.markdown("<div class='card'>", unsafe_allow_html=True)

if st.button("🚀 Predict Sales", use_container_width=True):
    input_data = np.array([[tv, radio, newspaper]])
    prediction = model.predict(input_data)

    st.markdown(
        f"<div class='prediction'>Predicted Sales<br>{prediction[0]:.2f}</div>",
        unsafe_allow_html=True
    )

st.markdown("</div>", unsafe_allow_html=True)

# ---------------- FOOTER ----------------
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown(
    "<p style='text-align:center; color:#6b7280;'>Built by Aryan Pankaj Kumar</p>",
    unsafe_allow_html=True
)
