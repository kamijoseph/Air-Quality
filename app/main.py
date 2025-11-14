
import streamlit as st
from xgboost import XGBClassifier

# page cinfiguration
st.set_page_config(
    page_title = "Air Quality Predictive System",
    page_icon = "🏭",
    layout = "wide",
    initial_sidebar_state = "expanded"
)

# styling
st.markdown("""
    <style>
    body {
        background-color: #000000 !important;
        color: #f5f5f5 !important;
    }
    .main {
        background-color: #111111;
        color: #f5f5f5;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 0 10px rgba(0,0,0,0.7);
    }
    .stButton>button {
        color: white;
        background: linear-gradient(90deg, #00b4db 0%, #0083b0 100%);
        border: none;
        border-radius: 10px;
        padding: 0.7rem 1.4rem;
        font-weight: 600;
        font-size: 1rem;
        transition: 0.3s ease;
    }
    .stButton>button:hover {
        background: linear-gradient(90deg, #0083b0 0%, #00b4db 100%);
        transform: scale(1.03);
    }
    .title-text {
        color: #ffffff;
        text-shadow: 0 0 10px #00b4db;
    }
    .description-text {
        color: #cccccc;
        font-size: 1.1rem;
        text-align: justify;
    }
    .recommend-box {
        background-color: #0d1117;
        color: #f0f0f0;
        border-left: 4px solid #00b4db;
        padding: 1.5rem;
        border-radius: 10px;
        margin-top: 1.5rem;
        font-size: 1.05rem;
    }
    </style>
""", unsafe_allow_html=True)