import numpy as np
import pandas as pd


class LocalizationEngine:

    def generate(self):

        alternativas = pd.DataFrame({

            "Alternativa": [
                "Riobamba",
                "Ambato",
                "Latacunga",
                "Cuenca"
            ],

            "Tecnico": [85, 88, 82, 90],

            "Economico": [92, 80, 84, 70],

            "Logistico": [87, 90, 80, 88],

            "Ambiental": [91, 85, 88, 84],

            "Social": [89, 86, 82, 92],

            "Institucional": [83, 88, 80, 95],

            "Tecnologico": [80, 85, 82, 94],

            "Estrategico": [88, 90, 84, 96]
        })

        pesos = np.array([
            0.20,
            0.15,
            0.15,
            0.10,
            0.10,
            0.10,
            0.10,
            0.10
        ])

        X = alternativas.iloc[:, 1:].values

        normalizada = (
            X /
            np.sqrt((X ** 2).sum(axis=0))
        )

        ponderada = normalizada * pesos

        ideal_pos = ponderada.max(axis=0)

        ideal_neg = ponderada.min(axis=0)

        d_pos = np.sqrt(
            ((ponderada - ideal_pos) ** 2).sum(axis=1)
        )

        d_neg = np.sqrt(
            ((ponderada - ideal_neg) ** 2).sum(axis=1)
        )

        score = d_neg / (d_neg + d_pos)

        alternativas["score_topsis"] = score

        ranking = (
            alternativas
            .sort_values(
                "score_topsis",
                ascending=False
            )
            .reset_index(drop=True)
        )

        ubicacion_optima = ranking.loc[
            0,
            "Alternativa"
        ]

        score_integral = round(
            ranking.loc[
                0,
                "score_topsis"
            ] * 100,
            2
        )

        return {

            "ubicacion_optima":
                ubicacion_optima,

            "score_integral":
                score_integral,

            "ranking":
                ranking[
                    [
                        "Alternativa",
                        "score_topsis"
                    ]
                ].to_dict(
                    orient="records"
                )
        }