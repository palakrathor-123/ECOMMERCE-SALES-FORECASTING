from sklearn.linear_model import LinearRegression
import pandas as pd

def train_model(df):
    # Features (X) aur Target (y) select karna
    # Screenshot ke hisaab se Month, Quantity, aur Price use ho raha hai
    X = df[["Month", "Quantity", "Price"]]
    y = df["TotalSales"]
    
    # Linear Regression model create aur train karna
    model = LinearRegression()
    model.fit(X, y)
    
    return model

def predict_future_sales(model):
    # Future data create karna prediction ke liye
    # Screenshot mein April (4), May (5), aur June (6) ka data hai
    future_data = pd.DataFrame({
        "Month": [4, 5, 6],
        "Quantity": [10, 12, 15],
        "Price": [200, 200, 200]
    })
    
    # Model ka use karke predictions nikalna
    predictions = model.predict(future_data)
    
    return predictions