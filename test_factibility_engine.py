import sys
import os
import json

sys.path.append(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

from release.PROYECTIA_V4_STABLE.engines.factibility_engine.factibility_engine import (
    FactibilityEngine
)


with open(
    "projects/PROY_0122/project_master.json",
    encoding="utf-8"
) as f:

    pm = json.load(f)

engine = FactibilityEngine()

resultado = engine.generate(pm)

print(resultado)