import streamlit as st
import numpy as np
import pickle
import matplotlib.pyplot as plt

# Load trained model
model = pickle.load(open("model.pkl", "rb"))

# Page config
st.set_page_config(page_title="Customer Churn Prediction", page_icon="📊")

st.title("📊 Customer Churn Prediction App")
st.write("Enter all customer details below:")

# -----------------------------
# 🔹 INPUT FIELDS (19 FEATURES)
# -----------------------------

# Basic customer info
gender = st.selectbox("Gender", [0, 1])
senior_citizen = st.selectbox("Senior Citizen", [0, 1])
partner = st.selectbox("Partner", [0, 1])
dependents = st.selectbox("Dependents", [0, 1])

tenure = st.number_input("Tenure")

# Services
phone_service = st.selectbox("Phone Service", [0, 1])
multiple_lines = st.selectbox("Multiple Lines", [0, 1])

internet_service = st.selectbox("Internet Service", [0, 1, 2])
online_security = st.selectbox("Online Security", [0, 1])
online_backup = st.selectbox("Online Backup", [0, 1])
device_protection = st.selectbox("Device Protection", [0, 1])
tech_support = st.selectbox("Tech Support", [0, 1])
streaming_tv = st.selectbox("Streaming TV", [0, 1])
streaming_movies = st.selectbox("Streaming Movies", [0, 1])

# Billing info
contract = st.selectbox("Contract", [0, 1, 2])
paperless_billing = st.selectbox("Paperless Billing", [0, 1])
payment_method = st.selectbox("Payment Method", [0, 1, 2, 3])

monthly_charges = st.number_input("Monthly Charges")
total_charges = st.number_input("Total Charges")

# -----------------------------
# 🔮 PREDICTION
# -----------------------------

if st.button("Predict Churn"):

    input_data = np.array([[
        gender,
        senior_citizen,
        partner,
        dependents,
        tenure,
        phone_service,
        multiple_lines,
        internet_service,
        online_security,
        online_backup,
        device_protection,
        tech_support,
        streaming_tv,
        streaming_movies,
        contract,
        paperless_billing,
        payment_method,
        monthly_charges,
        total_charges
    ]])

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("⚠ Customer WILL CHURN")
    else:
        st.success("✔ Customer will NOT CHURN")

# -----------------------------
# 📊 SIMPLE VISUALIZATION
# -----------------------------

st.subheader("Sample Churn Distribution")

fig, ax = plt.subplots()
ax.bar(["No Churn", "Churn"], [80, 20])
st.pyplot(fig)