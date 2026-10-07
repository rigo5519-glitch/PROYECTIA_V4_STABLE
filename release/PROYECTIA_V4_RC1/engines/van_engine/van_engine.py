class VANEngine:

    def generate(
        self,
        cash_flow_data
    ):

        TMAR = 0.12

        flujos = []

        for fila in cash_flow_data[
            "tabla_flujo"
        ]:

            flujos.append(
                fila["Flujo"]
            )

        van = 0

        for periodo, flujo in enumerate(
            flujos
        ):

            van += (

                flujo /

                ((1 + TMAR) ** periodo)
            )

        if van > 0:

            evaluacion = "FACTIBLE"

        elif van == 0:

            evaluacion = "INDIFERENTE"

        else:

            evaluacion = "NO FACTIBLE"

        return {

            "TMAR":
                TMAR,

            "VAN":
                round(
                    van,
                    2
                ),

            "evaluacion":
                evaluacion
        }