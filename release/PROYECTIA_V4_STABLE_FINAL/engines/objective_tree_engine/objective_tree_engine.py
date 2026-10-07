class ObjectiveTreeEngine:

    def convert_cause_to_mean(
        self,
        causa
    ):

        return f"Fortalecer {causa.lower()}"

    def convert_effect_to_end(
        self,
        efecto
    ):

        return f"Reducir {efecto.lower()}"

    def generate(
        self,
        problem_tree
    ):

        problema = (
            problem_tree["problema_central"]
        )

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
                "Mejorar "
                + problema.lower()
            )

        medios = []

        for causa in problem_tree["causas"]:

            medio = self.convert_cause_to_mean(
                causa["causa"]
            )

            medios.append(medio)

        fines = []

        for efecto in problem_tree["efectos"]:

            fin = self.convert_effect_to_end(
                efecto["efecto"]
            )

            fines.append(fin)

        return {

            "objetivo_general":
                objetivo_general,

            "medios":
                medios,

            "fines":
                fines
        }