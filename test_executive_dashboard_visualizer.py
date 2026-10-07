from engines.visualization_engine.executive_dashboard_visualizer import (
    ExecutiveDashboardVisualizer
)

dashboard = {

    "VAN": 704804.01,

    "TIR": 53.73,

    "PRI": 2.02,

    "BC": 3.37,

    "Probabilidad_Exito": 100.0,

    "Nivel_Riesgo": "BAJO",

    "Score": 100,

    "Clasificacion": "EXCELENTE"
}

visualizer = (
    ExecutiveDashboardVisualizer()
)

visualizer.generate(
    dashboard
)

print(
    "✅ dashboard_ejecutivo.png generado"
)