import pandas as pd

# Load dataset
df = pd.read_excel("Dataset for Data Analytics.xlsx")

print("===== DATASET INFO =====")
print("Rows:", len(df))
print("Columns:", len(df.columns))

print("\n===== MISSING VALUES BEFORE CLEANING =====")
print(df.isnull().sum())

# Fill blank CouponCode values
df["CouponCode"] = df["CouponCode"].fillna("No Coupon")

print("\n===== MISSING VALUES AFTER CLEANING =====")
print(df.isnull().sum())

print("\n===== DUPLICATE ROWS =====")
print(df.duplicated().sum())

# Save cleaned dataset
df.to_excel("Cleaned_Dataset.xlsx", index=False)

print("\nCleaned file saved successfully!")