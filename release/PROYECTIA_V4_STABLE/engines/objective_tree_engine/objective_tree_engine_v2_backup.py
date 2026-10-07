class ObjectiveTreeEngine:

    def generate(self, problem_tree):

        problema = problem_tree["problema_central"]

        if "Bajo" in problema:

            objetivo_general = problema.replace(
                "Bajo",
                "Incrementar"
            )

        elif "Baja" in problema:

            objetivo_general = problema.replace(
                "Baja",
                "Incrementar"
            )

        elif "Deficiente" in problema:

            objetivo_general = problema.replace(
                "Deficiente",
                "Mejorar"
            )

        else:

            objetivo_general = (
                "Mejorar " +
                problema.lower()
            )

        return {

            "objetivo_general":
                objetivo_general,

            "objetivos_especificos": [

                "Fortalecer la gestion del proyecto",

                "Incrementar capacidades operativas",

                "Mejorar el desempeño sectorial"
            ]
        }