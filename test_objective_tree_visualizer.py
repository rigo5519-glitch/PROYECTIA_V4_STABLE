from engines.visualization_engine.objective_tree_visualizer import (
    ObjectiveTreeVisualizer
)

objective_tree = {

    "objetivo_general":
        "Incrementar aprovechamiento industrial de la produccion",

    "medios": [

        "Fortalecer capacidad de procesamiento",

        "Fortalecer tecnologia industrial",

        "Fortalecer valor agregado"
    ],

    "fines": [

        "Reducir perdida de competitividad",

        "Reducir desaprovechamiento productivo",

        "Reducir menores ingresos"
    ]
}

visualizer = (
    ObjectiveTreeVisualizer()
)

visualizer.generate(
    objective_tree
)

print(
    "✅ arbol_objetivos.png generado"
)