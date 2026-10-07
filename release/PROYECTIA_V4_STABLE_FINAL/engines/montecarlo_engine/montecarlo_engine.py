import numpy as np
import pandas as pd


class MonteCarloEngine:

    def calcular_van(
        self,
        inversion,
        flujos,
        tasa
    ):

        van = -inversion

        for periodo, flujo in enumerate(
            flujos,
            start=1
        ):

            van += (

                flujo /

                ((1 + tasa) ** periodo)
            )

        return van

    def generate(
        self,
        investment_data,
        revenue_data,
        cost_data
    ):

        ITERACIONES = 10000

        horizonte = 10

        TMAR = 0.12

        inversion = (
            investment_data[
                "inversion_total"
            ]
        )

        capacidad = (
            revenue_data[
                "capacidad_instalada"
            ]
        )

        precio = (
            revenue_data[
                "precio_unitario"
            ]
        )

        costos = (
            cost_data[
                "costos_operativos"
            ]
        )

        simulacion = []

        resultados_van = []

        for _ in range(
            ITERACIONES
        ):

            produccion_mc = np.random.triangular(

                capacidad * 0.80,

                capacidad,

                capacidad * 1.20
            )

            precio_mc = np.random.triangular(

                precio * 0.85,

                precio,

                precio * 1.15
            )

            costos_mc = np.random.normal(

                costos,

                costos * 0.10
            )

            ventas_mc = (

                produccion_mc *

                precio_mc
            )

            flujo_mc = (

                ventas_mc -

                costos_mc
            )

            flujos_mc = [

                flujo_mc
            ] * horizonte

            van_mc = self.calcular_van(

                inversion,

                flujos_mc,

                TMAR
            )

            resultados_van.append(
                van_mc
            )

            simulacion.append([

                precio_mc,

                produccion_mc,

                costos_mc,

                ventas_mc,

                van_mc
            ])

        df_multi = pd.DataFrame(

            simulacion,

            columns=[

                "Precio_Unitario",

                "Produccion",

                "Costos",

                "Ventas",

                "VAN"
            ]
        )

        probabilidad_exito = (

            (df_multi["VAN"] > 0)

            .mean()

            * 100
        )

        if probabilidad_exito >= 80:

            riesgo = "BAJO"

        elif probabilidad_exito >= 60:

            riesgo = "MEDIO"

        else:

            riesgo = "ALTO"

        return {

            "van_promedio":
                round(
                    df_multi["VAN"].mean(),
                    2
                ),

            "van_minimo":
                round(
                    df_multi["VAN"].min(),
                    2
                ),

            "van_maximo":
                round(
                    df_multi["VAN"].max(),
                    2
                ),

            "desviacion":
                round(
                    df_multi["VAN"].std(),
                    2
                ),

            "probabilidad_exito":
                round(
                    probabilidad_exito,
                    2
                ),

            "nivel_riesgo":
                riesgo,

            "dataset":
                    df_multi.to_dict(
                 orient="records"
        )
}
        