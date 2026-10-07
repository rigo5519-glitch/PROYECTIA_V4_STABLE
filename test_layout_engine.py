from engines.layout_engine.layout_engine import (
    LayoutEngine
)

size = {

    "categoria":
        "MEDIANO"
}

process = {

    "procesos": [

        "Recepcion",

        "Clasificacion",

        "Procesamiento",

        "Control Calidad",

        "Almacenamiento"
    ]
}

engine = LayoutEngine()

resultado = engine.generate(

    size,

    process
)

print(resultado)