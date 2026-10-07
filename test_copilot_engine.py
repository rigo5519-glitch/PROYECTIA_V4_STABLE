from engines.copilot_engine.copilot_engine import (
    CopilotEngine
)

copilot = CopilotEngine()

resultado = copilot.generate_report(
    "Quiero instalar una planta de reciclaje de neumaticos"
)

print(resultado)