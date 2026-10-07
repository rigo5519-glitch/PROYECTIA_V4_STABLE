from engines.visualization_engine.knowledge_graph_visualizer import (
    KnowledgeGraphVisualizer
)

graph = {

    "nodos": [

        {
            "id": "problema",
            "label": "Bajo aprovechamiento de residuos"
        },

        {
            "id": "objetivo",
            "label": "Incrementar aprovechamiento"
        },

        {
            "id": "ubicacion",
            "label": "Riobamba"
        },

        {
            "id": "capacidad",
            "label": "14091"
        },

        {
            "id": "inversion",
            "label": "297500"
        },

        {
            "id": "van",
            "label": "704804"
        }
    ],

    "relaciones": [

        {
            "source": "problema",
            "target": "objetivo"
        },

        {
            "source": "objetivo",
            "target": "ubicacion"
        },

        {
            "source": "ubicacion",
            "target": "capacidad"
        },

        {
            "source": "capacidad",
            "target": "inversion"
        },

        {
            "source": "inversion",
            "target": "van"
        }
    ]
}

visualizer = (
    KnowledgeGraphVisualizer()
)

visualizer.generate(
    graph
)

print(
    "✅ knowledge_graph.png generado"
)