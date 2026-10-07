from engines.workforce_engine.workforce_engine import (
    WorkforceEngine
)

size_data = {

    "categoria":
        "MEDIANO"
}

engine = (
    WorkforceEngine()
)

resultado = engine.generate(
    size_data
)

print(resultado)