import numpy as np


class SizeEngine:

    def generate(
        self,
        market_data,
        localization_data
    ):

        demanda_efectiva = (
            market_data["demanda_efectiva"]
        )

        demanda_maxima = round(
            demanda_efectiva * 1.22
        )

        score_localizacion = (
            localization_data[
                "score_integral"
            ]
        )

        # Factores 09B
        mercado_score = min(
            demanda_maxima / 15000,
            1
        ) * 100

        tecnologia_score = 85

        localizacion_score = (
            score_localizacion
        )

        financiamiento_score = 80

        operacion_score = 78

        pesos = [

            0.35,
            0.20,
            0.15,
            0.15,
            0.15
        ]

        valores = [

            mercado_score,

            tecnologia_score,

            localizacion_score,

            financiamiento_score,

            operacion_score
        ]

        score_tamano = np.average(
            valores,
            weights=pesos
        )

        capacidad_instalada = round(
            demanda_maxima * 1.10
        )

        if capacidad_instalada < 5000:

            categoria = "PEQUEÑO"

        elif capacidad_instalada < 15000:

            categoria = "MEDIANO"

        else:

            categoria = "GRANDE"

        if score_tamano >= 85:

            factibilidad = "MUY FACTIBLE"

        elif score_tamano >= 70:

            factibilidad = "FACTIBLE"

        else:

            factibilidad = "POCO FACTIBLE"

        return {

            "ubicacion_optima":
                localization_data[
                    "ubicacion_optima"
                ],

            "demanda_maxima":
                demanda_maxima,

            "capacidad_instalada":
                capacidad_instalada,

            "categoria":
                categoria,

            "factibilidad":
                factibilidad,

            "score_tamano":
                round(
                    score_tamano,
                    2
                )
        }