from engines.llm_orchestrator.llm_orchestrator_v2 import (
    LLMOrchestratorV2
)


class CopilotEngine:

    def generate_report(
        self,
        idea
    ):

        orchestrator = (
            LLMOrchestratorV2()
        )

        analisis = (
            orchestrator.analyze(
                idea
            )
        )

        return analisis