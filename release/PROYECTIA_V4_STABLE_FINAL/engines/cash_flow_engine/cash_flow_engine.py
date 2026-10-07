import pandas as pd


class CashFlowEngine:

    def generate(
        self,
        investment_data,
        cost_data,
        revenue_data
    ):

        inversion_inicial = (
            investment_data["inversion_total"]
        )

        ventas = (
            revenue_data["ventas"]
        )

        costos_operativos = (
            cost_data["costos_operativos"]
        )

        depreciacion = (
            investment_data["equipos"] * 0.10
        )

        impuesto_renta = 0.25

        utilidad_operativa = (
            ventas
            - costos_operativos
            - depreciacion
        )

        impuesto = (
            utilidad_operativa
            * impuesto_renta
        )

        utilidad_neta = (
            utilidad_operativa
            - impuesto
        )

        flujo_operativo = (
            utilidad_neta
            + depreciacion
        )

        horizonte = 10

        utilizacion = {}

        for anio in range(
            1,
            horizonte + 1
        ):

            if anio == 1:

                utilizacion[anio] = 0.70

            elif anio == 2:

                utilizacion[anio] = 0.80

            elif anio == 3:

                utilizacion[anio] = 0.90

            elif anio == 4:

                utilizacion[anio] = 0.95

            else:

                utilizacion[anio] = 1.00

        flujos = []

        for anio, factor in utilizacion.items():

            flujos.append(
                flujo_operativo * factor
            )

        flujo_proyecto = [
            -inversion_inicial,
            *flujos
        ]

        df_flujo = pd.DataFrame({

            "Periodo":
                range(
                    len(flujo_proyecto)
                ),

            "Flujo":
                flujo_proyecto
        })

        df_flujo[
            "Flujo_Acumulado"
        ] = (

            df_flujo["Flujo"]
            .cumsum()
        )

        return {

            "inversion_inicial":
                round(
                    inversion_inicial,
                    2
                ),

            "flujo_operativo":
                round(
                    flujo_operativo,
                    2
                ),

            "horizonte":
                horizonte,

            "flujos":
                flujos,

            "tabla_flujo":
                df_flujo.to_dict(
                    orient="records"
                )
        }