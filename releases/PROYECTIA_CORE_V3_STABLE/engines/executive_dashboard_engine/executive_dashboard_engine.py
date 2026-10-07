class ExecutiveDashboardEngine:

    def generate(
        self,
        van_data,
        tir_data,
        pri_data,
        bc_data,
        montecarlo_data
    ):

        van = van_data["VAN"]

        tir = tir_data["TIR"]

        pri = pri_data["PRI_Exacto"]

        bc = bc_data["BC"]

        probabilidad = (
            montecarlo_data[
                "probabilidad_exito"
            ]
        )

        riesgo = (
            montecarlo_data[
                "nivel_riesgo"
            ]
        )

        dashboard = {

            "VAN":
                round(van, 2),

            "TIR":
                round(tir, 2),

            "PRI":
                round(pri, 2),

            "BC":
                round(bc, 2),

            "Probabilidad_Exito":
                round(probabilidad, 2),

            "Nivel_Riesgo":
                riesgo
        }

        score = 0

        if van > 0:
            score += 20

        if tir > 12:
            score += 20

        if pri < 5:
            score += 20

        if bc > 1:
            score += 20

        if probabilidad >= 80:
            score += 20

        if score >= 90:

            clasificacion = "EXCELENTE"

        elif score >= 70:

            clasificacion = "BUENO"

        elif score >= 50:

            clasificacion = "ACEPTABLE"

        else:

            clasificacion = "NO RECOMENDABLE"

        dashboard["Score"] = score

        dashboard["Clasificacion"] = clasificacion

        return dashboard