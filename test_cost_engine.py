from engines.cost_engine.cost_engine import (
    CostEngine
)

size_data = {

    "categoria":
        "MEDIANO",

    "capacidad_instalada":
        14079
}

engine = CostEngine()

resultado = engine.generate(
    size_data
)

print(resultado)