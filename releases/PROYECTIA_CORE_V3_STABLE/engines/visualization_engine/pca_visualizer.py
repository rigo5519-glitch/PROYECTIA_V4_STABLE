import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


class PCAVisualizer:

    def heatmap_correlacion(
        self,
        df_multi,
        output_file="outputs/pca_heatmap.png"
    ):

        corr = df_multi.corr()

        plt.figure(
            figsize=(8, 6)
        )

        sns.heatmap(

            corr,

            annot=True,

            cmap="coolwarm",

            fmt=".2f"
        )

        plt.title(
            "Matriz de Correlación"
        )

        plt.tight_layout()

        plt.savefig(
            output_file,
            dpi=300
        )

        plt.close()

    def varianza_acumulada(
        self,
        varianza_df,
        output_file="outputs/pca_varianza.png"
    ):

        plt.figure(
            figsize=(8, 5)
        )

        plt.plot(

            varianza_df["Componente"],

            varianza_df["Acumulada_%"],

            marker="o"
        )

        plt.axhline(

            y=80,

            color="red",

            linestyle="--"
        )

        plt.title(
            "Varianza Acumulada"
        )

        plt.xlabel(
            "Componente Principal"
        )

        plt.ylabel(
            "Varianza Acumulada (%)"
        )

        plt.grid(
            alpha=0.3
        )

        plt.tight_layout()

        plt.savefig(
            output_file,
            dpi=300
        )

        plt.close()