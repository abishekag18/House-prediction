import streamlit as st
import pickle
import numpy as np

# Load model
with open("model_pickle.pkl", "rb") as f:
    model = pickle.load(f)

st.title("🏠 House Price Prediction")

st.write("Enter the house details")

area = st.number_input("Area (sq ft)", min_value=100)
bedrooms = st.number_input("Bedrooms", min_value=1)
bathrooms = st.number_input("Bathrooms", min_value=1)

if st.button("Predict Price"):

    data = np.array([[area, bedrooms, bathrooms]])

    prediction = model.predict(data)

    st.success(f"Predicted Price: {prediction[0]:,.2f}")
    
