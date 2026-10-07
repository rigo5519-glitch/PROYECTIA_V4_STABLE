class BCEngine:

    def generate(
        self,
        van_data,
        investment_data
    ):

        van = van_data["VAN"]

        inversion = (
            investment_data[
                "inversion_total"
            ]
        )

        beneficios_actualizados = (
            van +
            inversion
        )

        bc = (
            beneficios_actualizados /
            inversion
        )

        if bc > 1:

            evaluacion = (
                "FACTIBLE"
            )

        else:

            evaluacion = (
                "NO FACTIBLE"
            )

        return {

            "beneficios_actualizados":
                round(
                    beneficios_actualizados,
                    2
                ),

            "inversion_inicial":
                round(
                    inversion,
                    2
                ),

            "BC":
                round(
                    bc,
                    2
                ),

            "evaluacion":
                evaluacion
        }