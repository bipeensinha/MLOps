import pandas as pd

from sklearn.tree import DecisionTreeClassifier

# Read Feature Store
df = pd.read_csv("../data/customer_features.csv")

# Create target column
df["BillingStatus"] = [0, 0, 1, 0, 1, 0, 0, 1]

# Select Features
X = df[
    [
        "MonthlyDataUsage",
        "AverageCallCount",
        "MonthlyBill",
        "UsageBillingRatio",
    ]
]

# Target
y = df["BillingStatus"]

# Train AI Model
model = DecisionTreeClassifier()

model.fit(X, y)

print("AI Model Trained Successfully")