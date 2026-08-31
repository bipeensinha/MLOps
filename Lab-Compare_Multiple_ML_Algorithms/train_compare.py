import warnings
import logging

# Suppress Python warnings
warnings.filterwarnings("ignore")

# Suppress WARNING and INFO log messages
logging.disable(logging.WARNING)

import pandas as pd
import mlflow
import mlflow.sklearn

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier




# ---------------------------------------
# 1. Load Dataset
# ---------------------------------------

data = pd.read_csv("billing_data.csv")

X = data[
    [
        "Usage_GB",
        "Bill_Amount",
        "Expected_Bill",
        "Roaming_GB"
    ]
]

y = data["Anomaly"]


# ---------------------------------------
# 2. Train/Test Split
# ---------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.30,
    random_state=42,
    stratify=y
)


# ---------------------------------------
# 3. Define Models
# ---------------------------------------

models = {

    "Logistic Regression":
        LogisticRegression(max_iter=1000),

    "Decision Tree":
        DecisionTreeClassifier(
            max_depth=4,
            random_state=42
        ),

    "Random Forest":
        RandomForestClassifier(
            n_estimators=100,
            random_state=42
        ),

    "KNN":
       KNeighborsClassifier(n_neighbors=3)
}


# ---------------------------------------
# 4. MLflow Experiment
# ---------------------------------------

mlflow.set_experiment("Vodafone Billing Model Comparison")


# ---------------------------------------
# 5. Train and Compare Models
# ---------------------------------------

for model_name, model in models.items():

    with mlflow.start_run(run_name=model_name):

        # Train
        model.fit(X_train, y_train)

        # Predict
        predictions = model.predict(X_test)

        # Metrics
        accuracy = accuracy_score(
            y_test,
            predictions
        )

        precision = precision_score(
            y_test,
            predictions,
            zero_division=0
        )

        recall = recall_score(
            y_test,
            predictions,
            zero_division=0
        )

        # Print results
        print("\nModel:", model_name)
        print("Accuracy:", round(accuracy, 3))
        print("Precision:", round(precision, 3))
        print("Recall:", round(recall, 3))

                # Log parameters
        mlflow.log_param(
            "algorithm",
            model_name
        )

        # Log metrics
        mlflow.log_metric(
            "accuracy",
            accuracy
        )

        mlflow.log_metric(
            "precision",
            precision
        )

        mlflow.log_metric(
            "recall",
            recall
        )

        # Log model
        mlflow.sklearn.log_model(
            model,
            name="billing_model",
            serialization_format="cloudpickle"
        )

print("\nAll models trained successfully!")

