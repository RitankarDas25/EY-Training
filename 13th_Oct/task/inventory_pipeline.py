import pandas as pd
from datetime import datetime

# Step 1: Extract
df = pd.read_csv('inventory.csv')

# Step 2: Transform
df['RestockNeeded'] = df.apply(lambda x: 'Yes' if x['Quantity'] < x['ReorderLevel'] else 'No', axis=1)
df['TotalValue'] = df['Quantity'] * df['PricePerUnit']

# Step 3: Load
df.to_csv('restock_report.csv', index=False)

# Step 4: Print completion time
print("Inventory pipeline completed at", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
