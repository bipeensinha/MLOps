import pandas as pd

# -----------------------------------------
# Read COVID data
# -----------------------------------------
df = pd.read_csv("data/covid_data.csv")

print("Raw COVID Data")
print(df)

# -----------------------------------------
# Create ML features
# -----------------------------------------
df["TemperatureAboveNormal"] = (df["Temperature"] > 38.0).astype(int)
df["LowOxygen"] = (df["OxygenLevel"] < 94).astype(int)
df["LongCough"] = (df["CoughDays"] >= 5).astype(int)

# -----------------------------------------
# Save feature dataset
# -----------------------------------------
df.to_csv("data/covid_features.csv", index=False)

print("\nCOVID Feature Dataset Created")
print(df)
