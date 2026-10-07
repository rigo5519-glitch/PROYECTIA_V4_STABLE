from engines.visualization_engine.cashflow_visualizer import (
    CashFlowVisualizer
)

cash_flow = {

    "tabla_flujo": [

        {
            "Periodo": 0,
            "Flujo_Acumulado": -297500
        },

        {
            "Periodo": 1,
            "Flujo_Acumulado": -160465.53
        },

        {
            "Periodo": 2,
            "Flujo_Acumulado": -3854.70
        },

        {
            "Periodo": 3,
            "Flujo_Acumulado": 172332.47
        },

        {
            "Periodo": 4,
            "Flujo_Acumulado": 358307.82
        },

        {
            "Periodo": 5,
            "Flujo_Acumulado": 554071.35
        }
    ]
}

visualizer = CashFlowVisualizer()

visualizer.generate(
    cash_flow
)

print(
    "✅ flujo_caja.png generado"
)