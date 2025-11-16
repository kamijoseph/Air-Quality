# **Air Quality Predictive System — Streamlit + XGBoost**

A production-ready intelligent web application for **predicting air quality categories** based on environmental and pollutant data.
The system uses a trained **XGBoost classifier**, integrates an interactive **Streamlit UI**, and provides **interpretable feedback** to guide users on atmospheric conditions and pollution severity.

Dataset used:
**Kaggle — Air Quality and Pollution Assessment**
[https://www.kaggle.com/datasets/mujtabamatin/air-quality-and-pollution-assessment](https://www.kaggle.com/datasets/mujtabamatin/air-quality-and-pollution-assessment)

---
## 🚀 Live Demo

Experience the app in action here:  
👉 [Air Quality Predictive System (Live Demo)](https://air-quality-webapp.streamlit.app/)

*(Click the link above to open the interactive web app.)*

---

## **📌 Key Features**

* Interactive **Streamlit web interface**
* Real-time **air quality prediction**
* Uses a trained **XGBoost (JSON-serialized) model**
* Accepts environmental inputs including:

  * Temperature
  * Humidity
  * PM2.5
  * NO₂
  * SO₂
  * CO
  * Proximity to industrial areas
  * Population density
* Clean UI with custom CSS styling
* Provides **air quality categorization**:

  * Good
  * Moderate
  * Poor
  * Hazardous
* Prints actionable descriptions for each class
* Fully customizable and extendable for future ML deployments

---

## **📂 Project Structure**

```
Air-Quality/
│
├── app/
│   ├── streamlit_app.py      # Main application script
│   ├── resources/
│   │   ├── air_model.json    # Trained XGBoost model
│   │   ├── action.png        # UI image asset
│   │   └── air_quality.jpg   # UI image asset
│
├── notebook/
│   ├── model_training.ipynb  # Training + preprocessing notebook
│
├── requirements.txt
├── README.md
└── LICENSE
```

---

## **🚀 Running the Application**

### **1. Clone the repository**

```bash
git clone https://github.com/kamijoseph/Air-Quality.git
cd Air-Quality
```

### **2. Create environment (recommended: Conda)**

```bash
conda create -n airq python=3.10 -y
conda activate airq
```

### **3. Install dependencies**

```bash
pip install -r requirements.txt
```

### **4. Run the Streamlit app**

```bash
streamlit run app/main.py
```

---

## **🧠 Model Description**

The prediction engine uses **XGBoostClassifier**, trained on the Kaggle dataset referenced above.
The model was saved in XGBoost's native **.json** format for lightweight and portable distribution.

**Input features** used for prediction:

1. Temperature (°C)
2. Humidity (%)
3. PM2.5 (µg/m³)
4. NO₂ (µg/m³)
5. SO₂ (µg/m³)
6. CO (mg/m³)
7. Proximity to Industrial Areas (km)
8. Population Density (people/km²)

**Output classes:**

| Class | Label     | Description                                |
| ----- | --------- | ------------------------------------------ |
| 0     | Good      | Clean and safe air                         |
| 1     | Hazardous | Dangerous pollution levels                 |
| 2     | Moderate  | Acceptable but may affect sensitive groups |
| 3     | Poor      | High pollution with health concerns        |

---

## **🎨 UI Overview**

The application features:

* Dark-themed interface
* Custom embedded CSS for styling
* Sidebar for inputs
* Prediction section with:

  * Air quality category
  * Short descriptive statement
  * Highlight box for interpretation


```

---

## **📊 Sample Prediction Flow**

1. User enters environmental data in the sidebar
2. Inputs are converted into a NumPy array
3. Model predicts the air quality class
4. Class is mapped to label and description
5. Results are displayed dynamically

---

## **📝 Code Reference (Main Script)**

Complete Streamlit script is located in:

```
app/streamlit_app.py
```

It contains:

* UI styling block
* Cached XGBoost model loader
* Input widgets (sliders + number inputs)
* Prediction logic
* Display components

---

## **🤝 Contributing**

Contributions are welcome.
Open a pull request with improvements or raise an issue for bugs and feature requests.

---

## **📄 License**

This project is released under the **MIT License**.

---

