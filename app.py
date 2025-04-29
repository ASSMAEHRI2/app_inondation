
import streamlit as st
import pandas as pd
import joblib

# Chargement du modèle
model = joblib.load("model_inondation.pkl")

st.title("🌧️ Prédiction du Risque d'Inondation")

st.markdown("Entrez les paramètres du réseau et de l’environnement :")

# Formulaire des variables d'entrée
x1 = st.number_input("Hauteur de la pluie (mm)", min_value=0.0)
x2 = st.number_input("Débit (L/s)", min_value=0.0)
x3 = st.number_input("Diamètre du conduit (mm)", min_value=0.0)
x4 = st.number_input("Pente (%)", min_value=0.0)
x5 = st.number_input("Taux d’occupation du sol (%)", min_value=0.0)

if st.button("Prédire"):
    input_data = pd.DataFrame([[x1, x2, x3, x4, x5]], columns=["pluie", "debit", "diametre", "pente", "occupation"])
    prediction = model.predict(input_data)[0]
    risque = "🚨 Risque d'inondation" if prediction == 1 else "✅ Pas de risque"
    st.success(risque)
