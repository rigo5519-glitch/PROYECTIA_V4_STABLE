import json

from engines.copilot_engine.prefeasibility_generator import (
    PrefeasibilityGenerator
)

with open(
    "projects/PROY_0105/project_master.json",
    encoding="utf-8"
) as f:

    project_master = json.load(f)

generator = (
    PrefeasibilityGenerator()
)

archivo = generator.generate(
    project_master
)

print(
    "PREFACTIBILIDAD:",
    archivo
)