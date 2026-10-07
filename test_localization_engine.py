from engines.localization_engine.localization_engine import (
    LocalizationEngine
)

engine = LocalizationEngine()

resultado = engine.generate()

print(resultado)