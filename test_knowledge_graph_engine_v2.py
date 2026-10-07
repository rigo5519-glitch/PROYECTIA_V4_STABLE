from engines.knowledge_graph_engine.knowledge_graph_engine_v2 import (
    KnowledgeGraphEngineV2
)

project_master = {

    "problem_tree": {
        "problema_central":
            "Bajo aprovechamiento de residuos"
    },

    "objective_tree": {
        "objetivo_general":
            "Incrementar aprovechamiento de residuos"
    },

    "localization": {
        "ubicacion_optima":
            "Riobamba"
    },

    "size": {
        "capacidad_instalada":
            14091
    },

    "investment": {
        "inversion_total":
            297500
    },

    "van": {
        "VAN":
            704804
    }
}

engine = KnowledgeGraphEngineV2()

resultado = engine.generate(
    project_master
)

print(resultado)