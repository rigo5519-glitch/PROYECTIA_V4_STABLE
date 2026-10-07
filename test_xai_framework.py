from engines.xai_framework_engine.xai_framework_engine import (
    XAIFrameworkEngine
)

engine = XAIFrameworkEngine()

resultado = engine.interpret_score(
    58.91
)

print(resultado)