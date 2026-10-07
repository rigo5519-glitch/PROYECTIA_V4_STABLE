from engines.llm_orchestrator.llm_orchestrator_v2 import (
    LLMOrchestratorV2
)

engine = (
    LLMOrchestratorV2()
)

resultado = engine.analyze(
    "Quiero instalar una planta de reciclaje de neumaticos"
)

print("\nRESULTADO\n")

for k, v in resultado.items():

    print(k, ":", v)