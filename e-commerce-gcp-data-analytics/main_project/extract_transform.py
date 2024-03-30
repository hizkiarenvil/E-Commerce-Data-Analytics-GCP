import pandas as pd

df = pd.read_csv('e_commerce_data.csv', encoding='latin1')

print(df.head())

# Error Handling TEST
# try:
#     df = pd.read_csv('e-commerce-data.csv', encoding='latin1')
# except FileNotFoundError:
#     print("CSV file not found. Please check the file path.")

# Check for missing values
missing_values = df.isnull().sum()
print('Missing Values:')
print(missing_values)

# Impute missing values in the 'description' column with 'unknown'
df['Description'].fillna('Unknown', inplace=True)

# Impute missing values in numeric columns with the mean
numeric_cols = ['Quantity', 'UnitPrice']
for col in numeric_cols:
    df[col].fillna(df[col].mean(), inplace=True)

# Step 2: Remove Duplicates
# Check for duplicate rows
duplicate_rows = df[df.duplicated()]
print('\nDuplicate Rows:')
print(duplicate_rows)

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# Step 3: Date-Time Conversion
# Convert 'invoicedate' to datetime
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'], format='%m/%d/%Y %H:%M')

#  Display the cleaned DataFrame
print('\nCleaned DataFrame:')
print(df.head())