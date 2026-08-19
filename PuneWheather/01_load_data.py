import pandas as pd

data = pd.read_csv("pune_weather.csv")

print("Pune Weather Data")
print("-----------------")

print(data)

print("\nNumber of rows:", len(data))
print("Number of columns:", len(data.columns))
