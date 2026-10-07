import matplotlib.pyplot as plt


class InvestmentVisualizer:

    def generate(
        self,
        investment_data,
        output_file="outputs/inversion_inicial.png"
    ):

        conceptos = [

            "Terreno",

            "Infraestructura",

            "Equipos",

            "Vehiculo",

            "Capital Trabajo"
        ]

        valores = [

            investment_data["terreno"],

            investment_data["infraestructura"],

            investment_data["equipos"],

            investment_data["vehiculo"],

            investment_data["capital_trabajo"]
        ]

        plt.figure(
            figsize=(8, 6)
        )

        plt.pie(

            valores,

            labels=conceptos,

            autopct="%1.1f%%",

            startangle=90
        )

        plt.title(
            "Distribución de la Inversión Inicial"
        )

        plt.axis("equal")

        plt.savefig(
            output_file,
            dpi=300,
            bbox_inches="tight"
        )

        plt.close()