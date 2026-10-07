class SensitivityEngine:

    def calcular_van(
        self,
        inversion,
        flujo,
        horizonte,
        tasa
    ):

        van = -inversion

        for anio in range(
            1,
            horizonte + 1
        ):

            van += (

                flujo /

                ((1 + tasa) ** anio)
            )

        return van

    def generate(
        self,
        investment_data,
        revenue_data,
        cost_data
    ):

        inversion = (
            investment_data[
                "inversion_total"
            ]
        )

        ventas = (
            revenue_data[
                "ventas"
            ]
        )

        costos = (
            cost_data[
                "costos_operativos"
            ]
        )

        flujo_base = (

            ventas -

            costos
        )

        tasa = 0.12

        horizonte = 10

        escenarios = {

            "Pesimista":
                0.85,

            "Base":
                1.00,

            "Optimista":
                1.15
        }

        resultado = {}

        for nombre, factor in escenarios.items():

            flujo = (
                flujo_base *
                factor
            )

            van = self.calcular_van(

                inversion,

                flujo,

                horizonte,

                tasa
            )

            resultado[nombre] = round(
                van,
                2
            )

        return resultado