import pandas as pd

# List of your three CSV files
files = [
    "data/daily_sales_data_0.csv",
    "data/daily_sales_data_1.csv",
    "data/daily_sales_data_2.csv"
]

# Read and concatenate them into a single DataFrame
df_list = [pd.read_csv(f) for f in files]
df = pd.concat(df_list, ignore_index=True)

# Filter for only "Pink Morsel" rows (case-insensitive)
df = df[df['product'].str.lower() == "pink morsel"]

# Compute the “Sales” field for each row
df['price'] = df['price'].replace(r'[\$,]', '', regex=True).astype(float)
df['quantity'] = df['quantity'].astype(int)
df['Sales'] = df['price'] * df['quantity']

# Write a new CSV file with only Sales, Date, and Region
df[['Sales', 'date', 'region']].to_csv('pink_morsel_sales.csv', index=False)

