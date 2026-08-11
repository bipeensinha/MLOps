import pandas as pd
from blob_utils import download_blob, upload_blob

print("=== VODAFONE FEATURE ENGINEERING ===")

download_blob("raw-data/billing_data_extracted.csv", "billing_data_extracted.csv")
df = pd.read_csv("billing_data_extracted.csv")

df["MonthlyDataUsage"] = df["DataGB"]
df["AverageCallCount"] = df["Calls"]
df["MonthlyBill"] = df["BillAmount"]
df["UsageBillingRatio"] = df["DataGB"] / df["BillAmount"]

df.to_csv("customer_features_extracted.csv", index=False)
upload_blob("customer_features_extracted.csv", "feature-store/customer_features_extracted.csv")

print("Feature Store Updated Successfully")
print(df)
