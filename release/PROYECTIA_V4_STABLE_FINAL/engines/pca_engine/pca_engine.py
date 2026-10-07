import pandas as pd

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA


class PCAEngine:

    def generate(self, df_multi):

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

        pca = PCA()

        componentes = pca.fit_transform(
            X_std
        )

        varianza = pd.DataFrame({

            "Componente":
                range(
                    1,
                    len(
                        pca.explained_variance_ratio_
                    ) + 1
                ),

            "Varianza_%":
                (
                    pca.explained_variance_ratio_
                    * 100
                )
        })

        varianza[
            "Acumulada_%"
        ] = (

            varianza[
                "Varianza_%"
            ]
            .cumsum()
        )

        cargas = pd.DataFrame(

            pca.components_.T,

            columns=[
                f"CP{i}"
                for i in range(
                    1,
                    len(variables)+1
                )
            ],

            index=variables
        )

        return {

            "varianza":
                varianza.round(2)
                .to_dict(
                    orient="records"
                ),

            "cargas":
                cargas.round(3)
                .to_dict()
        }