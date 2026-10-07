from engines.copilot_engine.copilot_pdf_generator import (
    CopilotPDFGenerator
)

generator = CopilotPDFGenerator()

archivo = generator.generate(
    "Quiero instalar una planta de reciclaje de neumaticos"
)

print(
    "PDF GENERADO:",
    archivo
)