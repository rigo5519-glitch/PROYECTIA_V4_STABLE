import numpy_financial as npf


class TIREngine:

    def generate(
        self,
        cash_flow_data
    ):

        flujos = []

        for fila in cash_flow_data[
            "tabla_flujo"
        ]:

            flujos.append(
                fila["Flujo"]
            )

        tir = npf.irr(
            flujos
        )

        TMAR = 0.12

        if tir > TMAR:

            evaluacion = (
                "FACTIBLE"
            )

        else:

            evaluacion = (
                "NO FACTIBLE"
            )

        return {

            "TMAR":
                TMAR,

            "TIR":
                round(
                    tir * 100,
                    2
                ),

            "evaluacion":
                evaluacion
        }