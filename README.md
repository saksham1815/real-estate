Bengaluru House Price Prediction App 🏡
This repository contains a Streamlit-based web application that predicts house prices in Bengaluru using a machine learning model trained on real estate data.

Features
Interactive UI: Predict house prices by entering location, area (sqft), number of bathrooms, and bedrooms (BHK).
Machine Learning Model: Uses a trained Linear Regression model for accurate price prediction.
Data Preprocessing:
Outlier removal for better predictions.
Dynamic handling of over 200+ Bengaluru locations.
Real-Time Results: Instantly calculate prices in Lakhs (₹).
Technologies Used
Python: Data processing and model development.
Streamlit: Web application framework for creating interactive UI.
scikit-learn: Machine learning model.
Pandas & NumPy: Data preprocessing and manipulation.
Setup Instructions
Clone the repository:
bash
Copy code
git clone https://github.com/yourusername/bengaluru-house-price-prediction.git
Navigate to the project folder:
bash
Copy code
cd bengaluru-house-price-prediction
Install dependencies:
bash
Copy code
pip install -r requirements.txt
Run the app locally:
bash
Copy code
streamlit run app.py
Project Structure
python
Copy code
bengaluru-house-price-prediction/
│
├── app.py                # Streamlit app script
├── bangalore_home_prices_model.pickle  # Trained machine learning model
├── columns.json          # Metadata for location columns
├── requirements.txt      # List of dependencies
├── Bengaluru_House_Data.csv (Optional) # Dataset (if provided)
└── README.md             # Project description
