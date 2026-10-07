from engines.copilot_engine.copilot_report_generator_v2 import (
    CopilotReportGeneratorV2
)

generator = CopilotReportGeneratorV2()

archivo = generator.generate(
    "Quiero instalar una planta de reciclaje de neumaticos"
)

print(
    "REPORTE GENERADO:",
    archivo
)