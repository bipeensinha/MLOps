# Import the Pandas library
import pandas as pd

# Read the Vodafone billing dataset
df = pd.read_csv("../data/billing_data.csv")

# Create business features

# Feature 1: Monthly Data Usage
df["MonthlyDataUsage"] = df["DataGB"]

# Feature 2: Average Call Count
df["AverageCallCount"] = df["Calls"]

# Feature 3: Monthly Bill
df["MonthlyBill"] = df["BillAmount"]

# Feature 4: Usage Billing Ratio
df["UsageBillingRatio"] = df["DataGB"] / df["BillAmount"]

# Save the generated features
df.to_csv("../data/customer_features.csv", index=False)

print("Feature Store Created Successfully")

print(df)
