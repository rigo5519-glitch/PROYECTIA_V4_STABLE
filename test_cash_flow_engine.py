from engines.cash_flow_engine.cash_flow_engine import (
    CashFlowEngine
)

investment = {

    "inversion_total": 297500,

    "equipos": 150000
}

costs = {

    "costos_operativos": 93963.24
}

revenue = {

    "ventas": 319975
}

engine = CashFlowEngine()

resultado = engine.generate(

    investment,

    costs,

    revenue
)

print(resultado)