import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_excel("Cleaned_Dataset.xlsx")

# Chart 1 - Top Products by Revenue
product_sales = df.groupby("Product")["TotalPrice"].sum()

plt.figure(figsize=(8,5))
product_sales.plot(kind="bar")
plt.title("Revenue by Product")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("Product_Revenue.png")
plt.close()

# Chart 2 - Payment Method Usage
payment_count = df["PaymentMethod"].value_counts()

plt.figure(figsize=(6,6))
payment_count.plot(kind="pie", autopct="%1.1f%%")
plt.title("Payment Method Distribution")
plt.ylabel("")
plt.savefig("Payment_Methods.png")
plt.close()

# Chart 3 - Order Status Count
status_count = df["OrderStatus"].value_counts()

plt.figure(figsize=(8,5))
status_count.plot(kind="bar")
plt.title("Order Status Distribution")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("Order_Status.png")
plt.close()

# Chart 4 - Referral Source Count
referral_count = df["ReferralSource"].value_counts()

plt.figure(figsize=(8,5))
referral_count.plot(kind="bar")
plt.title("Referral Source Distribution")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("Referral_Source.png")
plt.close()

# Chart 5 - Quantity vs Total Price
plt.figure(figsize=(8,5))
plt.scatter(df["Quantity"], df["TotalPrice"])
plt.title("Quantity vs Total Price")
plt.xlabel("Quantity")
plt.ylabel("Total Price")
plt.tight_layout()
plt.savefig("Quantity_vs_TotalPrice.png")
plt.close()

print("All charts created successfully!")