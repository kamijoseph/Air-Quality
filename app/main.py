
import streamlit as st
import numpy as np
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

# loading the model
@st.cache_resource
def load_xgb_model():
    model = XGBClassifier()
    model.load_model("app/../resources/air_model.json")
    return model

model = load_xgb_model()

# header
st.markdown("<h1 class='title-text'>🏭 AIR QUALITY PREDICTION SYSTEM.</h1>", unsafe_allow_html=True)
st.markdown("<p class='description-text'>This intelligent system predicts <b>AIR QUALITY</b> and provides air quality pollution severeness. Enter your DATA in the sidebar to begin.</p>", unsafe_allow_html=True)

st.markdown("---")

# user inputs
st.sidebar.header("🍃 Input the DATA")

# temperature input
temperature = st.sidebar.slider(
    "Temperature(°C)",
    min_value = -50.0,
    max_value = 100.0,
    value = 25.0,
    step = 0.1
)

# humidity input
humidity = st.sidebar.number_input(
    "Humidity (%)",
    min_value = 0.0,
    max_value = 200.0,
    value = 50.0,
    step = 10.0
)

# PM2.5
pm25 = st.sidebar.number_input(
    "PM2.5 (µg/m³)",
    min_value = 0.0,
    max_value = 1000.0,
    value = 40.0,
    step = 10.0
)

# no2
no2 = st.sidebar.slider(
    "NO₂ (µg/m³)",
    min_value = 0.0,
    max_value = 1000.0,
    value = 40.0,
    step = 0.1
)

# so2
so2 = st.sidebar.slider(
    "SO₂ (µg/m³)",
    min_value = 0.0,
    max_value = 1000.0,
    value = 60.0,
    step = 0.1
)

# CO
co = st.sidebar.slider(
    "CO (mg/m³)",
    min_value = 0.0,
    max_value = 50.0,
    value = 10.0,
    step = 0.1
)

# proximity to an industry area
proximity_industry = st.sidebar.number_input(
    "Proximity to Industrial Areas (km)",
    min_value=0.0,
    max_value=50.0,
    value=5.0,
    step=0.1
)

# population density
population_density = st.sidebar.number_input(
    "Population Density (people/km²)",
    min_value=0,
    max_value=100000,
    value=1000,
    step=10
)

# inputs preprocessing
input_data = np.array([
    temperature, humidity, pm25, no2, so2, co, proximity_industry, population_density
]).reshape(1, -1)

# image and button
col1, col2 = st.columns([2, 1])
with col2:
    st.image(
        "app/../resources/action.png",
        caption = "good air, great health",
        use_container_width=True,
    )

with col1:
    predict_button = st.button("🌫 PREDICTIONS 🏭")

    st.markdown("<br>", unsafe_allow_html=True)

    st.image(
        "app/../resources/air_quality.jpg",
        caption = "the bliss of pure air",
        use_container_width = True
    )