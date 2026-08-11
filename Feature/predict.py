# ---------------------------------------------------------
# Import Required Libraries
# ---------------------------------------------------------

# Pandas is used to read and work with CSV files
import pandas as pd

# DecisionTreeClassifier is a Machine Learning algorithm
# used to classify data into different categories.
from sklearn.tree import DecisionTreeClassifier


# ---------------------------------------------------------
# Step 1: Read the Feature Store
# ---------------------------------------------------------

# Load the engineered features from the Feature Store
df = pd.read_csv("../data/customer_features.csv")


# ---------------------------------------------------------
# Step 2: Create the Target Column
# ---------------------------------------------------------

# BillingStatus is the value we want the AI model to predict.
# 0 = Normal Billing
# 1 = Billing Anomaly

df["BillingStatus"] = [0, 0, 1, 0, 1, 0, 0, 1]


# ---------------------------------------------------------
# Step 3: Select Input Features
# ---------------------------------------------------------

# These are the business features used to train the AI model.

X = df[[
    "MonthlyDataUsage",
    "AverageCallCount",
    "MonthlyBill",
    "UsageBillingRatio"
]]


# ---------------------------------------------------------
# Step 4: Select the Target Variable
# ---------------------------------------------------------

# This is the output the model will learn to predict.

y = df["BillingStatus"]


# ---------------------------------------------------------
# Step 5: Create the Machine Learning Model
# ---------------------------------------------------------

# Create a Decision Tree Classification model.

model = DecisionTreeClassifier()


# ---------------------------------------------------------
# Step 6: Train the AI Model
# ---------------------------------------------------------

# Train the model using the Feature Store data.

model.fit(X, y)

print("AI Model Trained Successfully")


# ---------------------------------------------------------
# Step 7: Create a New Customer Record
# ---------------------------------------------------------

# New customer feature values for prediction.
# Using a DataFrame keeps the same feature names used during training.

new_customer = pd.DataFrame({
    "MonthlyDataUsage": [12],
    "AverageCallCount": [130],
    "MonthlyBill": [900],
    "UsageBillingRatio": [0.013]
})


# ---------------------------------------------------------
# Step 8: Predict the Billing Status
# ---------------------------------------------------------

prediction = model.predict(new_customer)


# ---------------------------------------------------------
# Step 9: Display the Result
# ---------------------------------------------------------

if prediction[0] == 0:
    print("Prediction : Normal Billing")
else:
    print("Prediction : Billing Anomaly Detected")