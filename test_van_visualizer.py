from engines.visualization_engine.van_visualizer import (
    VANVisualizer
)

cash_flow = {

    "tabla_flujo": [

        {"Periodo": 0, "Flujo": -297500},

        {"Periodo": 1, "Flujo": 137034.47},

        {"Periodo": 2, "Flujo": 156610.82},

        {"Periodo": 3, "Flujo": 176187.17},

        {"Periodo": 4, "Flujo": 185975.35},

        {"Periodo": 5, "Flujo": 195763.53},

        {"Periodo": 6, "Flujo": 195763.53},

        {"Periodo": 7, "Flujo": 195763.53},

        {"Periodo": 8, "Flujo": 195763.53},

        {"Periodo": 9, "Flujo": 195763.53},

        {"Periodo": 10, "Flujo": 195763.53}
    ]
}

visualizer = VANVisualizer()

visualizer.generate(
    cash_flow
)

print(
    "✅ van_acumulado.png generado"
)