import matplotlib.pyplot as plt


class SensitivityVisualizer:

    def generate(
        self,
        sensibilidad_data,
        output_file="outputs/sensibilidad_van.png"
    ):

        escenarios = list(
            sensibilidad_data.keys()
        )

        vans = list(
            sensibilidad_data.values()
        )

        plt.figure(
            figsize=(8, 5)
        )

        plt.bar(

            escenarios,

            vans,

            color=[
                "red",
                "steelblue",
                "green"
            ]
        )

        plt.title(
            "Sensibilidad del VAN"
        )

        plt.ylabel(
            "USD"
        )

        plt.grid(
            axis="y",
            alpha=0.3
        )

        plt.tight_layout()

        plt.savefig(
            output_file,
            dpi=300,
            bbox_inches="tight"
        )

        plt.close()