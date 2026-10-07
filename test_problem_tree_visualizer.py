from engines.visualization_engine.problem_tree_visualizer import (
    ProblemTreeVisualizer
)

problem_tree = {

    "problema_central":
        "Bajo aprovechamiento industrial de la produccion",

    "causas": [

        {
            "causa":
                "Limitada capacidad de procesamiento"
        },

        {
            "causa":
                "Escasa tecnologia industrial"
        },

        {
            "causa":
                "Bajo valor agregado"
        }
    ],

    "efectos": [

        {
            "efecto":
                "Menores ingresos de productores"
        },

        {
            "efecto":
                "Perdida de competitividad"
        },

        {
            "efecto":
                "Desaprovechamiento productivo"
        }
    ]
}

visualizer = (
    ProblemTreeVisualizer()
)

visualizer.generate(
    problem_tree
)

print(
    "✅ arbol_problemas.png generado"
)