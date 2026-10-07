from engines.rag_engine.rag_knowledge_engine import (
    RAGKnowledgeEngine
)


class LLMOrchestrator:

    def analyze(
        self,
        idea
    ):

        rag = RAGKnowledgeEngine()

        contexto = rag.retrieve_context(
            idea
        )

        if not contexto:

            return {
                "idea": idea,
                "recomendacion":
                "No existe experiencia previa."
            }

        return contexto