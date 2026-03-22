import streamlit as st
import plotly.graph_objects as go
import numpy as np

# -------------------- PAGE CONFIG --------------------
st.set_page_config(
    page_title="AI Risk Simulator",
    page_icon="⚠️",
    layout="wide"
)

# -------------------- CYBERPUNK CSS --------------------
st.markdown("""
<style>
body {
    background: radial-gradient(circle at top, #050a14, #000);
    color: white;
}

.glow-title {
    text-align: center;
    font-size: 40px;
    font-weight: bold;
    color: #00fff0;
    text-shadow: 0 0 15px #00fff0;
}

.subtitle {
    text-align: center;
    color: #aaa;
    margin-bottom: 30px;
}

@keyframes pulse {
  0% { text-shadow: 0 0 5px #ff2e63; }
  50% { text-shadow: 0 0 25px #ff2e63; }
  100% { text-shadow: 0 0 5px #ff2e63; }
}

.pulse-text {
    animation: pulse 2s infinite;
    color: #ff2e63;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# -------------------- HEADER --------------------
st.markdown('<div class="glow-title">⚠️ AI FRAUD RISK SIMULATOR</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Real-Time Risk Intelligence Engine</div>', unsafe_allow_html=True)

st.markdown('<div class="pulse-text">🧠 SYSTEM STATUS: ACTIVE & SCANNING</div>', unsafe_allow_html=True)

st.divider()



# -------------------- SLIDERS --------------------
st.subheader("🎛 Control Fraud Indicators")

col1, col2, col3 = st.columns(3)

with col1:
    refund_freq = st.slider("Refund Frequency", 0.0, 1.0, 0.6)
    refund_amt = st.slider("Refund Amount", 0.0, 1.0, 0.7)

with col2:
    order_value = st.slider("Order Value", 0.0, 1.0, 0.4)
    account_age = st.slider("Account Age", 0.0, 1.0, 0.5)

with col3:
    time_gap = st.slider("Time Gap", 0.0, 1.0, 0.6)
    return_ratio = st.slider("Return Ratio", 0.0, 1.0, 0.65)

# -------------------- RISK SCORE CALCULATION --------------------
features = [
    refund_freq,
    refund_amt,
    order_value,
    account_age,
    time_gap,
    return_ratio
]


risk_score = round(sum(features) / len(features) * 100, 2)

# -------------------- RISK LEVEL --------------------
if risk_score < 35:
    risk_label = "LOW RISK"
    risk_color = "#00ff9c"
elif risk_score < 70:
    risk_label = "MEDIUM RISK"
    risk_color = "#ffae00"
else:
    risk_label = "HIGH RISK"
    risk_color = "#ff2e63"


decision_color = "#00ff99" if risk_score < 40 else "#ffaa00" if risk_score < 70 else "#ff0033"

st.markdown(f"""
<div class="glow-card" style="border-color:{decision_color};">
    <h3 class="shimmer">AI Decision Locked</h3>
    <p><strong>Risk Score:</strong> {risk_score}</p>
    <p>The system has evaluated behavioral and transactional signals.</p>
</div>
""", unsafe_allow_html=True)


# -------------------- GAUGE CHART --------------------
gauge = go.Figure(go.Indicator(
    mode="gauge+number",
    value=risk_score,
    number={'suffix': "%", 'font': {'size': 48}},
    gauge={
        'axis': {'range': [0, 100]},
        'bar': {'color': risk_color},
        'steps': [
            {'range': [0, 35], 'color': '#003f2d'},
            {'range': [35, 70], 'color': '#403000'},
            {'range': [70, 100], 'color': '#400018'}
        ],
        'threshold': {
            'line': {'color': "#ff2e63", 'width': 4},
            'thickness': 0.8,
            'value': 80
        }
    }
))

gauge.update_layout(
    height=400,
    paper_bgcolor="#050a14",
    font=dict(color="white"),
    transition=dict(duration=700, easing="cubic-in-out")
)

# -------------------- RADAR CHART --------------------
labels = [
    "Refund Frequency",
    "Refund Amount",
    "Order Value",
    "Account Age",
    "Time Gap",
    "Return Ratio"
]

radar = go.Figure()

radar.add_trace(go.Scatterpolar(
    r=features + [features[0]],
    theta=labels + [labels[0]],
    fill='toself',
    name='Risk Pattern',
    line=dict(color="#00fff0", width=3),
    fillcolor='rgba(0,255,240,0.2)'
))

radar.update_layout(
    polar=dict(
        bgcolor="#050a14",
        radialaxis=dict(visible=True, range=[0,1], gridcolor="#1f2a44"),
        angularaxis=dict(gridcolor="#1f2a44")
    ),
    showlegend=False,
    paper_bgcolor="#050a14",
    height=400,
    font=dict(color="white")
)

# -------------------- DISPLAY --------------------
c1, c2 = st.columns(2)

with c1:
    st.plotly_chart(gauge, use_container_width=True)

with c2:
    st.plotly_chart(radar, use_container_width=True)

# -------------------- RESULT --------------------
st.markdown(f"""
<h2 style="text-align:center; color:{risk_color}; text-shadow:0 0 15px {risk_color};">
🧪 AI DECISION: {risk_label}
</h2>
""", unsafe_allow_html=True)

st.markdown("""
<div style="text-align:center; color:#aaa;">
This simulation mimics a real-time fraud scoring engine used in AI-powered financial systems.
</div>
""", unsafe_allow_html=True)

st.markdown("----")
st.markdown("### 🔎 Why This Decision Was Made")

if risk_score >= 70:
    st.error("""
    🚨 **High Risk Detected**
    
    This refund was flagged due to:
    - High refund frequency  
    - Unusual refund amount  
    - Short account history  
    """)
elif risk_score >= 40:
    st.warning("""
    ⚠️ **Medium Risk**
    
    This case shows some unusual behavior:
    - Refund timing anomaly  
    - Moderate deviation from normal spending  
    """)
else:
    st.success("""
    ✅ **Low Risk**
    
    This refund aligns with normal customer behavior:
    - Consistent purchase history  
    - Reasonable refund amount  
    - No abnormal patterns detected  
    """)

st.caption("🧠 The AI explains *why*, not just *what*.")
