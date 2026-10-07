class RevenueEngine:

    def generate(
        self,
        market_data,
        size_data
    ):

        demanda_maxima = (
            market_data[
                "demanda_potencial"
            ]
        )

        capacidad_instalada = (
            size_data[
                "capacidad_instalada"
            ]
        )

        produccion_real = min(

            demanda_maxima,

            capacidad_instalada
        )

        precio_unitario = 25

        ventas = (

            produccion_real *

            precio_unitario
        )

        return {

            "demanda_maxima":
                demanda_maxima,

            "capacidad_instalada":
                capacidad_instalada,

            "produccion_real":
                produccion_real,

            "precio_unitario":
                precio_unitario,

            "ventas":
                ventas
        }