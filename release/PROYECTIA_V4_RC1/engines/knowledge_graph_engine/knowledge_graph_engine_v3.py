class KnowledgeGraphEngineV3:

    def generate(
        self,
        project_master
    ):

        nodos = []

        relaciones = []

        # NODOS

        nodos.append({
            "id": "problema",
            "label":
                project_master[
                    "problem_tree"
                ]["problema_central"],
            "tipo": "Problema"
        })

        nodos.append({
            "id": "objetivo",
            "label":
                project_master[
                    "objective_tree"
                ]["objetivo_general"],
            "tipo": "Objetivo"
        })

        nodos.append({
            "id": "mercado",
            "label":
                "Mercado Objetivo",
            "tipo": "Mercado"
        })

        nodos.append({
            "id": "marketing",
            "label":
                project_master[
                    "marketing"
                ]["producto"],
            "tipo": "Marketing"
        })

        nodos.append({
            "id": "localizacion",
            "label":
                project_master[
                    "localization"
                ]["ubicacion_optima"],
            "tipo": "Localizacion"
        })

        nodos.append({
            "id": "tamano",
            "label":
                str(
                    project_master[
                        "size"
                    ][
                        "capacidad_instalada"
                    ]
                ),
            "tipo": "Capacidad"
        })

        nodos.append({
            "id": "workforce",
            "label":
                "Talento Humano",
            "tipo": "Workforce"
        })

        nodos.append({
            "id": "process",
            "label":
                "Procesos",
            "tipo": "Proceso"
        })

        nodos.append({
            "id": "investment",
            "label":
                str(
                    project_master[
                        "investment"
                    ][
                        "inversion_total"
                    ]
                ),
            "tipo": "Inversion"
        })

        nodos.append({
            "id": "costs",
            "label":
                str(
                    project_master[
                        "costs"
                    ][
                        "costos_operativos"
                    ]
                ),
            "tipo": "Costos"
        })

        nodos.append({
            "id": "revenue",
            "label":
                str(
                    project_master[
                        "revenue"
                    ]["ventas"]
                ),
            "tipo": "Ingresos"
        })

        nodos.append({
            "id": "van",
            "label":
                str(
                    project_master[
                        "van"
                    ]["VAN"]
                ),
            "tipo": "VAN"
        })

        # RELACIONES

        relaciones.extend([

            {
                "source": "problema",
                "target": "objetivo",
                "tipo": "resuelve"
            },

            {
                "source": "objetivo",
                "target": "mercado",
                "tipo": "atiende"
            },

            {
                "source": "mercado",
                "target": "marketing",
                "tipo": "comercializa"
            },

            {
                "source": "marketing",
                "target": "localizacion",
                "tipo": "opera_en"
            },

            {
                "source": "localizacion",
                "target": "tamano",
                "tipo": "permite"
            },

            {
                "source": "tamano",
                "target": "workforce",
                "tipo": "requiere"
            },

            {
                "source": "workforce",
                "target": "process",
                "tipo": "ejecuta"
            },

            {
                "source": "process",
                "target": "investment",
                "tipo": "requiere"
            },

            {
                "source": "investment",
                "target": "costs",
                "tipo": "genera"
            },

            {
                "source": "costs",
                "target": "revenue",
                "tipo": "condiciona"
            },

            {
                "source": "revenue",
                "target": "van",
                "tipo": "impacta"
            }
        ])

        return {

            "nodos": nodos,

            "relaciones": relaciones
        }