import pandas as pd

df = pd.read_excel("Cleaned_Dataset.xlsx")

print("===== DATASET OVERVIEW =====")
print("Rows:", len(df))
print("Columns:", len(df.columns))

print("\n===== TOTAL REVENUE =====")

total_revenue = df["TotalPrice"].sum()

print("Total Revenue:", total_revenue)
print("\n===== TOTAL ORDERS =====")

total_orders = len(df)

print("Total Orders:", total_orders)
print("\n===== PRODUCT TREND =====")

print(df["Product"].value_counts().head(5))
print("\n===== OUTLIERS =====")

Q1 = df["TotalPrice"].quantile(0.25)
Q3 = df["TotalPrice"].quantile(0.75)

IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

outliers = df[(df["TotalPrice"] < lower) |
              (df["TotalPrice"] > upper)]

print("Number of Outliers:", len(outliers))
print("\n===== BASIC STATISTICS =====")

print(df["Quantity"].describe())

print("\n")

print(df["TotalPrice"].describe())
print("\n===== OBSERVATIONS =====")

print("1. Total Revenue =", total_revenue)

print("2. Total Orders =", total_orders)

print("3. Printer is the highest selling product.")

print("4. Dataset contains 1200 orders.")

print("5. CouponCode missing values were cleaned.")

print("6. Outliers were checked using IQR method.")
print("\n===== PAYMENT METHOD ANALYSIS =====")

payment_method = df["PaymentMethod"].value_counts()

print(payment_method)
print("\n===== ORDER STATUS ANALYSIS =====")

order_status = df["OrderStatus"].value_counts()

print(order_status)
print("\n===== COUPON USAGE ANALYSIS =====")

coupon_usage = df["CouponCode"].value_counts()

print(coupon_usage)
print("\n===== REFERRAL SOURCE ANALYSIS =====")

referrals = df["ReferralSource"].value_counts()

print(referrals)

import matplotlib.pyplot as plt

top_products = df["Product"].value_counts().head(5)

plt.figure(figsize=(8,5))
top_products.plot(kind="bar")

plt.title("Top 5 Selling Products")
plt.xlabel("Product")
plt.ylabel("Number of Orders")

plt.tight_layout()
plt.savefig("Top5_Products.png")
plt.show()
payment_counts = df["PaymentMethod"].value_counts()

payment_counts.plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.title("Payment Method Distribution")
plt.ylabel("")
plt.savefig("Payment_Methods.png")
plt.show()
status_counts = df["OrderStatus"].value_counts()

status_counts.plot(kind="bar")

plt.title("Order Status Distribution")
plt.xlabel("Order Status")
plt.ylabel("Count")
plt.savefig("Order_Status.png")
plt.show()
referral_counts = df["ReferralSource"].value_counts()

referral_counts.plot(kind="bar")

plt.title("Referral Source Analysis")
plt.xlabel("Source")
plt.ylabel("Count")
plt.savefig("Referral_Source.png")
plt.show()
df["Date"] = pd.to_datetime(df["Date"])

monthly_revenue = df.groupby(
    df["Date"].dt.month
)["TotalPrice"].sum()

monthly_revenue.plot(
    kind="line",
    marker="o"
)

plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.savefig("Monthly_Revenue.png")
plt.show()
print("Chart Saved Successfully!")
