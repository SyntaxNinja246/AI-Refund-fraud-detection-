
import streamlit as st
st.markdown("""
<style>

/* Background */
.stApp {
    background: radial-gradient(circle at top, #0f2027, #000123);
    color: #e0e0e1;
}

/* Titles */
h1, h2, h3 {
    color: #00fff7;
    text-shadow: 0 0 10px #00fff7;
}

/* Metric cards */
div[data-testid="metric-container"] {
    background-color: rgba(0, 0, 0, 0.7);
    border: 1px solid #00fff7;
    border-radius: 12px;
    padding: 15px;
    box-shadow: 0 0 15px #00fff7;
}

/* Tables */
.stDataFrame {
    background-color: black;
    border: 1px solid #ff00ff;
    box-shadow: 0 0 12px #ff00ff;
}

/* Scrollbar */
::-webkit-scrollbar {
    width: 8px;
}
::-webkit-scrollbar-thumb {
    background: #00fff7;
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="glow-card">
    <span class="pulse-dot"></span>
    <strong style="margin-left:10px;">System Status:</strong> 
    <span class="shimmer">Monitoring Refund Activity</span>
</div>
""", unsafe_allow_html=True)


import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="AI Refund Fraud Detection",
    layout="wide"
)

st.title("🛒 AI Refund Fraud Detection Dashboard")

df = pd.read_csv("fraud_detection_results.csv")

total = len(df)
fraud = len(df[df['Predicted'] == 1])
genuine = total - fraud

col1, col2, col3 = st.columns(3)

col1.metric("Total Refund Requests", total)
col2.metric("Suspicious Refunds", fraud)
col3.metric("Genuine Refunds", genuine)

st.subheader("⚠ Suspicious Refund Requests")
st.dataframe(df[df['Predicted'] == 1])

import streamlit as st
import random

st.markdown("""
<style>
.cyber-card {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
    border-radius: 18px;
    padding: 25px;
    box-shadow: 0 0 25px rgba(0,255,255,0.25);
    animation: pulse 3s infinite;
}

@keyframes pulse {
    0% { box-shadow: 0 0 15px rgba(0,255,255,0.2); }
    50% { box-shadow: 0 0 30px rgba(0,255,255,0.6); }
    100% { box-shadow: 0 0 15px rgba(0,255,255,0.2); }
}

.verdict-fraud {
    color: #ff4b4b;
    font-size: 28px;
    font-weight: bold;
}

.verdict-genuine {
    color: #2bff88;
    font-size: 28px;
    font-weight: bold;
}

.reason {
    color: #e0f7fa;
    font-size: 16px;
    margin-top: 8px;
}

.confidence {
    font-size: 22px;
    font-weight: bold;
    color: cyan;
}
</style>
""", unsafe_allow_html=True)

st.subheader("🧠 Live Refund Case Analyzer")

case_id = st.selectbox(
    "Select Refund Case ID",
    ["RF-2041", "RF-2098", "RF-3102", "RF-4219", "RF-5871"]
)

# Fake AI reasoning engine (demo-friendly)
fraud_probability = random.randint(40, 95)

reasons = [
    "Multiple refund attempts detected in short time window",
    "Device fingerprint mismatch across sessions",
    "Unusual refund amount compared to order history",
    "High-risk location anomaly detected",
    "Repeated card usage across multiple accounts"
]

selected_reasons = random.sample(reasons, k=3)

is_fraud = fraud_probability > 65

st.markdown("<div class='cyber-card'>", unsafe_allow_html=True)

st.markdown(f"### 📄 Case ID: `{case_id}`")

if is_fraud:
    st.markdown("<div class='verdict-fraud'>⚠️ FRAUD LIKELY</div>", unsafe_allow_html=True)
else:
    st.markdown("<div class='verdict-genuine'>✅ GENUINE REFUND</div>", unsafe_allow_html=True)

st.markdown("---")


st.markdown(f"<div class='confidence'>🔐 Fraud Confidence: {fraud_probability}%</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
st.markdown("---")  

st.markdown("""
### 🧠 How the AI Refund Analyzer Works

This system simulates how an AI model evaluates refund requests in real-world platforms 
such as e-commerce and banking applications.

Each **Refund Case ID** represents a customer refund request.  
The AI analyzes multiple hidden factors like transaction behavior, refund frequency, 
amount patterns, and risk signals.

Based on this analysis, the model classifies the request as either:
- ✅ **Genuine Refund** (low risk, auto-approved)
- ⚠️ **Fraud Likely** (high risk, requires investigation)

This approach focuses on **explainable AI**, allowing humans to understand *why* a decision 
was made — not just the final result.
""")


st.markdown("---")

st.markdown(
    "<h3 style='color:#00fff7;'>🤖 AI System Status</h3>",
    unsafe_allow_html=True
)

c1, c2, c3 = st.columns(3)

c1.success("Model Loaded")
c2.success("Fraud Detection model Active")
c3.success("Data Synced")

st.caption("Powered by XGBoost + Behavioral Pattern Analysis")
