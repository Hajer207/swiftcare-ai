from pathlib import Path
import joblib
import pandas as pd
from train import train_model


MODEL_PATH = "models/trained_model.pkl"


def load_model():
    if not Path(MODEL_PATH).exists():
        model = train_model()
    else:
        model = joblib.load(MODEL_PATH)

    return model


model = load_model()


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
        "Treatment Priority": treatment_priority
    }])

    prediction = model.predict(input_data)[0]

    return prediction


def critical_alert(risk_level, treatment_priority):
    return risk_level == "High" and treatment_priority == "Urgent"