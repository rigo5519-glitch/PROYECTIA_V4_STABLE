import streamlit as st
import os

from utils import get_last_project

project_path = get_last_project()

docs = [

    "executive_brief.docx",
    "copilot_report.pdf",
    "prefactibilidad.docx"

]

st.title("📁 Documentos")

for doc in docs:

    path = os.path.join(
        project_path,
        doc
    )

    if os.path.exists(path):

        with open(
            path,
            "rb"
        ) as f:

            st.download_button(
                label=f"Descargar {doc}",
                data=f,
                file_name=doc
            )