import streamlit as st
import pandas as pd
import plotly.express as px

from src.logic import predict_patient, critical_alert
from src.styles import load_css


st.set_page_config(
    page_title="SwiftCare AI",
    layout="wide"
)

st.markdown(load_css(), unsafe_allow_html=True)


st.markdown(
    """
    <div class="main-title">
        🏥 SwiftCare AI
    </div>

    <div class="subtitle">
        Intelligent Patient Risk Prediction and Smart Clinical Triage Support
    </div>
    """,
    unsafe_allow_html=True
)


st.sidebar.header("🩺 Patient Information")

age = st.sidebar.slider("Age", 1, 100, 45)

gender = st.sidebar.selectbox(
    "Gender",
    ["Male", "Female"]
)

blood_type = st.sidebar.selectbox(
    "Blood Type",
    ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
)

admission_type = st.sidebar.selectbox(
    "Admission Type",
    ["Emergency", "Urgent", "Elective"]
)

medication = st.sidebar.selectbox(
    "Medication",
    ["Aspirin", "Ibuprofen", "Paracetamol", "Penicillin"]
)

test_results = st.sidebar.selectbox(
    "Test Results",
    ["Normal", "Abnormal", "Inconclusive"]
)

risk_level = st.sidebar.selectbox(
    "Risk Level",
    ["Low", "Medium", "High"]
)

treatment_priority = st.sidebar.selectbox(
    "Treatment Priority",
    ["Routine", "Moderate", "Urgent"]
)


# ===============================
# Clinical Dashboard Section
# ===============================

st.markdown("## 📊 Clinical Triage Dashboard")

metric_col1, metric_col2, metric_col3 = st.columns(3)

with metric_col1:
    st.metric(
        label="Total Patients",
        value="55,500"
    )

with metric_col2:
    st.metric(
        label="Critical Cases",
        value="19,970"
    )

with metric_col3:
    st.metric(
        label="High Risk %",
        value="36%"
    )


risk_df = pd.DataFrame({
    "Risk Level": ["Low", "Medium", "High"],
    "Count": [10439, 25091, 19970]
})

priority_df = pd.DataFrame({
    "Treatment Priority": ["Routine", "Moderate", "Urgent"],
    "Count": [10439, 25091, 19970]
})


chart_col1, chart_col2 = st.columns(2)

with chart_col1:
    risk_fig = px.bar(
        risk_df,
        x="Risk Level",
        y="Count",
        title="Risk Level Distribution",
        text="Count"
    )

    st.plotly_chart(
        risk_fig,
        use_container_width=True
    )


with chart_col2:
    priority_fig = px.pie(
        priority_df,
        names="Treatment Priority",
        values="Count",
        title="Treatment Priority Distribution"
    )

    st.plotly_chart(
        priority_fig,
        use_container_width=True
    )


st.markdown("---")


# ===============================
# Patient Prediction Section
# ===============================

if st.button("🔍 Predict Patient Condition"):

    disease = predict_patient(
        age,
        gender,
        blood_type,
        admission_type,
        medication,
        test_results,
        risk_level,
        treatment_priority
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            f"""
            <div class="card">
                <div class="metric-title">Predicted Condition</div>
                <div class="metric-value">{disease}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            f"""
            <div class="card">
                <div class="metric-title">Risk Level</div>
                <div class="metric-value">{risk_level}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            f"""
            <div class="card">
                <div class="metric-title">Treatment Priority</div>
                <div class="metric-value">{treatment_priority}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    if critical_alert(risk_level, treatment_priority):
        recommendation = "Immediate medical attention is required."
        st.markdown(
            """
            <div class="critical-box">
                🚨 CRITICAL ALERT: Immediate medical attention is required.
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        recommendation = "Continue standard clinical assessment."
        st.markdown(
            """
            <div class="safe-box">
                ✅ No critical alert detected. Continue standard clinical assessment.
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("### 📝 Clinical Recommendations")

    if risk_level == "High":
        st.warning(
            """
            - Immediate physician review is recommended.
            - Prioritize urgent triage pathway.
            - Continuous monitoring is advised.
            """
        )

    elif risk_level == "Medium":
        st.info(
            """
            - Moderate monitoring is advised.
            - Follow-up diagnostic assessment is recommended.
            - Re-evaluate if symptoms worsen.
            """
        )

    else:
        st.success(
            """
            - Routine care pathway is appropriate.
            - Standard follow-up is recommended.
            """
        )

    report = f"""
SwiftCare AI - Patient Report
=============================

Predicted Condition: {disease}

Patient Information:
- Age: {age}
- Gender: {gender}
- Blood Type: {blood_type}
- Admission Type: {admission_type}
- Medication: {medication}
- Test Results: {test_results}

AI Triage Output:
- Risk Level: {risk_level}
- Treatment Priority: {treatment_priority}

Clinical Recommendation:
{recommendation}

Note:
This report is generated by SwiftCare AI to support clinical decision-making.
Final medical decisions should be made by qualified healthcare professionals.
"""

    st.download_button(
        label="📄 Download Patient Report",
        data=report,
        file_name="swiftcare_patient_report.txt",
        mime="text/plain"
    )