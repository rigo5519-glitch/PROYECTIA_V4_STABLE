import pandas as pd
import numpy as np

from engines.pca_engine.pca_engine import (
    PCAEngine
)

np.random.seed(42)

df_multi = pd.DataFrame({

    "Precio_Unitario":
        np.random.normal(
            25,
            2,
            500
        ),

    "Produccion":
        np.random.normal(
            14091,
            500,
            500
        ),

    "Costos":
        np.random.normal(
            93981,
            8000,
            500
        )
})

df_multi["Ventas"] = (

    df_multi[
        "Precio_Unitario"
    ]

    *

    df_multi[
        "Produccion"
    ]
)

df_multi["VAN"] = (

    df_multi[
        "Ventas"
    ]

    -

    df_multi[
        "Costos"
    ]
)

engine = PCAEngine()

resultado = engine.generate(
    df_multi
)

print(resultado)