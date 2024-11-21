# **Bengaluru House Price Prediction App** 🏡  
This repository contains a **Streamlit-based web application** that predicts house prices in Bengaluru using a machine learning model trained on real estate data.

## **Features**  
- **Interactive UI**:  
  Predict house prices by entering:  
  - Location  
  - Area (sqft)  
  - Number of bathrooms  
  - Bedrooms (BHK)  

- **Machine Learning Model**:  
  A trained **Linear Regression model** ensures accurate price prediction.

- **Data Preprocessing**:  
  Includes outlier removal for better prediction accuracy.

- **Dynamic Handling**:  
  Supports **200+ Bengaluru locations** for predictions.

- **Real-Time Results**:  
  Instantly calculates prices in **Lakhs (₹)**.

## **Technologies Used**  
- **Python**: For data processing and model development.  
- **Streamlit**: Web application framework to create an interactive UI.  
- **scikit-learn**: Used to build the machine learning model.  
- **Pandas & NumPy**: For data preprocessing and manipulation.  

## **Project Structure**  
bengaluru-house-price-prediction/
│
├── app.py                     # Streamlit app script
├── bangalore_home_prices_model.pickle # Trained Linear Regression model
├── columns.json               # Metadata for location columns
├── requirements.txt           # Project dependencies
├── Bengaluru_House_Data.csv   # Dataset used for training the model
├── model.py                   # Script for model building and training
└──requirements.txt
└── README.md                  # Project documentation


### **Getting Started**  
1. Clone the repository:  
   ```bash
   git clone https://github.com/your-repo/bengaluru-house-price-prediction.git
   cd bengaluru-house-price-prediction
   ```

2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Streamlit app:  
   ```bash
   streamlit run app.py
   ```

---

## **Usage**  
- Open the app in your browser.  
- Input location, area (sqft), BHK, and bathrooms.  
- Click **Predict Price** to get the house price in Lakhs (₹).

---

## **Future Enhancements**  
- Add more advanced models (e.g., Random Forest, Gradient Boosting).  
- Incorporate additional features like amenities and distance to major landmarks.  
- Expand dataset to include other cities for multi-city predictions.  

