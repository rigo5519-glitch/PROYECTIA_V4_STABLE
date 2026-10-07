from engines.llm_orchestrator.llm_orchestrator import (
    LLMOrchestrator
)

orchestrator = (
    LLMOrchestrator()
)

resultado = orchestrator.analyze(
    "Quiero instalar una planta de reciclaje de neumaticos"
)

print(resultado)
