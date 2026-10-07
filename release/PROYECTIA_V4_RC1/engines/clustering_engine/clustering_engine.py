import pandas as pd

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans


class ClusteringEngine:

    def generate(
        self,
        df_multi
    ):

        variables = [

            "Precio_Unitario",

            "Produccion",

            "Costos",

            "Ventas",

            "VAN"
        ]

        X = df_multi[variables]

        scaler = StandardScaler()

        X_std = scaler.fit_transform(X)

        modelo = KMeans(

            n_clusters=2,

            random_state=42,

            n_init=10
        )

        clusters = modelo.fit_predict(
            X_std
        )

        df_multi["Cluster"] = clusters

        resumen = (

            df_multi
            .groupby("Cluster")
            .agg({

                "Precio_Unitario":
                    "mean",

                "Produccion":
                    "mean",

                "Costos":
                    "mean",

                "Ventas":
                    "mean",

                "VAN":
                    "mean"
            })

            .round(2)

            .reset_index()
        )

        probabilidades = (

            df_multi["Cluster"]
            .value_counts(
                normalize=True
            )

            * 100
        )

        return {

            "clusters":

                resumen.to_dict(
                    orient="records"
                ),

            "probabilidades":

                probabilidades.round(
                    2
                ).to_dict()
        }