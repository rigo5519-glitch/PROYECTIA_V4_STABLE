class MethodologicalReviewEngine:

    def evaluate(
        self,
        logical_framework
    ):

        score = 100

        observaciones = []

        indicadores = (
            logical_framework[
                "indicadores"
            ]
        )

        for indicador in indicadores:

            palabras = len(
                indicador.split()
            )

            if palabras < 3:

                score -= 10

                observaciones.append(
                    f"Indicador débil: {indicador}"
                )

        for supuesto in logical_framework[
            "supuestos"
        ]:

            if len(
                supuesto
            ) < 10:

                score -= 10

                observaciones.append(
                    f"Supuesto insuficiente: {supuesto}"
                )

        if score >= 90:

            estado = "🟢 Excelente"

        elif score >= 75:

            estado = "🟡 Aceptable"

        elif score >= 60:

            estado = "🟠 Revisar"

        else:

            estado = "🔴 Crítico"

        return {

            "score":
                score,

            "estado":
                estado,

            "observaciones":
                observaciones
        }
