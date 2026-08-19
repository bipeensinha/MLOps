import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle


# Load data
data = pd.read_csv("pune_weather.csv")


# Features
X = data[[
    "Temperature",
    "Humidity",
    "WindSpeed"
]]


# Target
y = data["Rain"].map({
    "Yes": 1,
    "No": 0
})


# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# Create model
model = LogisticRegression()


# Train model
model.fit(X_train, y_train)


print("Model training completed!")

print("Training records:", len(X_train))
print("Testing records:", len(X_test))


# Save model
with open("model.pkl", "wb") as file:
    pickle.dump(model, file)

print("Model saved as model.pkl")
