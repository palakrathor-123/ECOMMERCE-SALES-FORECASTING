import pandas as pd

# 1. Sample data banana (Dictionary format mein)
data = {
    'Date': ['2025-07-09', '2025-07-10', '2025-07-11', '2025-07-12'],
    'OrderID': [1000, 1001, 1002, 1003],
    'Product': ['Keyboard', 'Mouse', 'Monitor', 'USB Cable'],
    'Category': ['Accessories', 'Accessories', 'Electronics', 'Accessories'],
    'Price': [1200, 500, 15000, 300],
    'Quantity': [5, 10, 2, 15],
    'Region': ['Delhi', 'Mumbai', 'Bangalore', 'Delhi']
}

# 2. Data ko DataFrame mein convert karna
df = pd.DataFrame(data)

# 3. CSV file save karna (data folder ke andar)
# Dhyaan dein ki aapke project mein 'data' naam ka folder pehle se bana ho
df.to_csv('data/sales_data.csv', index=False)

print("CSV file successfully ban gayi hai: data/sales_data.csv")