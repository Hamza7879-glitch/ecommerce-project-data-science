
import pandas as pd

file_path = "Ecommerce_Unclean_Project.xlsx"

df = pd.read_excel(file_path)

print(df.head())

# Size of Data
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

# Check Column names
print(df.columns)

# Check Missing Values
print(df.isnull().sum())

# Remove Duplicate Rows
print("Duplicates before:", df.duplicated().sum())

df = df.drop_duplicates()

print("Duplicates after:", df.duplicated().sum())

# Clean Customer Names
df["Customer_Name"] = (
    df["Customer_Name"]
    .astype("string")
    .str.strip()
    .str.title()
)

# Clean City Names
df["City"] = (
    df["City"]
    .astype("string")
    .str.strip()
    .str.title()
)

# Clean State
df["State"] = (
    df["State"]
    .astype("string")
    .str.strip()
    .str.title()
)

# Clean Product and Category
df["Product"] = (
    df["Product"]
    .astype("string")
    .str.strip()
    .str.title()
)

df["Category"] = (
    df["Category"]
    .astype("string")
    .str.strip()
    .str.title()
)

# Clean Dates
df["Order_Date"] = pd.to_datetime(
    df["Order_Date"],
    dayfirst=True,
    errors="coerce"
)
df["Delivery_Date"] = pd.to_datetime(
    df["Delivery_Date"],
    dayfirst=True,
    errors="coerce"
)

# Clean Discount
df["Discount"] = pd.to_numeric(
    df["Discount"],
    errors="coerce"
)

# Handle Missing Discount
df["Discount"] = df["Discount"].fillna(0)

# Handle Quantity
df["Qty"] = pd.to_numeric(
    df["Qty"],
    errors="coerce"
)
# Check Values
print(df["Qty"].describe())
# Median Quantity
df["Qty"] = df["Qty"].fillna(
    df["Qty"].median()
)

# Handle Unit Price
df["Unit_Price"] = pd.to_numeric(
    df["Unit_Price"],
    errors="coerce"
)
# Check
print(df["Unit_Price"].describe())
# Median for Missing
df["Unit_Price"] = df["Unit_Price"].fillna(
    df["Unit_Price"].median()
)

# Clean Phone
df["Phone"] = df["Phone"].astype("string")
# For Missing Phone Numbers
df["Phone"] = df["Phone"].replace(
    ["nan", "None", ""],
    pd.NA
)

# Check Email
print(df["Email"].isnull().sum())
# For Removing Unnecessary Spaces
df["Email"] = (
    df["Email"]
    .astype("string")
    .str.strip()
    .str.lower()
)

# Clean Payment Mode
df["Payment_Mode"] = (
    df["Payment_Mode"]
    .astype("string")
    .str.strip()
)

# Clean Order Status
df["Order_Status"] = (
    df["Order_Status"]
    .astype("string")
    .str.strip()
    .str.title()
)

# Check Everything After Cleaning
print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicates:")
print(df.duplicated().sum())

print("\nData types:")
print(df.dtypes)

# Save the Cleaned File
output_file = "Ecommerce_Cleaned.xlsx"

df.to_excel(output_file, index=False)

print("\nCleaned file saved successfully!")

