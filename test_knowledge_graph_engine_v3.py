import json
import os

from engines.knowledge_graph_engine.knowledge_graph_engine_v3 import (
    KnowledgeGraphEngineV3
)

projects_dir = "projects"

ultimos = sorted(
    [
        p for p in os.listdir(projects_dir)
        if p.startswith("PROY_")
    ]
)

ultimo = ultimos[-1]

ruta = os.path.join(
    projects_dir,
    ultimo,
    "project_master.json"
)

with open(
    ruta,
    encoding="utf-8"
) as f:

    project_master = json.load(f)

engine = KnowledgeGraphEngineV3()

resultado = engine.generate(
    project_master
)

print(resultado)