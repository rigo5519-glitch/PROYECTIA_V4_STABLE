from engines.visualization_engine.cost_visualizer import (
    CostVisualizer
)

cost_data = {

    "personal": 60000,

    "energia": 16909.2,

    "mantenimiento": 5072.76,

    "administracion": 12000
}

visualizer = CostVisualizer()

visualizer.generate(
    cost_data
)

print(
    "✅ costos_operativos.png generado"
)