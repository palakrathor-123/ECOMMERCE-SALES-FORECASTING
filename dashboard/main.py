import sys
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from sklearn.linear_model import LinearRegression

# Path setup taaki src folder se modules import ho sakein
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.data_cleaning import load_and_clean_data
from src.forecasting_model import train_model, predict_future_sales

# Page Title
st.title("E-Commerce Sales Analysis Dashboard")

# 1. Load Dataset
df = load_and_clean_data("data/sales_data.csv")

# 2. Data Preprocessing
df["OrderDate"] = pd.to_datetime(df["OrderDate"])
df["TotalSales"] = df["Quantity"] * df["Price"]
df["Month"] = df["OrderDate"].dt.month

# 3. Dataset Preview
st.subheader("Dataset Preview")
st.write(df.head())

# 4. Sales by Region (Bar Chart)
st.subheader("Sales by Region")
region_sales = df.groupby("Region")["TotalSales"].sum()
fig1, ax1 = plt.subplots()
region_sales.plot(kind="bar", ax=ax1, color="skyblue")
ax1.set_xlabel("Region")
ax1.set_ylabel("Total Sales")
st.pyplot(fig1)

# 5. Monthly Sales Trend (Line Chart)
st.subheader("Monthly Sales Trend")
monthly_sales = df.groupby("Month")["TotalSales"].sum()
fig2, ax2 = plt.subplots()
monthly_sales.plot(kind="line", marker="o", ax=ax2, color="orange")
ax2.set_xlabel("Month")
ax2.set_ylabel("Total Sales")
st.pyplot(fig2)

# 6. Sales by Category (Pie Chart)
st.subheader("Sales by Category")
category_sales = df.groupby("Category")["TotalSales"].sum()
fig3, ax3 = plt.subplots()
category_sales.plot(kind="pie", autopct='%1.1f%%', ax=ax3)
ax3.set_ylabel("") # Hide y-label for pie chart
st.pyplot(fig3)

# 7. Top Selling Products
st.subheader("Top Selling Products")
top_products = df.groupby("Product")["TotalSales"].sum().sort_values(ascending=False)
st.write(top_products.head())

# 8. Correlation Heatmap
st.subheader("Correlation Heatmap")
# Sirf numeric columns ka correlation
corr = df[["Quantity", "Price", "TotalSales", "Month"]].corr()
fig5, ax5 = plt.subplots()
sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax5)
st.pyplot(fig5)

# 9. Sales Forecast (Machine Learning)
st.subheader("Sales Forecast")

# Model training
model = train_model(df)

# Future Data for Prediction (April, May, June)
future_data = pd.DataFrame({
    "Month": [4, 5, 6],
    "Quantity": [10, 12, 15],
    "Price": [200, 200, 200]
})

# Predictions
predictions = model.predict(future_data)

# Forecast Table
forecast_df = pd.DataFrame({
    "Month": ["April", "May", "June"],
    "Predicted Sales": predictions
})

st.write("Future Sales Predictions:")
st.write(forecast_df)

# Forecast Line Chart
st.line_chart(forecast_df.set_index("Month"))