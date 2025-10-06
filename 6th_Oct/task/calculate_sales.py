import pandas as pd
import logging

# Configure logging
logging.basicConfig(
    filename='sales.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

try:
    # Read CSV
    df = pd.read_csv('sales.csv')

    # Check if required columns exist
    required_columns = {'product', 'price', 'quantity'}
    if not required_columns.issubset(df.columns):
        raise ValueError("CSV file is missing required columns")

    # Convert price and quantity to numeric, force errors to NaN
    df['price'] = pd.to_numeric(df['price'], errors='coerce')
    df['quantity'] = pd.to_numeric(df['quantity'], errors='coerce')

    # Find rows with invalid numeric data
    invalid_rows = df[df['price'].isna() | df['quantity'].isna()]

    if not invalid_rows.empty:
        for _, row in invalid_rows.iterrows():
            logging.error(f"Invalid numeric value for product {row['product']}: price={row['price']}, quantity={row['quantity']}")
            print(f"Error: Invalid numeric value for product {row['product']}")
        # Remove invalid rows before processing
        df = df.drop(invalid_rows.index)

    # Compute total sales
    df['total_sales'] = df['price'] * df['quantity']

    # Print and log total sales per product
    for _, row in df.iterrows():
        total = row['total_sales']
        product = row['product']
        # Fix: convert total to int if no decimals, else keep as float
        if total == int(total):
            total_display = int(total)
        else:
            total_display = total
        print(f"{product} total = {total_display}")
        logging.info(f"{product} total sales = {total_display}")

except FileNotFoundError:
    logging.error("sales.csv not found.")
    print("Error: sales.csv file not found.")
except Exception as e:
    logging.error(f"An error occurred: {e}")
    print(f"Error: {e}")
