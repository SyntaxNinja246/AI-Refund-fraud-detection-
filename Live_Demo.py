import time
import random
import streamlit as st

st.markdown(
    """
    <style>
    .pulse {
        animation: pulse 2s infinite;
        color: #00ffe1;
        font-weight: bold;
    }
    @keyframes pulse {
        0% {opacity: 0.6;}
        50% {opacity: 1;}
        100% {opacity: 0.6;}
    }
    </style>
    <div class="pulse">🧪 Demo Mode Active — Live AI Simulation</div>
    """,
    unsafe_allow_html=True
)



if "demo_mode" not in st.session_state:
    st.session_state.demo_mode = False

st.sidebar.markdown("### ⚙️ Controls")
st.session_state.demo_mode = st.sidebar.toggle(
    "🧪 Demo Mode",
    value=st.session_state.demo_mode
)



st.success(
    """
    🧪 **Demo Mode ON**

    This system is now simulating real-time AI behavior.
    Values update automatically to demonstrate:
    
    • Live risk scoring
    
    • Explainable decisions
    
    • System responsiveness
    """
)


st.markdown("## 🧠 Live Fraud Risk Pulse")

risk_placeholder = st.empty()
explain_placeholder = st.empty()

if st.session_state.demo_mode:
    for _ in range(5):
        risk = round(random.uniform(0.2, 0.95), 2)

        risk_placeholder.metric(
            label="⚠️ System Risk Score",
            value=risk,
            delta="Live signal update"
        )

        explain_placeholder.markdown(
            f"""
            🧠 **What’s happening?**  
            The AI is continuously analyzing refund behavior patterns.
            
            🔍 Current signal strength indicates  
            **{"LOW" if risk < 0.4 else "MODERATE" if risk < 0.7 else "HIGH"} risk activity**.
            """
        )

        time.sleep(1)
else:
    risk_placeholder.metric(
        "⚠️ System Risk Score",
        0.42,
        "Stable"
    )

with st.expander("💡 Why am I seeing this?"):
    st.write(
        """
        The system continuously monitors refund behavior such as:
        • Frequency of refund requests  
        • Time gaps between purchases and refunds  
        • Device and account consistency  

        During Demo Mode, values change automatically to show
        how the AI reacts in real-time.
        """
    )

risk_slider = st.slider(
    "📊 Simulated Risk Factors",
    0.0, 1.0,
    random.uniform(0.3, 0.8) if st.session_state.demo_mode else 0.5
)

decision = "GENUINE" if risk_slider < 0.6 else "FRAUD"

st.markdown(
    f"""
    ### 🔍 AI Decision
    **{decision} REFUND**
    """
)

st.info(
    f"""
    🧠 **Why this decision?**  
    The combined risk signals resulted in a score of `{risk_slider:.2f}`.
    
    Values above `0.6` indicate abnormal behavior patterns.
    """
)

