from engines.idea_engine.idea_engine import (
    IdeaEngine
)

engine = IdeaEngine()

resultado = engine.analyze(
    "Centro ecoturístico comunitario en Alausí para turismo de naturaleza y aventura"
)

print(resultado)