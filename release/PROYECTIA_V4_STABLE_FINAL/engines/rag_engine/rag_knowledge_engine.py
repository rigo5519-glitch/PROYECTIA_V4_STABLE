from engines.rag_engine.rag_engine import (
    RAGEngine
)


class RAGKnowledgeEngine:

    def retrieve_context(
        self,
        idea
    ):

        rag = RAGEngine()

        proyectos = rag.retrieve(
            idea
        )

        if not proyectos:
            return []

        mejor = proyectos[0]

        project_master = (
            rag.retrieve_project_master(
                mejor["project_id"]
            )
        )

        return {
            "proyecto": mejor,
            "project_master": project_master
        }