from pathlib import Path
import joblib

from src.preprocessing import preprocess_data
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


def train_model():
    df = preprocess_data()

    X = df.drop(columns=["Medical Condition", "Billing Amount"])
    y = df["Medical Condition"]

    categorical_features = [
        "Gender",
        "Blood Type",
        "Admission Type",
        "Medication",
        "Test Results",
        "Risk Level",
        "Treatment Priority",
    ]

    preprocessor = ColumnTransformer(
        transformers=[
            ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features)
        ],
        remainder="passthrough"
    )

    model = Pipeline([
        ("preprocessor", preprocessor),
        ("classifier", RandomForestClassifier(n_estimators=100, random_state=42))
    ])

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)

    Path("models").mkdir(exist_ok=True)
    joblib.dump(model, "models/trained_model.pkl")

    print(f"Model Accuracy: {accuracy:.2f}")
    print("Model saved successfully.")

    return model


if __name__ == "__main__":
    train_model()