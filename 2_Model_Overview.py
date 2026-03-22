import streamlit as st

st.set_page_config(page_title="Model Overview", layout="wide")

# ================== NEON + ANIMATION CSS ==================
st.markdown("""
<style>

/* Page fade-in */
@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

/* Card slide-up */
@keyframes slideUp {
  from {
    transform: translateY(40px);
    opacity: 0;
  }
  to {
    transform: translateY(0);
    opacity: 1;
  }
}

/* Neon pulse */
@keyframes pulseGlow {
  0% { box-shadow: 0 0 12px rgba(0,255,247,0.2); }
  50% { box-shadow: 0 0 28px rgba(0,255,247,0.45); }
  100% { box-shadow: 0 0 12px rgba(0,255,247,0.2); }
}

body {
    background:
        radial-gradient(circle at 20% 10%, rgba(0, 255, 247, 0.08), transparent 40%),
        radial-gradient(circle at 80% 30%, rgba(0, 140, 255, 0.08), transparent 45%),
        radial-gradient(circle at bottom, rgba(0, 255, 180, 0.05), transparent 50%),
        linear-gradient(180deg, #020617, #050a1f, #020617);
    color: purple;
    animation: fadeIn 1.2s ease-in-out;
}
@keyframes slowGlow {
  0% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
  100% { background-position: 0% 50%; }
}

body {
    background-size: 200% 200%;
    animation: slowGlow 18s ease infinite, fadeIn 1.2s ease-in-out;
}


.neon-title {
    font-size: 48px;
    font-weight: 800;
    color: #00fff7;
    text-shadow: 0 0 2px #00fff9, 0 0 10px #00fff7;
}

.subtitle {
    color: #9ca3af;
    font-size: 18px;
}

.glass-card {
    background: rgba(255, 255, 255, 0.06);
    border-radius: 20px;
    padding: 28px;
    margin-bottom: 28px;
    border: 1px solid rgba(0, 255, 247, 0.25);
    box-shadow: 0 0 18px rgba(0, 255, 247, 0.15);
    animation: slideUp 0.9s ease forwards, pulseGlow 4s infinite;
    transition: transform 2.5s ease;
}

.glass-card:hover {
    transform: translateY(-6px) scale(10.1);
}

.section-title {
    font-size: 26px;
    color: #7efcff;
    font-weight: 700;
    margin-bottom: 10px;
}

.bullet {
    font-size: 18px;
    line-height: 1.7;
}

.footer-glow {
    color: #00fff7;
    text-shadow: 0 0 15px #00fff7;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="glow-card">
    <h4 class="shimmer">Explainable AI Core</h4>
    <p>
    The model evaluates multiple features together and assigns importance dynamically.
    No static rules. No black-box decisions.
    </p>
</div>
""", unsafe_allow_html=True)


# ================== TITLE ==================
st.markdown("""
<div class="neon-title">🧠 Model & System Overview</div>
<p class="subtitle">
A futuristic look into the intelligence behind the AI Refund Fraud Detection System
</p>
<br>
""", unsafe_allow_html=True)

# ================== ROW 1 ==================
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="glass-card">
        <div class="section-title">🤖 Machine Learning Models Used</div>
        <ul class="bullet">
            <li>Random Forest</li>
            <li><b>XGBoost (Final Model)</b></li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="glass-card">
        <div class="section-title">📌 Why XGBoost?</div>
        <ul class="bullet">
            <li>Efficient handling of class imbalance</li>
            <li>Detects complex non-linear fraud patterns</li>
            <li>High recall for fraudulent refund detection</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# ================== ROW 2 ==================
col3, col4 = st.columns(2)

with col3:
    st.markdown("""
    <div class="glass-card">
        <div class="section-title">📊 Evaluation Metrics</div>
        <ul class="bullet">
            <li>Accuracy</li>
            <li>Precision</li>
            <li>Recall</li>
            <li>F1-Score</li>
            <li>ROC-AUC Curve</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="glass-card">
        <div class="section-title">⚙️ System Workflow</div>
        <ol class="bullet">
            <li>Transaction data ingestion</li>
            <li>Preprocessing & feature engineering</li>
            <li>ML model prediction</li>
            <li>Fraud flagging</li>
            <li>Dashboard visualization</li>
        </ol>
    </div>
    """, unsafe_allow_html=True)

# ================== FOOTER ==================
st.markdown("""
<div class="glass-card" style="text-align:center;">
    <div class="section-title">🌍 Real-World Impact</div>
    <p class="bullet">
        This AI-driven system helps e-commerce platforms reduce financial losses,
        detect refund abuse early, and preserve trust with genuine customers.
    </p>
    <h3 class="footer-glow">🚀 Intelligent • Scalable • Future-Ready</h3>
</div>
""", unsafe_allow_html=True)


st.markdown("### 🧠 How the AI Makes Decisions")

st.markdown("""
The model evaluates multiple features together to make a prediction.
No single feature can decide fraud on its own.
""")

st.markdown("""
**Examples of influential features:**
- Refund frequency  
- Time gap between purchases and refunds  
- Transaction amount deviation  
- Account age and activity level  
""")

st.success("""
✅ This model is **explainable** — every decision can be traced back to contributing factors.
""")

st.caption("🔐 Transparency ensures ethical and responsible AI usage.")



st.success("System Ready for Deployment 🚀")
