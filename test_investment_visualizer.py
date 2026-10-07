from engines.visualization_engine.investment_visualizer import (
    InvestmentVisualizer
)

investment = {

    "terreno": 30000,

    "infraestructura": 75000,

    "equipos": 150000,

    "vehiculo": 20000,

    "capital_trabajo": 22500
}

visualizer = (
    InvestmentVisualizer()
)

visualizer.generate(
    investment
)

print(
    "✅ inversion_inicial.png generado"
)