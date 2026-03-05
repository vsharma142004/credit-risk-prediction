import streamlit as st
import joblib
import numpy as np
import plotly.express as px
import pandas as pd

# ------------------ Page Config ------------------
st.set_page_config(
    page_title="Credit Risk Prediction",
    page_icon="💳",
    layout="centered"
)


# ------------------ Load Model ------------------
model_data = joblib.load("model.pkl")
model = model_data["model"]
threshold = model_data["threshold"]
coefficients = model_data["coefficients"]
feature_names = model_data["features"]
#------------------ Custom CSS Styling ------------------
st.markdown("""
<style>

/* ---------------- GOOGLE FONT ---------------- */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap');

/* ---------------- GLOBAL FONT ---------------- */
/* Force override Streamlit font */
* {
    font-family: 'IBM Plex Sans' !important;
}

/* ---------------- APP BACKGROUND ---------------- */
.stApp {
    background: linear-gradient(135deg, #0f172a 0%, #0d1117 40%, #1e1b4b 100%);
}


/* ---------------- MAIN TITLE ---------------- */
.main-title {
    font-size: 42px;
    font-weight: 800;
    color: #9D4EDD;
    letter-spacing: 1px;
}

/* ---------------- SUBTITLE ---------------- */
.subtitle {
    font-size: 18px;
    color: #8fa3bf;
    margin-bottom: 30px;
}

/* ---------------- SECTION HEADINGS ---------------- */
h1, h2, h3 {
    font-weight: 700;
    color: #E6EDF3;
}

/* ---------------- METRIC CARDS ---------------- */
[data-testid="stMetric"] {
    background-color: #111827;
    padding: 18px;
    border-radius: 12px;
    border: 1px solid #1f2937;
    box-shadow: 0 0 12px rgba(157, 78, 221, 0.15);
}

/* Metric label */
[data-testid="stMetricLabel"] {
    color: #9CA3AF;
    font-weight: 500;
}

/* Metric value */
[data-testid="stMetricValue"] {
    font-size: 28px;
    font-weight: 700;
    color: #9D4EDD;
}

/* ---------------- BUTTONS ---------------- */
.stButton > button {
    background-color: #9D4EDD;
    color: white;
    font-weight: 600;
    border-radius: 10px;
    padding: 10px 20px;
    border: none;
    transition: all 0.2s ease-in-out;
}

.stButton > button:hover {
    background-color: #7B2CBF;
    box-shadow: 0 0 12px rgba(157, 78, 221, 0.6);
    transform: translateY(-1px);
}

/* ---------------- INPUT FIELDS ---------------- */
input, textarea, select {
    border-radius: 8px !important;
}

/* ---------------- SIDEBAR ---------------- */
section[data-testid="stSidebar"] {
    background-color: #111827;
}

/* ---------------- DIVIDER ---------------- */
hr {
    border: 1px solid #1f2937;
}

/* ---------------- EXPANDER ---------------- */
.streamlit-expanderHeader {
    font-weight: 600;
    color: #9D4EDD;
}

/* ---------------- PROGRESS BAR ---------------- */
.stProgress > div > div > div > div {
    background-color: #9D4EDD;
}

/* ---------------- SMOOTH FADE-IN FOR METRICS ---------------- */
[data-testid="stMetric"] {
    animation: fadeIn 0.6s ease-in;
}

@keyframes fadeIn {
    from {opacity: 0; transform: translateY(5px);}
    to {opacity: 1; transform: translateY(0);}
}

</style>
""", unsafe_allow_html=True)


























# ------------------ Header ------------------
st.markdown('<div class="main-title">💳 Credit Default Risk Assessment</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">AI-powered loan default probability estimation</div>', unsafe_allow_html=True)


st.divider()


# ------------------ Sidebar Disclaimer ------------------
st.sidebar.markdown("## ⚠️ Disclaimer")
st.sidebar.info(
    "This model is built for educational purposes only. "
    "It should not be used for real financial decision-making."
)


# ------------------ Input Section ------------------
st.markdown("### Applicant Financial Details")


col1, col2 = st.columns(2)


with col1:
    income = st.number_input(
    "Annual Income ($)",
    min_value=8000.0,
    max_value=121349.0,
    value=50000.0,
    step=1000.0
)


with col2:
    loan = st.number_input(
    "Loan Amount ($)",
    min_value=1000.0,
    max_value=35158.0,
    value=10000.0,
    step=500.0
)


credit_history = st.selectbox(
    "Credit History",
    options=[1, 0],
    format_func=lambda x: "Good" if x == 1 else "Bad"
)


st.divider()


# ------------------ Prediction ------------------
if st.button("🔍 Assess Risk", use_container_width=True):
    

     # 🔹 Clip extreme values (based on training distribution)
    income = np.clip(income, 0, 1_000_000)
    loan = np.clip(loan, 0, 500_000)

    # Basic feature engineering (same as training)
    log_income = np.log1p(income)
    log_loan = np.log1p(loan)


    
    loan_to_income = loan / (income + 1)

    features = np.array([[log_income, log_loan, loan_to_income, credit_history]])


    probability = model.predict_proba(features)[0][1]
    prediction = int(probability >= threshold)

    


    st.markdown("### Risk Evaluation Result")
    
    if prediction == 0:
       st.success(f"✅ Loan Approved — Default Probability: {probability:.2f}")
    else:
       st.error(f"🚨 High Risk — Loan Rejected — Default Probability: {probability:.2f}")
    st.metric("Default Probability", f"{probability:.2%}")

     
    st.progress(int(probability * 100))

    st.markdown("## 📊 Risk Assessment Dashboard")

    colA, colB = st.columns(2)

    with colA:
      st.metric(
        label="Default Probability",
        value=f"{probability * 100:.1f}%"
    )

    with colB:
      risk_label = "LOW RISK" if prediction == 0 else "HIGH RISK"
      st.metric(
        label="Risk Category",
        value=risk_label
    )
    

    import plotly.graph_objects as go

    fig = go.Figure(go.Indicator(
       mode="gauge+number",
       value=probability * 100,
       title={'text': "Risk Score"},
       gauge={
        'axis': {'range': [0, 100]},
        'bar': {'color': "#FDFDFD"},
        'steps': [
            {'range': [0, 30], 'color': "#00C853"},
            {'range': [30, 70], 'color': "#FFD600"},
            {'range': [70, 100], 'color': "#D50000"},
        ],
    }
    ))

    st.plotly_chart(fig, use_container_width=True)

    st.markdown("### 💡 Financial Risk Insights")

    loan_to_income = loan / (income + 1)

    st.write(f"Loan-to-Income Ratio: **{loan_to_income:.2f}**")

    if loan_to_income > 0.6:
       st.warning("⚠️ High exposure relative to income.")
    elif loan_to_income > 0.4:
       st.info("Moderate exposure level.")
    else:
       st.success("Healthy income-to-loan balance.")

    
    # ---- Influence Calculation ----
    feature_values = {
      "log_income": log_income,
      "log_loan_amount": log_loan,
      "loan_to_income": loan_to_income,
      "credit_history": credit_history
    }

    influence_scores = {}

    for feature in feature_names:
       influence_scores[feature] = feature_values[feature] * coefficients[feature]
 
    

    explain_df = pd.DataFrame({
      "Feature": list(influence_scores.keys()),
      "Impact": list(influence_scores.values())
     })

    explain_df = explain_df.sort_values(by="Impact")

    fig2 = px.bar(
      explain_df,
      x="Impact",
      y="Feature",
      orientation='h',
      title="Feature Contribution to Risk",
     )

    st.plotly_chart(fig2, use_container_width=True)


    
























































































































































