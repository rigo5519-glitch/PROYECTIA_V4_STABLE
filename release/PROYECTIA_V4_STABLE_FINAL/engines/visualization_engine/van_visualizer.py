import matplotlib.pyplot as plt
import pandas as pd


class VANVisualizer:

    def generate(
        self,
        cash_flow_data,
        output_file="outputs/van_acumulado.png"
    ):

        df = pd.DataFrame(
            cash_flow_data["tabla_flujo"]
        )

        TMAR = 0.12

        valor_presente = []

        for _, fila in df.iterrows():

            vp = (

                fila["Flujo"]

                /

                ((1 + TMAR) ** fila["Periodo"])
            )

            valor_presente.append(vp)

        df["Valor_Presente"] = valor_presente

        df["VAN_Acumulado"] = (

            df["Valor_Presente"]
            .cumsum()
        )

        plt.figure(
            figsize=(10, 6)
        )

        plt.plot(

            df["Periodo"],

            df["VAN_Acumulado"],

            marker="o",

            linewidth=2,

            color="green"
        )

        plt.axhline(

            y=0,

            color="red",

            linestyle="--",

            linewidth=2
        )

        plt.title(
            "VAN Acumulado"
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