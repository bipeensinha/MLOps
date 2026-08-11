import pandas as pd, joblib

print("=== VODAFONE BILLING PREDICTION ===")

model = joblib.load("../models/model_v2.pkl")

new_customer = pd.DataFrame({
    "MonthlyDataUsage":[12],
    "AverageCallCount":[130],
    "MonthlyBill":[900],
    "UsageBillingRatio":[0.013]
})

prediction = model.predict(new_customer)

print("Prediction :", "Normal Billing" if prediction[0]==0 else "Billing Anomaly Detected")
