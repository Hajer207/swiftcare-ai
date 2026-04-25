import joblib
import pandas as pd


model = joblib.load(
    "models/trained_model.pkl"
)


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

    prediction = model.predict(
        input_data
    )[0]

    return prediction



def critical_alert(
    risk_level,
    treatment_priority
):

    if (
        risk_level=="High"
        and treatment_priority=="Urgent"
    ):
        return True

    return False