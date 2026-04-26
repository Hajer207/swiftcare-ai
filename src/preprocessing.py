import pandas as pd


def load_data(path="data/healthcare_dataset.csv"):
    """
    Load the healthcare dataset from a CSV file.
    """
    df = pd.read_csv(path)
    return df


def clean_data(df):
    """
    Clean the dataset by removing unnecessary columns and handling missing values.
    """
    df = df.copy()

    columns_to_drop = [
        "Name",
        "Doctor",
        "Hospital",
        "Room Number",
        "Date of Admission",
        "Discharge Date",
        "Insurance Provider",
    ]

    df = df.drop(columns=columns_to_drop, errors="ignore")
    df = df.dropna()

    return df


def create_risk_level(row):
    """
    Create a risk level based on patient age, admission type, and test results.
    """
    age = row["Age"]
    admission_type = row["Admission Type"]
    test_result = row["Test Results"]

    if admission_type == "Emergency" and test_result == "Abnormal":
        return "High"

    elif age >= 65 and admission_type in ["Emergency", "Urgent"]:
        return "High"

    elif test_result == "Abnormal" and admission_type == "Urgent":
        return "High"

    elif test_result == "Abnormal":
        return "Medium"

    elif admission_type == "Urgent" or test_result == "Inconclusive":
        return "Medium"

    else:
        return "Low"


def create_priority(row):
    """
    Create treatment priority based on risk level.
    """
    risk_level = row["Risk Level"]

    if risk_level == "High":
        return "Urgent"

    elif risk_level == "Medium":
        return "Moderate"

    else:
        return "Routine"


def add_engineered_features(df):
    """
    Add extra engineered features to help improve model performance.
    """
    df = df.copy()

    df["Age Group"] = pd.cut(
        df["Age"],
        bins=[0, 18, 35, 50, 65, 120],
        labels=[
            "Child",
            "Young Adult",
            "Adult",
            "Senior",
            "Elderly"
        ]
    )

    df["Is Elderly"] = df["Age"].apply(
        lambda x: 1 if x >= 65 else 0
    )

    df["Is Abnormal Test"] = df["Test Results"].apply(
        lambda x: 1 if x == "Abnormal" else 0
    )

    df["Is Emergency"] = df["Admission Type"].apply(
        lambda x: 1 if x == "Emergency" else 0
    )

    return df


def preprocess_data(path="data/healthcare_dataset.csv"):
    """
    Full preprocessing pipeline.
    """
    df = load_data(path)
    df = clean_data(df)

    df["Risk Level"] = df.apply(
        create_risk_level,
        axis=1
    )

    df["Treatment Priority"] = df.apply(
        create_priority,
        axis=1
    )

    df = add_engineered_features(df)

    return df


if __name__ == "__main__":
    df = preprocess_data()

    print(df.head())
    print(df.columns)
    print(df.shape)

    print("\nRisk Level Distribution:")
    print(df["Risk Level"].value_counts())

    print("\nTreatment Priority Distribution:")
    print(df["Treatment Priority"].value_counts())

    print("\nAge Group Distribution:")
    print(df["Age Group"].value_counts())