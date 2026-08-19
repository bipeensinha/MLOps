import pandas as pd

data = pd.read_csv("pune_weather.csv")

# Features
X = data[[
    "Temperature",
    "Humidity",
    "WindSpeed"
]]

# Target
y = data["Rain"]

# Convert Yes / No to 1 / 0
y = y.map({
    "Yes": 1,
    "No": 0
})

print("FEATURES")
print(X)

print("\nTARGET")
print(y)
