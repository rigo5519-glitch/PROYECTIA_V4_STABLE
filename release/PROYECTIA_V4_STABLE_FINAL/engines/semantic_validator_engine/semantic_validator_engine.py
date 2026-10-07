class SemanticValidatorEngine:

    def compare_texts(
        self,
        text1,
        text2
    ):

        words1 = set(
            str(text1).lower().split()
        )

        words2 = set(
            str(text2).lower().split()
        )

        common = words1.intersection(
            words2
        )

        total = max(
            len(words1),
            len(words2),
            1
        )

        score = (
            len(common) / total
        ) * 100

        return round(score, 2)

    def traffic_light(
        self,
        score
    ):

        if score >= 80:

            return "🟢 EXCELENTE"

        elif score >= 65:

            return "🟡 ACEPTABLE"

        elif score >= 50:

            return "🟠 REVISAR"

        else:

            return "🔴 CRITICO"

    def validate(
        self,
        problem_tree,
        objective_tree,
        logical_framework
    ):

        problema = (
            problem_tree["problema_central"]
        )

        objetivo = (
            objective_tree["objetivo_general"]
        )

        score_po = self.compare_texts(
            problema,
            objetivo
        )

        indicador = (
            logical_framework[
                "indicadores"
            ][0]
        )

        score_oi = self.compare_texts(
            objetivo,
            indicador
        )

        indice_global = round(
            (
                score_po +
                score_oi
            ) / 2,
            2
        )

        return {

            "problema_objetivo":
                score_po,

            "objetivo_indicador":
                score_oi,

            "indice_global":
                indice_global,

            "estado":
                self.traffic_light(
                    indice_global
                )
        }