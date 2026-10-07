from engines.idea_engine.idea_engine import IdeaEngine
from engines.market_engine.market_engine import MarketEngine

idea_engine = IdeaEngine()

project = idea_engine.analyze(
    "Quiero implementar una planta procesadora de lacteos"
)

market_engine = MarketEngine()

resultado = market_engine.generate(
    project
)

print(resultado)