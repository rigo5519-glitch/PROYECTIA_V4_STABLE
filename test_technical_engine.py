from engines.idea_engine.idea_engine import IdeaEngine
from engines.technical_engine.technical_engine import TechnicalEngine


idea_engine = IdeaEngine()

project = idea_engine.analyze(
    "Quiero implementar una planta procesadora de lacteos"
)

technical_engine = TechnicalEngine()

technical = technical_engine.generate(
    project
)

print(technical)