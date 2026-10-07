from engines.pri_engine.pri_engine import (
    PRIEngine
)

cash_flow = {

    "tabla_flujo": [

        {
            "Periodo": 0,
            "Flujo_Acumulado":
                -297500,
            "Flujo":
                -297500
        },

        {
            "Periodo": 1,
            "Flujo_Acumulado":
                -160465.53,
            "Flujo":
                137034.47
        },

        {
            "Periodo": 2,
            "Flujo_Acumulado":
                -3854.70,
            "Flujo":
                156610.82
        },

        {
            "Periodo": 3,
            "Flujo_Acumulado":
                172332.47,
            "Flujo":
                176187.17
        }
    ]
}

engine = PRIEngine()

resultado = engine.generate(
    cash_flow
)

print(resultado)