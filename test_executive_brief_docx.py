from engines.copilot_engine.executive_brief_docx import (
    ExecutiveBriefDOCX
)

print("INICIO TEST")

generator = ExecutiveBriefDOCX()

archivo = generator.generate(
    "Quiero instalar una planta de reciclaje de neumaticos"
)

print(
    "EXECUTIVE BRIEF GENERADO:",
    archivo
)