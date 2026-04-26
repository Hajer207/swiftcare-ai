# 🩺 SwiftCare AI  
### Intelligent Clinical Risk Prediction and Smart Triage Support

---

## 📌 Overview

SwiftCare AI is a Machine Learning-powered Clinical Decision Support System designed to assist healthcare providers in:

- Predicting patient medical conditions  
- Assessing risk levels  
- Prioritizing treatment urgency  
- Triggering critical alerts for high-risk patients  
- Supporting faster and smarter triage decisions

---

## 🎯 Project Objective

Traditional patient triage can be time-consuming and inconsistent.

This project aims to improve:

✅ Patient safety  
✅ Early critical case detection  
✅ Decision-making efficiency  
✅ Smart treatment prioritization

---

## 🚨 Problem Statement

Current hospital triage often relies on:

- Manual prioritization  
- Rule-based workflows  
- Human judgment alone

### Challenges:
- Delays in identifying critical patients  
- Inconsistent prioritization decisions  
- Pressure on medical staff  
- Possible medical risk due to late escalation

---

## 🤖 Machine Learning Framing

### Problem Type
**Multiclass Classification**

### Why Machine Learning?
Machine learning was used to:

- Predict medical condition automatically  
- Classify risk severity  
- Support triage prioritization  
- Reduce manual dependency

---

## 🧠 Model Used

### AutoML Framework
**AutoGluon Tabular**

### Best Model Selected
🏆 WeightedEnsemble_L2

AutoGluon automatically tested multiple models and selected the best performing ensemble model.

---

## 📊 Dataset

Healthcare structured dataset:

- 55,500 rows  
- 14 features

### Input Features
- Age  
- Gender  
- Blood Type  
- Admission Type  
- Medication  
- Test Results

### Prediction Target
- Patient Medical Condition

---

## ⚙️ Feature Engineering

Engineered features added:

- Age Group  
- Is Elderly  
- Is Abnormal Test  
- Is Emergency

### Purpose
These engineered features improved prediction behavior and triage logic.

---

## 📈 Model Performance

### Accuracy
**18%**

Baseline:
17%

Improved using:
- Feature Engineering  
- AutoML Optimization

---

## 🩺 Application Features

SwiftCare AI provides:

### 🔍 Prediction Module
- Predict patient condition

### ⚠ Risk Assessment
- Low / Medium / High Risk

### 🚑 Treatment Priority
- Routine  
- Moderate  
- Urgent

### 🚨 Critical Alerts
Automatic emergency alerts for critical cases

### 📋 Clinical Recommendations
Decision-support recommendations generated automatically

### 📄 Patient Report
Downloadable patient report

---

## 🖥️ Streamlit Interface

Interactive prototype built using **Streamlit**

Run locally:

```bash
streamlit run app.py
```

Access in browser:

```text
http://localhost:8501
```

---

## 📂 Project Structure

```text
SwiftCare AI/
│
├── AutogluonModels/
│   └── swiftcare_model/
│
├── data/
│   └── healthcare_dataset.csv
│
├── src/
│   ├── __init__.py
│   ├── logic.py
│   ├── preprocessing.py
│   └── styles.py
│
├── app.py
├── train.py
├── requirements.txt
└── README.md
```

---

## 🛠 Technologies Used

- Python  
- AutoGluon  
- Streamlit  
- Pandas  
- Scikit-learn

---

## ✅ Success Criteria

Project success is measured by:

- Accurate triage support  
- Early high-risk patient detection  
- Functional deployment prototype  
- Decision-support usefulness

---

## 🔮 Future Improvements

Possible extensions:

- Real hospital data integration  
- Improved model accuracy  
- Real-time healthcare deployment  
- Cloud production deployment  
- Integration with hospital information systems

---

## 🚀 Deployment

Prototype deployed locally with Streamlit.

(Cloud deployment optional)

---

## 👩‍💻 Author

**Developed by Hajer Abdullah**

Machine Learning Project Prototype  
