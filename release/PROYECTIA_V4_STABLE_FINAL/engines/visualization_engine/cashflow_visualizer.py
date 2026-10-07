import matplotlib.pyplot as plt
import pandas as pd


class CashFlowVisualizer:

    def generate(
        self,
        cash_flow_data,
        output_file="outputs/flujo_caja.png"
    ):

        df = pd.DataFrame(
            cash_flow_data["tabla_flujo"]
        )

        plt.figure(
            figsize=(10, 6)
        )

        plt.plot(

            df["Periodo"],

            df["Flujo_Acumulado"],

            marker="o",

            linewidth=2,

            color="navy"
        )

        plt.axhline(

            y=0,

            color="red",

            linestyle="--",

            linewidth=2
        )

        plt.title(
            "Flujo Acumulado del Proyecto"
        )

        plt.xlabel(
            "Periodo"
        )

        plt.ylabel(
            "USD"
        )

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