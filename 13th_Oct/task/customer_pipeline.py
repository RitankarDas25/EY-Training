import pandas as pd
from datetime import datetime

# Step 1: Extract
df = pd.read_csv('customers.csv')

# Step 2: Transform
def age_group(age):
    if age < 30:
        return 'Young'
    elif age < 50:
        return 'Adult'
    else:
        return 'Senior'

df['AgeGroup'] = df['Age'].apply(age_group)
df_filtered = df[df['Age'] >= 20]

# Step 3: Load
df_filtered.to_csv('filtered_customers.csv', index=False)

# Step 4: Print execution time
print("Customer pipeline executed at", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
