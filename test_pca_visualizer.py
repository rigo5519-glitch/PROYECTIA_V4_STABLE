import pandas as pd
import numpy as np

from engines.visualization_engine.pca_visualizer import (
    PCAVisualizer
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
    df_multi["Precio_Unitario"]
    *
    df_multi["Produccion"]
)

df_multi["VAN"] = (
    df_multi["Ventas"]
    -
    df_multi["Costos"]
)

varianza = pd.DataFrame({

    "Componente":
        [1, 2, 3, 4, 5],

    "Acumulada_%":
        [58.46, 80.91, 99.98, 100, 100]
})

visualizer = PCAVisualizer()

visualizer.heatmap_correlacion(
    df_multi
)

visualizer.varianza_acumulada(
    varianza
)

print(
    "✅ PCA visualizaciones generadas"
)