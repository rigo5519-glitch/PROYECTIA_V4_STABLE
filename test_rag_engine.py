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

project_master = (

    engine.retrieve_project_master(

        mejor["project_id"]
    )
)

print(

    project_master["investment"]
)

print(

    project_master["van"]
)