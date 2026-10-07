from engines.rag_engine.rag_knowledge_engine import (
    RAGKnowledgeEngine
)

engine = RAGKnowledgeEngine()

resultado = engine.retrieve_context(
    "Quiero instalar una planta de reciclaje de neumaticos"
)

print(resultado)
