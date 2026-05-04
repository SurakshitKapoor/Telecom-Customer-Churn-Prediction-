import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/predict-batch"

st.title("Telecom Company Customer Churn Prediction App")
st.subheader("Enter Customer Details")


# ---------------- Inputs fields ---------------- #

Gender = st.selectbox("Gender", ["Female", "Male"])

SeniorCitizen = st.selectbox("Senior Citizen", [0, 1])

Partner = st.selectbox("Partner", ["Yes", "No"])

Dependents = st.selectbox("Dependents", ["No", "Yes"])

PhoneService = st.selectbox("Phone Service", ["No", "Yes"])

MultipleLines = st.selectbox("Multiple Lines", ["No", "Yes"])

InternetService = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])

OnlineSecurity = st.selectbox("Online Security", ["No", "Yes"])

OnlineBackup = st.selectbox("Online Backup", ["Yes", "No"])

DeviceProtection = st.selectbox("Device Protection", ["No", "Yes"])

TechSupport = st.selectbox("Tech Support", ["No", "Yes"])

StreamingTV = st.selectbox("Streaming TV", ["No", "Yes"])

StreamingMovies = st.selectbox("Streaming Movies", ["No", "Yes"])

Contract = st.selectbox("Contract", ["Monthly", "One year", "Two year"])

PaperlessBilling = st.selectbox("Paperless Billing", ["Yes", "No"])

PaymentMethod = st.selectbox(
    "Payment Method",
    [
        "Manual",
        "Bank transfer (automatic)",
        "Credit card (automatic)"
    ]
)


# ---------------- NUMERICAL FEATURES ---------------- #

Tenure = st.number_input("Tenure", min_value=0, max_value=100, value=1)

MonthlyCharges = st.number_input("Monthly Charges", min_value=0.0)

TotalCharges = st.number_input("Total Charges", min_value=0.0)


# ---------------- API CALL ---------------- #

if st.button("Predict Churn"):

    data = {
        "Gender": Gender,
        "SeniorCitizen": SeniorCitizen,
        "Partner": Partner,
        "Dependents": Dependents,
        "Tenure": Tenure,
        "PhoneService": PhoneService,
        "MultipleLines": MultipleLines,
        "InternetService": InternetService,
        "OnlineSecurity": OnlineSecurity,
        "OnlineBackup": OnlineBackup,
        "DeviceProtection": DeviceProtection,
        "TechSupport": TechSupport,
        "StreamingTV": StreamingTV,
        "StreamingMovies": StreamingMovies,
        "Contract": Contract,
        "PaperlessBilling": PaperlessBilling,
        "PaymentMethod": PaymentMethod,
        "MonthlyCharges": MonthlyCharges,
        "TotalCharges": TotalCharges
    }

    payload = {"inputs": [data]}

    response = requests.post(API_URL, json=payload)

    if response.status_code == 200:
        result = response.json()

        st.success("Prediction Completed")

        preds = result["predictions"]

        for i, p in enumerate(preds):

            if p == 1:
                label = "🔴 Customer WILL CHURN"
            else:
                label = "🟢 Customer will NOT CHURN"

            st.write(f"Customer {i+1}: {label}")

    else:
        st.error("API Error")