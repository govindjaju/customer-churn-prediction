import streamlit as st
import numpy as np
import pickle

# -------------------------
# LOAD MODEL
# -------------------------
model = pickle.load(open("model.pkl", "rb"))

# -------------------------
# TITLE
# -------------------------
st.title("Customer Churn Prediction App")

# -------------------------
# INPUT SECTION (USER-FRIENDLY)
# -------------------------

# Basic Info
gender = st.selectbox("Gender", ["Male", "Female"])
senior = st.selectbox("Senior Citizen", ["Yes", "No"])
partner = st.selectbox("Partner", ["Yes", "No"])
dependents = st.selectbox("Dependents", ["Yes", "No"])

# Account Info
tenure = st.number_input("Tenure (months)", min_value=0)
monthly_charges = st.number_input("Monthly Charges")
total_charges = st.number_input("Total Charges")

# Services
phone_service = st.selectbox("Phone Service", ["Yes", "No"])
multiple_lines = st.selectbox("Multiple Lines", ["Yes", "No", "No phone service"])
internet_service = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])

online_security = st.selectbox("Online Security", ["Yes", "No"])
online_backup = st.selectbox("Online Backup", ["Yes", "No"])
device_protection = st.selectbox("Device Protection", ["Yes", "No"])
tech_support = st.selectbox("Tech Support", ["Yes", "No"])

streaming_tv = st.selectbox("Streaming TV", ["Yes", "No"])
streaming_movies = st.selectbox("Streaming Movies", ["Yes", "No"])

# Contract Info
contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
paperless = st.selectbox("Paperless Billing", ["Yes", "No"])
payment_method = st.selectbox(
    "Payment Method",
    ["Electronic check", "Mailed check", "Bank transfer", "Credit card"]
)

# -------------------------
# PREDICTION BUTTON
# -------------------------
if st.button("Predict"):

    # -------------------------
    # ENCODING (MATCH TRAINING)
    # -------------------------
    gender = 1 if gender == "Male" else 0
    senior = 1 if senior == "Yes" else 0
    partner = 1 if partner == "Yes" else 0
    dependents = 1 if dependents == "Yes" else 0

    phone_service = 1 if phone_service == "Yes" else 0

    multiple_lines = 0 if multiple_lines == "No" else (1 if multiple_lines == "Yes" else 2)

    internet_service = {"DSL": 0, "Fiber optic": 1, "No": 2}[internet_service]

    online_security = 1 if online_security == "Yes" else 0
    online_backup = 1 if online_backup == "Yes" else 0
    device_protection = 1 if device_protection == "Yes" else 0
    tech_support = 1 if tech_support == "Yes" else 0

    streaming_tv = 1 if streaming_tv == "Yes" else 0
    streaming_movies = 1 if streaming_movies == "Yes" else 0

    contract = {"Month-to-month": 0, "One year": 1, "Two year": 2}[contract]

    paperless = 1 if paperless == "Yes" else 0

    payment_method = {
        "Electronic check": 0,
        "Mailed check": 1,
        "Bank transfer": 2,
        "Credit card": 3
    }[payment_method]

    # -------------------------
    # FINAL INPUT ARRAY (19 FEATURES)
    # -------------------------
    input_data = np.array([[gender, senior, partner, dependents,
                            tenure, monthly_charges, total_charges,
                            phone_service, multiple_lines, internet_service,
                            online_security, online_backup, device_protection,
                            tech_support, streaming_tv, streaming_movies,
                            contract, paperless, payment_method]])

    # -------------------------
    # MODEL PREDICTION
    # -------------------------
    prediction = model.predict(input_data)

    # -------------------------
    # OUTPUT
    # -------------------------
    if prediction[0] == 1:
        st.error("Customer will CHURN ❌")
    else:
        st.success("Customer will NOT CHURN ✅")