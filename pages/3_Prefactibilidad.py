import streamlit as st

from utils import (
    load_project_master
)

pm = load_project_master()

st.title(
    "📘 Prefactibilidad"
)

st.subheader(
    "Diagnóstico"
)

st.json(
    pm["diagnostic"]
)

st.subheader(
    "Mercado"
)

st.json(
    pm["market"]
)

st.subheader(
    "Marketing"
)

st.json(
    pm["marketing"]
)

st.subheader(
    "Localización"
)

st.json(
    pm["localization"]
)

st.subheader(
    "Inversión"
)

st.json(
    pm["investment"]
)

st.subheader(
    "VAN"
)

st.json(
    pm["van"]
)
