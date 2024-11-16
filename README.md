**Bengaluru House Price Prediction App 🏡**
This repository contains a Streamlit-based web application that predicts house prices in Bengaluru using a machine learning model trained on real estate data.

**Features**
Interactive UI: Predict house prices by entering location, area (sqft), number of bathrooms, and bedrooms (BHK).
Machine Learning Model: Uses a trained Linear Regression model for accurate price prediction.
Data Preprocessing:
Outlier removal for better predictions.
Dynamic handling of over 200+ Bengaluru locations.
Real-Time Results: Instantly calculate prices in Lakhs (₹).

**Technologies Used**
Python: Data processing and model development.
Streamlit: Web application framework for creating interactive UI.
scikit-learn: Machine learning model.
Pandas & NumPy: Data preprocessing and manipulation.


**Project Structure**
bengaluru-house-price-prediction/
│
├── app.py                # Streamlit app script
├── bangalore_home_prices_model.pickle  # Trained machine learning model
├── columns.json          # Metadata for location columns
├── requirements.txt      # List of dependencies
├── Bengaluru_House_Data.csv  # Dataset 
└──model.py #model making 
└── README.md             # Project description
