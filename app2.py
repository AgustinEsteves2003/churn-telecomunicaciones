import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Baja del servicio en empresa de telecomunicaciones", page_icon="📞")

st.title("Probabilidad de baja del servicio en empresa de telecomunicaciones")
st.markdown("Predice la probabilidad de que un cliente de una empresa de telecomunicaciones le de baja al servicio basado en características del propio cliente (busca detectar a lo que en ingles se lo conoce como *churn*).")


st.subheader("📋 Información personal del cliente")
# Input fields
tenure = st.number_input("Antiguedad como cliente activo (en años)", min_value=0, max_value=100, value=0, step=1)
MonthlyCharges = st.number_input("Tarifa mensual (en USD)", min_value=0, max_value=1000, value=60, step=1)
TotalCharges = st.number_input("Tarifa total desde que es cliente activo (en USD)", min_value=0, max_value=10000, value=2000, step=1)
gender = st.selectbox("Genero", ["Female", "Male"])
SeniorCitizen = st.selectbox("Jubilado", ["No", "Yes"])
Partner = st.selectbox("Casado/en pareja", ["No", "Yes"])
Dependents = st.selectbox("Posee dependientes", ["No", "Yes"])
Contract = st.selectbox("Contrato", ['Month-to-month', 'One year', 'Two year'])
PaperlessBilling = st.selectbox("Facturacion electronica", ["No", "Yes"])
PaymentMethod = st.selectbox("Metodo de pago", ['Bank transfer (automatic)', 'Credit card (automatic)', 'Electronic check', 'Mailed check'])

st.markdown("---")
st.subheader("📡📞 Servicios contratados")
PhoneService = st.selectbox("Phone Service", ["No", "Yes"])
MultipleLines = st.selectbox("Multiple Lines", ["No", 'No phone service', "Yes"])
InternetService = st.selectbox("Internet Service", ['DSL', 'Fiber optic', "No"])
OnlineSecurity = st.selectbox("Online Security", ["No", 'No internet service', "Yes"])
OnlineBackup = st.selectbox("Online Backup", ["No", 'No internet service', "Yes"])
DeviceProtection = st.selectbox("Device Protection", ["No", 'No internet service', "Yes"])
TechSupport = st.selectbox("Tech Support", ["No", 'No internet service', "Yes"])
StreamingTV = st.selectbox("Streaming TV", ["No", 'No internet service', "Yes"])
StreamingMovies = st.selectbox("Streaming Movies", ["No", 'No internet service', "Yes"])


model = joblib.load(r'C:\Users\agust\Downloads\xgb_telco_grid.joblib')

# Expected features (from your training)
FEATURES = ['tenure', 'MonthlyCharges', 'TotalCharges', 'gender_Female', 'gender_Male', 'SeniorCitizen_No', 'SeniorCitizen_Yes', "Partner_No", "Partner_Yes", "Dependents_No", "Dependents_Yes",
            "PhoneService_No", "PhoneService_Yes", "MultipleLines_No", "MultipleLines_No phone service", "MultipleLines_Yes", "InternetService_DSL", "InternetService_Fiber optic", "InternetService_No",
            "OnlineSecurity_No", "OnlineSecurity_No internet service", "OnlineSecurity_Yes", "OnlineBackup_No", "OnlineBackup_No internet service", "OnlineBackup_Yes", "DeviceProtection_No",
            "DeviceProtection_No internet service", "DeviceProtection_Yes", "TechSupport_No", "TechSupport_No internet service", "TechSupport_Yes", "StreamingTV_No", "StreamingTV_No internet service",
            "StreamingTV_Yes", "StreamingMovies_No", "StreamingMovies_No internet service", "StreamingMovies_Yes", "Contract_Month-to-month", "Contract_One year", "Contract_Two year", "PaperlessBilling_No",
            "PaperlessBilling_Yes", "PaymentMethod_Bank transfer (automatic)", "PaymentMethod_Credit card (automatic)", "PaymentMethod_Electronic check", "PaymentMethod_Mailed check"]

def predict_churn(gender, SeniorCitizen, Partner, Dependents, tenure, PhoneService, MultipleLines, InternetService, OnlineSecurity, OnlineBackup,
                  DeviceProtection, TechSupport, StreamingTV, StreamingMovies, Contract, PaperlessBilling, PaymentMethod, MonthlyCharges, TotalCharges):
    # Create input data
    data = {
        'tenure': tenure, 'MonthlyCharges': MonthlyCharges, 'TotalCharges': TotalCharges,
        'gender_Female': 1 if gender == 'Female' else 0,
        'gender_Male': 1 if gender == 'Male' else 0,
        'SeniorCitizen_No': 1 if SeniorCitizen == 'No' else 0,
        'SeniorCitizen_Yes': 1 if SeniorCitizen == 'Yes' else 0,
        'Partner_No': 1 if Partner == 'No' else 0,
        'Partner_Yes': 1 if Partner == 'Yes' else 0,
        'Dependents_No': 1 if Dependents == 'No' else 0,
        'Dependents_Yes': 1 if Dependents == 'Yes' else 0,
        'PhoneService_No': 1 if PhoneService == 'No' else 0,
        'PhoneService_Yes': 1 if PhoneService == 'Yes' else 0,
        'MultipleLines_No': 1 if MultipleLines == 'No' else 0,
        'MultipleLines_No phone service': 1 if MultipleLines == 'No phone service' else 0,
        'MultipleLines_Yes': 1 if MultipleLines == 'Yes' else 0,
        'InternetService_DSL': 1 if InternetService == 'DSL' else 0,
        'InternetService_Fiber optic': 1 if InternetService == 'Fiber optic' else 0,
        'InternetService_No': 1 if InternetService == 'No' else 0,
        'OnlineSecurity_No': 1 if OnlineSecurity == 'No' else 0,
        'OnlineSecurity_No internet service': 1 if OnlineSecurity == 'No internet service' else 0,
        "OnlineSecurity_Yes": 1 if OnlineSecurity == 'Yes' else 0,
        'OnlineBackup_No': 1 if OnlineBackup == 'No' else 0,
        'OnlineBackup_No internet service': 1 if OnlineBackup == 'No internet service' else 0,
        'OnlineBackup_Yes': 1 if OnlineBackup == 'Yes' else 0,
        'DeviceProtection_No': 1 if DeviceProtection == 'No' else 0,
        'DeviceProtection_No internet service': 1 if DeviceProtection == 'No internet service' else 0,
        'DeviceProtection_Yes': 1 if DeviceProtection == 'Yes' else 0,
        'TechSupport_No': 1 if TechSupport == 'No' else 0,
        'TechSupport_No internet service': 1 if TechSupport == 'No internet service' else 0,
        'TechSupport_Yes': 1 if TechSupport == 'Yes' else 0,
        'StreamingTV_No': 1 if StreamingTV == 'No' else 0,
        'StreamingTV_No internet service': 1 if StreamingTV == 'No internet service' else 0,
        "StreamingTV_Yes": 1 if StreamingTV == 'Yes' else 0,
        'StreamingMovies_No': 1 if StreamingMovies == 'No' else 0,
        'StreamingMovies_No internet service': 1 if StreamingMovies == 'No internet service' else 0,
        'StreamingMovies_Yes': 1 if StreamingMovies == 'Yes' else 0,
        'Contract_Month-to-month': 1 if Contract == 'Month-to-month' else 0,
        'Contract_One year': 1 if Contract == 'One year' else 0,
        'Contract_Two year': 1 if Contract == 'Two year' else 0,
        'PaperlessBilling_No': 1 if PaperlessBilling == 'No' else 0,
        'PaperlessBilling_Yes': 1 if PaperlessBilling == 'Yes' else 0,
        'PaymentMethod_Bank transfer (automatic)': 1 if PaymentMethod == 'Bank transfer (automatic)' else 0,
        'PaymentMethod_Credit card (automatic)': 1 if PaymentMethod == 'Credit card (automatic)' else 0,
        'PaymentMethod_Electronic check': 1 if PaymentMethod == 'Electronic check' else 0,
        'PaymentMethod_Mailed check': 1 if PaymentMethod == 'Mailed check' else 0
    }

    df = pd.DataFrame([data])[FEATURES]
    prediction = model.predict(df)[0]
    probability = model.predict_proba(df)[0][1]

    return "churn" if prediction == 1 else "no churn", f"{probability*100:.1f}%"

if st.button("Predict"):
    prediction, probability = predict_churn(gender, SeniorCitizen, Partner, Dependents, tenure, PhoneService, MultipleLines, InternetService, OnlineSecurity, OnlineBackup,
                  DeviceProtection, TechSupport, StreamingTV, StreamingMovies, Contract, PaperlessBilling, PaymentMethod, MonthlyCharges, TotalCharges)

    if prediction == "churn":
        st.error(f"❌ El cliente dara de baja del servicio (Churn probability: {probability})")
    else:
        st.success(f"✅ El cliente permanecera en el servicio (Churn probability: {probability})")

    st.text("Creado por Agustin Esteves.")
    st.write("[LinkedIn](https://www.linkedin.com/in/agustin-esteves-0617b22b4/)")