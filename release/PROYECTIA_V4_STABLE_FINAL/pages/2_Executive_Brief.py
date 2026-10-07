import streamlit as st

from utils import (
    load_project_master
)

pm = load_project_master()

st.title(
    "📄 Executive Brief"
)

st.subheader(
    "Proyecto"
)

st.write(
    pm["idea"]["idea_original"]
)

st.subheader(
    "Problema"
)

st.write(
    pm["diagnostic"][
        "problema_central"
    ]
)

st.subheader(
    "Objetivo"
)

st.write(
    pm["objective_tree"][
        "objetivo_general"
    ]
)

st.subheader(
    "Ubicación"
)

st.write(
    pm["localization"][
        "ubicacion_optima"
    ]
)

st.subheader(
    "Factibilidad"
)

st.write(
    pm["dashboard"][
        "Clasificacion"
    ]
)
