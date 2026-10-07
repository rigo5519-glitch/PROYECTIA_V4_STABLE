class KnowledgeGraphEngine:

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

        nodos.append({

            "id": "problema",

            "label": problema,

            "tipo": "Problema"
        })

        nodos.append({

            "id": "objetivo",

            "label": objetivo,

            "tipo": "Objetivo"
        })

        relaciones.append({

            "source":
                "problema",

            "target":
                "objetivo",

            "tipo":
                "resuelve"
        })

        return {

            "nodos":
                nodos,

            "relaciones":
                relaciones
        }