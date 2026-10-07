from engines.rag_engine.rag_engine import (
    RAGEngine
)

engine = RAGEngine()

resultados = engine.retrieve(
    "Quiero instalar una planta de reciclaje de neumaticos"
)

print("\nPROYECTOS ENCONTRADOS\n")

for r in resultados:

    print(r)

    print("\nCARGANDO EL MEJOR PROYECTO\n")

    mejor = resultados[0]

    print("PROJECT ID:")

    print(mejor["project_id"])

    project_master = engine.retrieve_project_master(
    mejor["project_id"]
)

    print("\nCLAVES DISPONIBLES\n")

    print(project_master.keys())