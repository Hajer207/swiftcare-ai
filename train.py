from autogluon.tabular import TabularPredictor
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from src.preprocessing import preprocess_data


MODEL_PATH = "AutogluonModels/swiftcare_model"


def train_model():
    df = preprocess_data()

    df = df.drop(columns=["Billing Amount"], errors="ignore")
    df = df.dropna()

    # Convert categorical columns to string to avoid AutoGluon type issues
    categorical_columns = [
        "Gender",
        "Blood Type",
        "Admission Type",
        "Medication",
        "Test Results",
        "Risk Level",
        "Treatment Priority",
        "Medical Condition",
    ]

    for col in categorical_columns:
        df[col] = df[col].astype(str)

    train_data, test_data = train_test_split(
        df,
        test_size=0.2,
        random_state=42,
        stratify=df["Medical Condition"]
    )

    predictor = TabularPredictor(
        label="Medical Condition",
        path=MODEL_PATH,
        problem_type="multiclass",
        eval_metric="accuracy"
    ).fit(
        train_data=train_data,
        presets="medium_quality",
        time_limit=600,
        verbosity=3
    )

    test_x = test_data.drop(columns=["Medical Condition"])
    test_y = test_data["Medical Condition"]

    predictions = predictor.predict(test_x)
    accuracy = accuracy_score(test_y, predictions)

    print(f"AutoGluon Model Accuracy: {accuracy:.2f}")
    print("AutoGluon model saved successfully.")

    return predictor


if __name__ == "__main__":
    train_model()