from engines.knowledge_graph_engine.knowledge_graph_engine import (
    KnowledgeGraphEngine
)

project_master = {

    "problem_tree": {

        "problema_central":
            "Bajo aprovechamiento de residuos"
    },

    "objective_tree": {

        "objetivo_general":
            "Incrementar aprovechamiento de residuos"
    }
}

engine = (
    KnowledgeGraphEngine()
)

resultado = engine.generate(
    project_master
)

print(resultado)