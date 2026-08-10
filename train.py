import pandas as pd
import mlflow
import mlflow.sklearn

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Load Dataset
data = pd.read_csv("billing_data.csv")

# Features and Target
X = data[["Usage_GB", "Bill_Amount", "Expected_Bill"]]
y = data["Leakage"]

# Split Dataset (70% Training, 30% Testing)
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.30,
    random_state=42
)

# Start MLflow Experiment
mlflow.set_experiment("Vodafone Billing AI")

with mlflow.start_run():

    # Create Model
    model = DecisionTreeClassifier(max_depth=3)

    # Train Model
    model.fit(X_train, y_train)

    # Prediction
    predictions = model.predict(X_test)

    # Accuracy
    accuracy = accuracy_score(y_test, predictions)

    # Log Parameters
    mlflow.log_param("Algorithm", "Decision Tree")
    mlflow.log_param("Max Depth", 3)

    # Log Metric
    mlflow.log_metric("Accuracy", accuracy)

    # Save Model
    mlflow.sklearn.log_model(model, "billing_model")

    print("--------------------------------")
    print("Training Completed")
    print("Accuracy :", round(accuracy * 100, 2), "%")
    print("--------------------------------")