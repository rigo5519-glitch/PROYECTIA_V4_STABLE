from engines.tir_engine.tir_engine import (
    TIREngine
)

cash_flow = {

    "tabla_flujo": [

        {"Flujo": -297500},

        {"Flujo": 137034.47},

        {"Flujo": 156610.82},

        {"Flujo": 176187.17},

        {"Flujo": 185975.35},

        {"Flujo": 195763.53},

        {"Flujo": 195763.53},

        {"Flujo": 195763.53},

        {"Flujo": 195763.53},

        {"Flujo": 195763.53},

        {"Flujo": 195763.53}
    ]
}

engine = TIREngine()

resultado = engine.generate(
    cash_flow
)

print(resultado)