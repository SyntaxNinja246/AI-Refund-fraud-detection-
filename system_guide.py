import streamlit as st

st.set_page_config(
    page_title="System Guide",
    page_icon="🧭",
    layout="wide"
)

st.markdown("""
<style>
.guide-card {
    background: linear-gradient(135deg, rgba(0,255,255,0.08), rgba(255,0,255,0.05));
    border: 1px solid rgba(0,255,255,0.25);
    border-radius: 18px;
    padding: 22px;
    margin-bottom: 22px;
    transition: all 0.35s ease;
}

.guide-card:hover {
    box-shadow: 0 0 28px rgba(0,255,255,0.55);
    transform: translateY(-4px);
}

.guide-step {
    font-size: 18px;
    font-weight: 600;
    color: #00fff0;
}

.guide-sub {
    color: #c7c7c7;
    margin-top: 6px;
    font-size: 15px;
}

.signal {
    color: #00ff99;
    font-weight: 600;
}

.warning {
    color: #ff4d4d;
    font-weight: 600;
}

.typing {
    border-right: 2px solid #00fff0;
    white-space: nowrap;
    overflow: hidden;
    animation: typing 3s steps(40) forwards;
}

@keyframes typing {
    from { width: 0; }
    to { width: 100%; }
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<h1>🧭 AI System Guide</h1>
<h5 class="typing">
This is not a dashboard. This is the control manual of an intelligent fraud detection system.
</h5>
""", unsafe_allow_html=True)


st.markdown("""
<div class="guide-card">
    <span class="step-badge">STEP 1</span>
    <h3>📊 Dashboard — System Awareness</h3>
    <p>
        This is the control center. It provides a real-time snapshot of refund activity,
        system health, and overall fraud exposure.
            It gives a quick overview of refund activity across the system and 
            shows how many refunds are happening, how risky they look,
        and whether fraud levels are normal or increasing
    </p>
            <p style="color:#cfd8ff;">
            👉 <b>In simple words:</b> This is the system’s “health check screen”.
            </p>
    <p style="color:#00fff0;">
        💡 Why it matters: Early signals prevent financial loss before escalation.
            It helps teams notice problems early before money is lost.
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="guide-card">
    <span class="step-badge">STEP 2</span>
    <h3>🔍 Fraud Analytics — Pattern Detection</h3>
    <p>
        The system analyzes refund behavior patterns such as frequency spikes,
        abnormal refund ratios, and timing irregularities.
             This section analyzes refund behavior in detail.
        It looks for unusual patterns like too many refunds,
        high refund amounts, or strange timing.
    </p>
            <p style="color:#cfd8ff;">
            👉 <b>In simple words:</b> The system is asking,
            “Does this behavior look normal or unusual?>
            </p>
    <p style="color:#00fff0;">
        💡 Why it matters: Fraud rarely happens once — patterns reveal intent.
            Fraud usually follows patterns, not accidents.
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="guide-card">
    <span class="step-badge">STEP 3</span>
    <h3>🧠 Model Overview — Explainable Intelligence</h3>
    <p>
        The AI model evaluates feature importance and relationships instead of
        relying on hard-coded rules.
             This page explains how the AI model makes decisions.
        It shows which factors influence risk the most,
        such as refund frequency, amount, or return ratio.
    </p>
            <p style="color:#cfd8ff;">
            👉 <b>In simple words:</b> It explains
            “What information the AI cares about the most.”
            </p>
    <p style="color:#00fff0;">
        💡 Why it matters: Every decision can be explained and trusted.
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="guide-card">
    <span class="step-badge">STEP 4</span>
    <h3>⚠️ Risk Simulator — Decision Engine</h3>
    <p>
            This tool lets users test individual refund cases.
        By changing input values, the system calculates a risk score
        and predicts whether the case is safe or risky.
            Individual refund cases are simulated using real-time feature inputs,
        generating a risk score and final decision.
    </p>
            <p style="color:#cfd8ff;">
            👉 <b>In simple words:</b> “If this refund happens,how risky will it be?”
            </p>
    <p style="color:#00fff0;">
        💡 Why it matters: Decisions are data-driven, not assumptions.
    </p>
</div>
""", unsafe_allow_html=True)


st.markdown("""
<div class="guide-card">
    <h3>🔐 Built for Trust & Transparency</h3>
    <p>
        This system follows Explainable AI principles.
        Every risk score is supported by clear reasons,
        not hidden or black-box decisions.
    </p>
    <p style="color:#cfd8ff;">
        👉 <b>In simple words:</b> The AI always explains
        <i>why</i> it made a decision.
    </p>
    <p style="color:#00fff1; font-weight:600;">
        ✔ Clear explanations  
        ✔ Human-friendly decisions  
        ✔ Responsible AI design
    </p>
</div>
""", unsafe_allow_html=True)
