class KnowledgeGraphEngineV2:

    def generate(
        self,
        project_master
    ):

        nodos = []

        relaciones = []

        problema = (
            project_master[
                "problem_tree"
            ][
                "problema_central"
            ]
        )

        objetivo = (
            project_master[
                "objective_tree"
            ][
                "objetivo_general"
            ]
        )

        ubicacion = (
            project_master[
                "localization"
            ][
                "ubicacion_optima"
            ]
        )

        capacidad = (
            project_master[
                "size"
            ][
                "capacidad_instalada"
            ]
        )

        inversion = (
            project_master[
                "investment"
            ][
                "inversion_total"
            ]
        )

        van = (
            project_master[
                "van"
            ][
                "VAN"
            ]
        )

        nodos.extend([

            {
                "id": "problema",
                "label": problema,
                "tipo": "Problema"
            },

            {
                "id": "objetivo",
                "label": objetivo,
                "tipo": "Objetivo"
            },

            {
                "id": "ubicacion",
                "label": ubicacion,
                "tipo": "Localizacion"
            },

            {
                "id": "capacidad",
                "label": str(capacidad),
                "tipo": "Capacidad"
            },

            {
                "id": "inversion",
                "label": str(inversion),
                "tipo": "Inversion"
            },

            {
                "id": "van",
                "label": str(van),
                "tipo": "VAN"
            }
        ])

        relaciones.extend([

            {
                "source": "problema",
                "target": "objetivo",
                "tipo": "resuelve"
            },

            {
                "source": "objetivo",
                "target": "ubicacion",
                "tipo": "se_desarrolla_en"
            },

            {
                "source": "ubicacion",
                "target": "capacidad",
                "tipo": "permite"
            },

            {
                "source": "capacidad",
                "target": "inversion",
                "tipo": "requiere"
            },

            {
                "source": "inversion",
                "target": "van",
                "tipo": "genera"
            }
        ])

        return {

            "nodos": nodos,

            "relaciones": relaciones
        }