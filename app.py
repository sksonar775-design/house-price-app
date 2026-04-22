import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

# Dataset
data = {
    "Size": [1000,1200,1500,800,900,1100,1300,1600,1400,1700],
    "Bedrooms": [2,3,3,1,2,2,3,4,3,4],
    "Bathrooms": [1,2,2,1,1,2,2,3,2,3],
    "Price": [2000000,3000000,3500000,1500000,1800000,2500000,3200000,4000000,3600000,4200000]
}

df = pd.DataFrame(data)

X = df.drop("Price", axis=1)
y = df["Price"]

model = LinearRegression()
model.fit(X, y)

# UI
st.title("🏠 House Price Prediction App")

size = st.number_input("Enter Size (sq ft)", value=1000)
bedrooms = st.number_input("Enter Bedrooms", value=2)
bathrooms = st.number_input("Enter Bathrooms", value=1)

if st.button("Predict"):
    input_data = pd.DataFrame(
        [[size, bedrooms, bathrooms]],
        columns=["Size", "Bedrooms", "Bathrooms"]
    )

    prediction = model.predict(input_data)

    st.success(f"Estimated Price: ₹{int(prediction[0])}")