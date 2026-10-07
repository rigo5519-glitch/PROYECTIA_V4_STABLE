from engines.knowledge_engine.knowledge_engine import KnowledgeEngine


engine = KnowledgeEngine()

knowledge = engine.get_all_knowledge()

for sector in knowledge:

    print("\n====================")
    print(sector["sector"])
    print("====================")

    print(sector)