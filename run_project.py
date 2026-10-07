from project_generator import ProjectGenerator

generator = ProjectGenerator()

ideas = [

    "Quiero implementar una planta procesadora de lacteos",

    "Quiero crear una empresa de transporte pesado",

    "Quiero desarrollar un centro turistico comunitario",

    "Quiero instalar una planta de reciclaje de neumaticos"
]

for idea in ideas:

    resultado = generator.generate_project(idea)

    print("\n")
    print("=" * 70)
    print("IDEA:")
    print(idea)
    print("=" * 70)

    print("\nCLASIFICACION")
    print(resultado["idea"])

    print("\nDIAGNOSTICO")
    print(resultado["diagnostic"])

    print("\nARBOL DE PROBLEMAS")
    print(resultado["problem_tree"])

    print("\nARBOL DE OBJETIVOS")
    print(resultado["objective_tree"])

    print("\nMARCO LOGICO")
    print(resultado["logical_framework"])

    print("\nMERCADO")
    print(resultado["market"])

    print("\nTECNICO")
    print(resultado["technical"])

    print("\nLOCALIZACION")
    print(resultado["localization"])

    print("\nPROJECT MASTER")

    print(resultado["project_master"])

    print("\nTAMAÑO")
    print(resultado["size"])

    print("\nFLUJO DE CAJA")
    print(resultado["cash_flow"])

    print("\nINVERSION")
    print(resultado["investment"])

    print("\nCOSTOS")
    print(resultado["costs"])

    print("\nINGRESOS")
    print(resultado["revenue"])

    print("\nVAN")
    print(resultado["van"])

    print("\nTIR")
    print(resultado["tir"])

    print("\nPRI")
    print(resultado["pri"])

    print("\nB/C")
    print(resultado["bc"])

    print("\nSENSIBILIDAD")
    print(resultado["sensitivity"])

    print("\nMONTE CARLO")
    print(resultado["montecarlo"])

    print("\nTALENTO HUMANO")
    print(resultado["workforce"])

    print("\nPROCESOS")
    print(resultado["process"])

    print("\nMARKETING")
    print(resultado["marketing"])

    print("\nPCA")
    print(resultado["pca"])

    print("\nCLUSTERING")
    print(resultado["clustering"])


    print("\nDASHBOARD")
    print(resultado["dashboard"])

    print("\nORGANIZACION")
    print(resultado["organizational"])

    print("\nLAYOUT")
    print(resultado["layout"])

    print("\nKNOWLEDGE GRAPH")
    print(resultado["knowledge_graph"])