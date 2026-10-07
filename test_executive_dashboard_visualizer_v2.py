from engines.visualization_engine.executive_dashboard_visualizer_v2 import (
    ExecutiveDashboardVisualizerV2
)

dashboard = {

    "VAN": 704804.01,

    "TIR": 53.73,

    "PRI": 2.02,

    "BC": 3.37,

    "Probabilidad_Exito": 100,

    "Nivel_Riesgo": "BAJO",

    "Score": 100,

    "Clasificacion": "EXCELENTE"
}

engine = (
    ExecutiveDashboardVisualizerV2()
)

engine.generate(
    dashboard
)

print(
    "✅ dashboard_ejecutivo_v2.png generado"
)