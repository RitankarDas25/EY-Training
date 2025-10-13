import pandas as pd
from datetime import datetime

# Step 1: Extract
products = pd.read_csv('products.csv')
customers = pd.read_csv('customers_capstone.csv')
orders = pd.read_csv('orders.csv')

orders['CustomerID'] = orders['CustomerID'].astype(str)
customers['CustomerID'] = customers['CustomerID'].astype(str)

# Step 2.1: Join datasets
orders_customers = pd.merge(orders, customers, on='CustomerID', how='left')
full_data = pd.merge(orders_customers, products, on='ProductID', how='left')

# Step 2.2: Add calculated columns
full_data['TotalAmount'] = full_data['Quantity'] * full_data['Price']
full_data['OrderMonth'] = pd.to_datetime(full_data['OrderDate']).dt.month

# Step 2.3: Filter data
filtered_data = full_data[(full_data['Quantity'] >= 2) & (full_data['Country'].isin(['India', 'UAE']))]

# Step 2.4: Group and aggregate
category_summary = filtered_data.groupby('Category')['TotalAmount'].sum().reset_index()
segment_summary = filtered_data.groupby('Segment')['TotalAmount'].sum().reset_index()

# Step 2.5: Customer revenue ranking
customer_revenue = (
    filtered_data.groupby(['CustomerID', 'Name'])['TotalAmount']
    .sum()
    .reset_index()
    .sort_values(by='TotalAmount', ascending=False)
)

# Step 3: Load final outputs
filtered_data.to_csv('processed_orders.csv', index=False)
category_summary.to_csv('category_summary.csv', index=False)
segment_summary.to_csv('segment_summary.csv', index=False)

# Print execution time
print("Sales pipeline executed at", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
