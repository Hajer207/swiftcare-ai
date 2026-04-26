from pathlib import Path
import pandas as pd
from autogluon.tabular import TabularPredictor

from train import train_model


MODEL_PATH = "AutogluonModels/swiftcare_model"


def load_model():
    if not Path(MODEL_PATH).exists():
        predictor = train_model()
    else:
        predictor = TabularPredictor.load(MODEL_PATH)

    return predictor


model = load_model()


def get_age_group(age):
    if age <= 18:
        return "Child"
    elif age <= 35:
        return "Young Adult"
    elif age <= 50:
        return "Adult"
    elif age <= 65:
        return "Senior"
    else:
        return "Elderly"


def predict_patient(
    age,
    gender,
    blood_type,
    admission_type,
    medication,
    test_results,
    risk_level,
    treatment_priority
):

    input_data = pd.DataFrame([{
        "Age": age,
        "Gender": gender,
        "Blood Type": blood_type,
        "Admission Type": admission_type,
        "Medication": medication,
        "Test Results": test_results,
        "Risk Level": risk_level,
        "Treatment Priority": treatment_priority,

        # Engineered features used during training
        "Age Group": get_age_group(age),
        "Is Elderly": 1 if age >= 65 else 0,
        "Is Abnormal Test": 1 if test_results == "Abnormal" else 0,
        "Is Emergency": 1 if admission_type == "Emergency" else 0
    }])

    prediction = model.predict(input_data)[0]

    return prediction


def critical_alert(risk_level, treatment_priority):
    return risk_level == "High" and treatment_priority == "Urgent"