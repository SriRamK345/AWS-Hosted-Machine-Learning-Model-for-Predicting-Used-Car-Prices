import streamlit as st
import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder

# Load the dataset and model only once using Streamlit's caching mechanism
@st.cache_resource
def load_model_and_data():
    df = pd.read_csv("Car DS/reqdf.csv")
    model = joblib.load("Car DS/RF_model.pkl")
    
    # Fit LabelEncoders
    le_manufacturer = LabelEncoder()
    le_fuel = LabelEncoder()
    
    le_manufacturer.fit(df["manufacturer"])
    le_fuel.fit(df["fuel"])
    
    return df, model, le_manufacturer, le_fuel

# Load resources
df, model, le_manufacturer, le_fuel = load_model_and_data()

# Define the prediction function
def predict_price(year, manufacturer, fuel, odometer, transmission):
    # Encode inputs
    manufacturer_encoded = le_manufacturer.transform([manufacturer])[0]
    fuel_encoded = le_fuel.transform([fuel])[0]
    
    # Input data as a DataFrame
    input_data = pd.DataFrame({
        "year": [year],
        "manufacturer": [manufacturer_encoded],
        "fuel": [fuel_encoded],
        "odometer": [odometer],
        "transmission": [transmission]
    })
    
    # Make the prediction
    prediction = model.predict(input_data)[0]
    return prediction

# Streamlit app layout
st.title(":red[Used Car Price Prediction]")

# Input fields with labels and default values
year = st.number_input("**:violet[Year Purchased]**", min_value=1900, max_value=2024, value=2010)
manufacturer = st.selectbox("**:violet[Manufacturer]**", df["manufacturer"].unique())
fuel = st.selectbox("**:violet[Fuel Type]**", df["fuel"].unique())
odometer = st.number_input("**:violet[Odometer]**", min_value=0, value=50000, step=100)
transmission = st.selectbox("**:violet[Transmission]**", ["automatic", "manual", "other"])

# Map transmission to numerical value
transmission_map = {"automatic": 0, "manual": 1, "other": 2}
transmission_encoded = transmission_map[transmission]

# Prediction button
if st.button("Predict"):
    # Call the prediction function with user inputs
    predicted_price = predict_price(year, manufacturer, fuel, odometer, transmission_encoded)
    
    # Display the predicted price
    st.success(f"The Predicted Price of the vechicle: ${predicted_price:.2f}")
