class XAIFrameworkEngine:

    def interpret_score(
        self,
        score
    ):

        if score >= 85:

            return {

                "nivel":
                    "Excelente",

                "explicacion":
                    "Existe una relación semántica fuerte.",

                "riesgo":
                    "Muy Bajo",

                "accion":
                    "No requiere ajustes."
            }

        elif score >= 70:

            return {

                "nivel":
                    "Aceptable",

                "explicacion":
                    "La relación es adecuada pero puede fortalecerse.",

                "riesgo":
                    "Bajo",

                "accion":
                    "Revisar redacción."
            }

        elif score >= 50:

            return {

                "nivel":
                    "Revisar",

                "explicacion":
                    "La coherencia es insuficiente.",

                "riesgo":
                    "Medio",

                "accion":
                    "Reformular conceptos."
            }

        else:

            return {

                "nivel":
                    "Crítico",

                "explicacion":
                    "No existe evidencia de relación conceptual.",

                "riesgo":
                    "Alto",

                "accion":
                    "Reconstruir el elemento."
            }