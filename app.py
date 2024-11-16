import streamlit as st
import pickle
import json
import numpy as np

# Load the model
with open('bangalore_home_prices_model.pickle', 'rb') as f:
    model = pickle.load(f)

# Load the columns
with open("columns.json", "r") as f:
    data_columns = json.load(f)['data_columns']

# Function to predict prices
def predict_price(location, sqft, bath, bhk):
    loc_index = np.where(np.array(data_columns) == location.lower())[0][0] if location.lower() in data_columns else -1
    x = np.zeros(len(data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1
    return model.predict([x])[0]

# Streamlit UI
st.title("Bengaluru House Price Prediction")

# Input fields
locations = [col for col in data_columns[3:]]  # Skip 'sqft', 'bath', 'bhk'
selected_location = st.selectbox("Select Location", locations)
sqft = st.number_input("Enter Total Square Feet Area", min_value=0, value=1000)
bath = st.number_input("Enter Number of Bathrooms", min_value=1, max_value=10, value=2)
bhk = st.number_input("Enter Number of BHK", min_value=1, max_value=10, value=2)

# Prediction button
if st.button("Predict"):
    price = predict_price(selected_location, sqft, bath, bhk)
    st.success(f"Estimated Price: ₹ {price:.2f} Lakhs")
