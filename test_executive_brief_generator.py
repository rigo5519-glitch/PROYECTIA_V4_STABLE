from engines.copilot_engine.executive_brief_generator import (
    ExecutiveBriefGenerator
)

generator = ExecutiveBriefGenerator()

brief = generator.generate(
    "Quiero instalar una planta de reciclaje de neumaticos"
)

print(brief)