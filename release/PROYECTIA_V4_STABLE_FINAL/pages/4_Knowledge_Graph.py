import streamlit as st

from utils import (
    load_project_master
)

pm = load_project_master()

st.title(
    "🧠 Knowledge Graph"
)

kg = pm["knowledge_graph"]

st.subheader(
    "Nodos"
)

st.json(
    kg["nodos"]
)

st.subheader(
    "Relaciones"
)

st.json(
    kg["relaciones"]
)