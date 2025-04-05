import pandas as pd

# Read the Excel files using correct relative paths
sales = pd.read_excel('../data/sales.xlsx')
products = pd.read_excel('../data/products.xlsx')
customers = pd.read_excel('../data/customers.xlsx')

# Example Cleaning Operations
# Drop duplicates
sales.drop_duplicates(inplace=True)
products.drop_duplicates(inplace=True)
customers.drop_duplicates(inplace=True)

# Handle missing values
sales.fillna(0, inplace=True)
products.fillna('Unknown', inplace=True)
customers.fillna('Unknown', inplace=True)

# Save cleaned data
sales.to_csv('../processed_data/sales_clean.csv', index=False)
products.to_csv('../processed_data/products_clean.csv', index=False)
customers.to_csv('../processed_data/customers_clean.csv', index=False)

print("Data Cleaning Completed Successfully!")
