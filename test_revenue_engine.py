from engines.revenue_engine.revenue_engine import (
    RevenueEngine
)

market = {

    "demanda_potencial":
        12799
}

size = {

    "capacidad_instalada":
        14079
}

engine = RevenueEngine()

resultado = engine.generate(

    market,

    size
)

print(resultado)