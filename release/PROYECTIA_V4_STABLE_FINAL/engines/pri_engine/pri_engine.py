class PRIEngine:

    def generate(
        self,
        cash_flow_data
    ):

        tabla = cash_flow_data[
            "tabla_flujo"
        ]

        pri = None

        for fila in tabla:

            if (
                fila[
                    "Flujo_Acumulado"
                ] >= 0
            ):

                pri = fila[
                    "Periodo"
                ]

                break

        pri_exacto = None

        for i in range(
            1,
            len(tabla)
        ):

            if (
                tabla[i][
                    "Flujo_Acumulado"
                ] >= 0
            ):

                acumulado_anterior = (
                    tabla[i - 1][
                        "Flujo_Acumulado"
                    ]
                )

                flujo_actual = (
                    tabla[i][
                        "Flujo"
                    ]
                )

                fraccion = (

                    abs(
                        acumulado_anterior
                    )

                    /

                    flujo_actual
                )

                pri_exacto = (

                    (i - 1)

                    +

                    fraccion
                )

                break

        if pri_exacto < 5:

            clasificacion = (
                "Recuperación Rápida"
            )

        elif pri_exacto < 10:

            clasificacion = (
                "Recuperación Moderada"
            )

        else:

            clasificacion = (
                "Recuperación Lenta"
            )

        return {

            "PRI":
                pri,

            "PRI_Exacto":
                round(
                    pri_exacto,
                    2
                ),

            "clasificacion":
                clasificacion
        }