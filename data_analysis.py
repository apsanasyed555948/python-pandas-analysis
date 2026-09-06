import pandas as pd

# --------------------------------------------------
# Pandas Data Analysis Project
# --------------------------------------------------
# This program demonstrates:
# 1. Loading a CSV dataset
# 2. Inspecting the data
# 3. Cleaning missing and incorrect data
# 4. Filtering data
# 5. Grouping and aggregation
# 6. Generating simple insights
# --------------------------------------------------

# Create sample sales data
data = {
    "Product": [
        "Laptop", "Phone", "Tablet", "Laptop",
        "Phone", "Tablet", "Laptop", "Phone",
        "Tablet", "Laptop"
    ],
    "Category": [
        "Electronics", "Electronics", "Electronics", "Electronics",
        "Electronics", "Electronics", "Electronics", "Electronics",
        "Electronics", "Electronics"
    ],
    "Quantity": [
        2, 5, 3, 1, 4, None, 2, 6, 3, 1
    ],
    "Price": [
        800, 500, 300, 800, 500, 300, 800, 500, 300, -800
    ]
}

# Convert the data into a Pandas DataFrame
df = pd.DataFrame(data)

# Save the data as a CSV file
df.to_csv("sales_data.csv", index=False)

print("CSV dataset created successfully!")

# --------------------------------------------------
# Load and inspect the CSV dataset
# --------------------------------------------------

df = pd.read_csv("sales_data.csv")

print("\nFirst 5 rows:")
print(df.head())

print("\nDataset information:")
print(df.info())

print("\nMissing values:")
print(df.isnull().sum())

# --------------------------------------------------
# Clean the data
# --------------------------------------------------

# Replace missing Quantity values with 0
df["Quantity"] = df["Quantity"].fillna(0)

# Remove rows with zero or negative prices
df = df[df["Price"] > 0]

print("\nData after cleaning:")
print(df)

# --------------------------------------------------
# Calculate total sales
# --------------------------------------------------

df["Total_Sales"] = df["Quantity"] * df["Price"]

# --------------------------------------------------
# Filtering
# --------------------------------------------------

# Select sales greater than 1500
high_sales = df[df["Total_Sales"] > 1500]

print("\nSales greater than 1500:")
print(high_sales)

# --------------------------------------------------
# Grouping and aggregation
# --------------------------------------------------

product_summary = df.groupby("Product").agg(
    Total_Quantity=("Quantity", "sum"),
    Total_Sales=("Total_Sales", "sum"),
    Average_Sales=("Total_Sales", "mean")
).reset_index()

print("\nProduct Summary:")
print(product_summary)

# --------------------------------------------------
# Generate simple insights
# --------------------------------------------------

top_product = product_summary.loc[
    product_summary["Total_Sales"].idxmax()
]

print("\nINSIGHTS")
print("-" * 40)

print(
    f"The product with the highest total sales is "
    f"{top_product['Product']} with total sales of "
    f"{top_product['Total_Sales']:.2f}."
)

print(
    f"{top_product['Product']} sold a total quantity of "
    f"{top_product['Total_Quantity']:.0f}."
)

print(
    "The dataset was cleaned by replacing the missing "
    "quantity with 0 and removing the row with an "
    "incorrect negative price."
)
