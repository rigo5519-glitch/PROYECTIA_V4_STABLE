import streamlit as st
import plotly.graph_objects as go

from utils import load_project_master

pm = load_project_master()

dashboard = pm["dashboard"]

st.title("📊 Dashboard Ejecutivo")

c1, c2, c3, c4 = st.columns(4)

c1.metric(
    "VAN",
    f'${dashboard["VAN"]:,.2f}'
)

c2.metric(
    "TIR",
    f'{dashboard["TIR"]:.2f}%'
)

c3.metric(
    "PRI",
    dashboard["PRI"]
)

c4.metric(
    "B/C",
    dashboard["BC"]
)

fig = go.Figure(
    go.Indicator(
        mode="gauge+number",
        value=dashboard["Score"],
        title={"text": "Score General"},
        gauge={
            "axis": {"range": [0, 100]},
            "bar": {"color": "green"}
        }
    )
)

st.plotly_chart(
    fig,
    use_container_width=True
)
