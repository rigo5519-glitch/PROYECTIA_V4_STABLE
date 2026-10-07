import matplotlib.pyplot as plt
import numpy as np


class MonteCarloVisualizer:

    def generate(
        self,
        resultados_van,
        output_file="outputs/montecarlo_van.png"
    ):

        plt.figure(
            figsize=(10, 6)
        )

        plt.hist(

            resultados_van,

            bins=50,

            color="steelblue",

            edgecolor="black",

            alpha=0.7
        )

        plt.axvline(

            np.mean(
                resultados_van
            ),

            color="red",

            linestyle="--",

            linewidth=2,

            label="VAN Promedio"
        )

        plt.axvline(

            0,

            color="black",

            linestyle=":",

            linewidth=2,

            label="VAN = 0"
        )

        plt.title(
            "Distribución Monte Carlo del VAN"
        )

        plt.xlabel(
            "VAN"
        )

        plt.ylabel(
            "Frecuencia"
        )

        plt.legend()

        plt.grid(
            alpha=0.3
        )

        plt.tight_layout()

        plt.savefig(
            output_file,
            dpi=300,
            bbox_inches="tight"
        )

        plt.close()
