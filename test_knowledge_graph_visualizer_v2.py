import json
import os

from engines.knowledge_graph_engine.knowledge_graph_engine_v3 import (
    KnowledgeGraphEngineV3
)

from engines.visualization_engine.knowledge_graph_visualizer import (
    KnowledgeGraphVisualizer
)

projects_dir = "projects"

proyectos = sorted(
    [
        p for p in os.listdir(projects_dir)
        if p.startswith("PROY_")
    ]
)

ultimo_proyecto = proyectos[-1]

ruta = os.path.join(
    projects_dir,
    ultimo_proyecto,
    "project_master.json"
)

with open(
    ruta,
    encoding="utf-8"
) as f:

    project_master = json.load(f)

graph_engine = KnowledgeGraphEngineV3()

graph = graph_engine.generate(
    project_master
)

visualizer = KnowledgeGraphVisualizer()

visualizer.generate(
    graph,
    output_file="outputs/knowledge_graph_v2.png"
)

print(
    f"✅ knowledge_graph_v2.png generado usando {ultimo_proyecto}"
)