# 🏥 SwiftCare AI  
## Intelligent Clinical Risk Prediction and Smart Triage Support System

## Overview
SwiftCare AI is a machine learning–powered clinical decision support system designed to assist healthcare professionals in faster and more consistent triage decisions.

The system predicts a patient’s potential medical condition, classifies risk level, recommends treatment priority, and highlights critical cases requiring immediate attention.

---

## Problem Statement
Traditional patient triage often relies on manual assessment and clinician judgment, which can lead to:

- Delayed identification of critical cases  
- Inconsistent prioritization between practitioners  
- Increased pressure on medical staff during high patient volume  
- Potential delays in urgent treatment

SwiftCare AI addresses these challenges using data-driven prediction and intelligent triage support.

---

## Project Objectives
This project aims to:

- Predict the patient's possible medical condition  
- Classify patient risk level (Low / Medium / High)  
- Recommend treatment priority (Routine / Moderate / Urgent)  
- Generate critical alerts for high-risk urgent cases  
- Provide downloadable AI-assisted patient reports

---

## Machine Learning Tasks
### 1. Disease Prediction
Multi-class classification model predicts likely medical condition.

### 2. Risk Classification
Patients are categorized into:
- Low Risk
- Medium Risk
- High Risk

### 3. Treatment Priority Recommendation
System recommends:
- Routine
- Moderate
- Urgent

---

## Dataset
Dataset used:

Healthcare Dataset  
Records: 55,500 patients

Features used:

- Age  
- Gender  
- Blood Type  
- Admission Type  
- Medication  
- Test Results

Removed features:
- Billing Amount (removed as non-clinical feature)
- Administrative identifiers

---

## Feature Engineering
Custom engineered features include:

### Risk Level Logic
Risk level is generated based on:

- Age  
- Admission Type  
- Test Results

Examples:

- Emergency + Abnormal → High Risk  
- Elderly + Urgent Admission → High Risk  
- Abnormal Tests → Medium Risk

---

## Model
Algorithm Used:

- Random Forest Classifier

Pipeline Includes:

- Data preprocessing  
- Categorical encoding  
- Train/Test split  
- Model training and evaluation

Baseline Accuracy:

```text
0.27
```

(Initial baseline model for prototype purposes)

---

## Deployment
Interactive Streamlit application includes:

✔ Patient data input  
✔ Disease prediction  
✔ Risk assessment  
✔ Treatment priority recommendation  
✔ Critical alert detection  
✔ Clinical recommendations  
✔ Downloadable patient report

---

## Critical Alert Example
If:

```text
Risk Level = High
Treatment Priority = Urgent
```

System triggers:

```text
🚨 Critical Alert:
Immediate medical attention required
```

---

## Project Structure

```text
SwiftCare-AI/
│
├── data/
│   └── healthcare_dataset.csv
│
├── src/
│   ├── preprocessing.py
│   ├── logic.py
│   └── styles.py
│
├── app.py
├── train.py
├── requirements.txt
└── README.md
```

---

## Installation

Clone repository:

```bash
git clone https://github.com/Hajer207/swiftcare-ai.git
cd swiftcare-ai
```

Create virtual environment:

```bash
python -m venv .venv
```

Activate:

Windows:
```bash
.venv\Scripts\activate
```

Install requirements:

```bash
pip install -r requirements.txt
```

---

## Run the Project

Train model:

```bash
python train.py
```

Run application:

```bash
streamlit run app.py
```

---

## Success Criteria
Project success is measured by:

- Accurate risk classification  
- Faster triage support  
- Clear critical case detection  
- Practical deployment usability

---

## Future Improvements
Potential enhancements:

- Auto-calculated risk scoring
- Explainable AI (Feature Importance)
- PDF clinical reports
- Live hospital triage dashboard
- Improved model accuracy using AutoGluon/XGBoost

---

## Technologies Used
- Python  
- Pandas  
- Scikit-learn  
- Joblib  
- Streamlit  
- Git / GitHub

---

## Author
Developed as a Machine Learning project prototype for intelligent healthcare decision support.

Hajer
