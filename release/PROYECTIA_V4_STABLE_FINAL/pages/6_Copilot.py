import streamlit as st

from engines.copilot_engine.copilot_engine import (
    CopilotEngine
)

st.title("🤖 Copilot")

idea = st.text_area(
    "Escriba una idea"
)

if st.button(
    "Analizar"
):

    copilot = CopilotEngine()

    resultado = copilot.generate_report(
        idea
    )

    st.json(
        resultado
    )