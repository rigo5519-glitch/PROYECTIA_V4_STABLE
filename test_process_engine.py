from engines.process_engine.process_engine import (
    ProcessEngine
)

project = {

    "sector":
        "Industria"
}

engine = ProcessEngine()

resultado = engine.generate(
    project
)

print(resultado)