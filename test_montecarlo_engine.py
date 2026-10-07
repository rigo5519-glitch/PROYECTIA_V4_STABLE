from engines.montecarlo_engine.montecarlo_engine import (
    MonteCarloEngine
)

investment = {

    "inversion_total":
        297500
}

revenue = {

    "capacidad_instalada":
        14091,

    "precio_unitario":
        25
}

costs = {

    "costos_operativos":
        93981.96
}

engine = MonteCarloEngine()

resultado = engine.generate(

    investment,

    revenue,

    costs
)

print(resultado)