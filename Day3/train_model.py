import pandas as pd, joblib
from sklearn.tree import DecisionTreeClassifier
from blob_utils import download_blob

print("=== VODAFONE MODEL TRAINING ===")

download_blob("feature-store/customer_features_extracted.csv", "customer_features_extracted.csv")
df = pd.read_csv("customer_features_extracted.csv")

df["BillingStatus"] = [0,0,1,0]  # Labels

X = df[["MonthlyDataUsage","AverageCallCount","MonthlyBill","UsageBillingRatio"]]
y = df["BillingStatus"]

model = DecisionTreeClassifier(random_state=42)
model.fit(X, y)

joblib.dump(model, "../models/model_v2.pkl")
print("AI Model Trained Successfully")
