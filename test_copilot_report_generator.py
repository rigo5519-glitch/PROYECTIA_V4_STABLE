from engines.copilot_engine.copilot_report_generator import (
    CopilotReportGenerator
)

generator = CopilotReportGenerator()

reporte = generator.generate(
    "Quiero instalar una planta de reciclaje de neumaticos"
)

print(reporte)