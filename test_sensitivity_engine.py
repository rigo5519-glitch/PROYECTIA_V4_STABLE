from engines.sensitivity_engine.sensitivity_engine import (
    SensitivityEngine
)

investment = {

    "inversion_total":
        297500
}

revenue = {

    "ventas":
        350000
}

costs = {

    "costos_operativos":
        93981.96
}

engine = SensitivityEngine()

resultado = engine.generate(

    investment,

    revenue,

    costs
)

print(resultado)