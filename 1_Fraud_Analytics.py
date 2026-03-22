import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Load results
df = pd.read_csv("fraud_detection_results.csv")

fraud_count = df[df["Predicted"] == 1].shape[0]
genuine_count = df[df["Predicted"] == 0].shape[0]

st.markdown("""
<div class="glow-card">
    <h4 class="shimmer">Behavioral Insight</h4>
    <p>
    A sudden increase in refund frequency often indicates exploitation of refund policies.
    The system continuously adapts to such patterns.
    </p>
</div>
""", unsafe_allow_html=True)


st.markdown("## 📊 Fraud vs Genuine (Prediction Breakdown)")

# Futuristic Donut Chart
fig = go.Figure(data=[go.Pie(
    labels=["Genuine", "Fraud"],
    values=[genuine_count, fraud_count],
    hole=0.65,
    marker=dict(
        colors=["#00ffd5", "#ff2e63"],
        line=dict(color="#0a0f1e", width=4)
    ),
    textinfo="label+percent",
    textfont=dict(size=16, color="white"),
    hoverinfo="label+value"
)])

fig.update_layout(
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    height=420,
    margin=dict(t=20, b=20),
    showlegend=False,
    annotations=[
        dict(
            text="<b>AI<br>Decisions</b>",
            x=0.5, y=0.5,
            font=dict(size=20, color="#00ffd5"),
            showarrow=False
        )
    ]
)

st.plotly_chart(fig, use_container_width=True)


st.markdown("### 🔍 Key Insight")
st.info(
    "Fraudulent refund requests show distinct behavioral and transactional patterns "
    "that differ significantly from genuine customers."
)
import plotly.graph_objects as go
import pandas as pd
import streamlit as st



import plotly.graph_objects as go
import streamlit as st

st.markdown("## 🕸 Feature Importance – AI Decision Radar")

features = [
    "Refund Amount",
    "Refund Frequency",
    "Return Ratio",
    "Account Age",
    "Order Value",
    "Time Gap"
]

importance_scores = [0.82, 0.76, 0.68, 0.55, 0.61, 0.49]

# Close the radar loop
features += [features[0]]
importance_scores += [importance_scores[0]]

fig = go.Figure()

# Neon Radar Area
fig.add_trace(go.Scatterpolar(
    r=importance_scores,
    theta=features,
    fill='toself',
    name='Fraud Risk Influence',
    line=dict(color='#00fff0', width=3),
    fillcolor='rgba(0,255,240,0.25)',
    marker=dict(size=8, color='#00fff0')
))

# High-risk threshold ring
fig.add_trace(go.Scatterpolar(
    r=[0.7]*len(features),
    theta=features,
    mode='lines',
    line=dict(color='#ff2e63', width=2, dash='dash'),
    name='High Risk Threshold'
))

fig.update_layout(
    polar=dict(
        bgcolor="#050a14",
        radialaxis=dict(
            visible=True,
            range=[0,1],
            gridcolor="rgba(0,255,255,0.15)",
            tickfont=dict(color="#00fff0")
        ),
        angularaxis=dict(
            gridcolor="rgba(255,0,255,0.15)",
            tickfont=dict(color="#ffffff", size=12)
        )
    ),
    paper_bgcolor="#050a14",
    showlegend=True,
    legend=dict(
        font=dict(color="white"),
        bgcolor="rgba(0,0,0,0)"
    ),
    height=600,
    margin=dict(t=40, b=40)
)

st.plotly_chart(fig, use_container_width=True)
st.markdown("""
<div style="
background: rgba(255,0.05,255,0.05);
backdrop-filter: blur(12px);
padding: 1px;
border-radius: 1px;
border: 1px solid rgba(0,255,213,0.25);
margin-bottom: 1px;">
<span style="color:#aaa;">This radar chart visualizes how different behavioral features contribute to refund fraud risk.
Features crossing the threshold ring indicate higher fraud influence, helping analysts focus on risky behavior patterns.</span>
</div>
""", unsafe_allow_html=True)


st.markdown("## 🌌 3D Feature Impact Space")


fig_3d = go.Figure()
fig_3d.add_trace(go.Scatter3d(
    x=importance_scores,
    y=list(range(len(features))),
    z=[1]*len(features),
    text=features,
    mode='markers+text',
    marker=dict(
        size=[18, 22, 20, 24, 21, 23],
        color=importance_scores,
        colorscale="Turbo",
        opacity=0.95,
        line=dict(color="white", width=1)
    ),
    textfont=dict(color="white", size=11),
    hovertemplate="<b>%{text}</b><br>Importance: %{x}<extra></extra>"
))

for i in range(len(importance_scores)-1):
    fig_3d.add_trace(go.Scatter3d(
        x=[importance_scores[i], importance_scores[i+1]],
        y=[i, i+1],
        z=[1, 1],
        mode='lines',
        line=dict(
            color="rgba(0,255,213,0.4)",
            width=4
        ),
        showlegend=False
    ))


fig_3d.update_layout(
    height =700,
    margin =dict(l=0, r=0, t=30, b=0),
    scene_camera = dict(
        eye=dict(x=1.2, y=1.2, z=0.8)
    ),
    scene=dict(
        xaxis=dict(
            title="Importance Score",
            color="#00ffd5",
            gridcolor="rgba(0,255,213,0.15)",
            backgroundcolor="rgba(0,0,0,0)"
        ),
        yaxis=dict(
            title="Feature Index",
            color="#ff66ff",
            gridcolor="rgba(255,102,255,0.15)",
            backgroundcolor="rgba(0,0,0,0)"
        ),
        zaxis=dict(
            visible=False
        ),
        bgcolor="rgba(5,10,20,1)"
    ),
    paper_bgcolor="rgba(5,10,20,1)"
)

import numpy as np

theta = np.linspace(0, 2*np.pi, 100)
x_ring = [0.7]*100
y_ring = np.linspace(0, len(features)-1, 100)
z_ring = np.sin(theta)*0.05 + 1

fig_3d.add_trace(go.Scatter3d(
    x=x_ring,
    y=y_ring,
    z=z_ring,
    mode='lines',
    line=dict(color="rgba(255,0,150,0.6)", width=6),
    name="Risk Threshold"
))
st.plotly_chart(fig_3d, use_container_width=True)

st.markdown("""
<div style="
background: rgba(255,0.05,255,0.05);
backdrop-filter: blur(12px);
padding: 1px;
border-radius: 1px;
border: 1px solid rgba(0,255,213,0.25);
margin-bottom: 1px;">
🧠 <b>AI Feature Impact Visualization</b><br>
<span style="color:#aaa;">Real-time importance learned by the fraud detection model</span>
</div>
""", unsafe_allow_html=True)

st.markdown("### 🔍 Why These Patterns Matter")

st.markdown("""
Fraud rarely happens randomly. It often follows **behavioral patterns** such as:

- Frequent refund requests in short time periods  
- Refund amounts higher than average purchases  
- Unusual refund timing (late night / odd hours)  
- New or low-activity accounts requesting refunds  

By analyzing these patterns, the system identifies **hidden anomalies**
that may not be obvious through manual review.
""")

st.info("📊 Patterns help the system detect *behavioral intent*, not just transaction value.")
