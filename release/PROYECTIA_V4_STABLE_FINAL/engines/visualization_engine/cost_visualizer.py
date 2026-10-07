import matplotlib.pyplot as plt


class CostVisualizer:

    def generate(
        self,
        cost_data,
        output_file="outputs/costos_operativos.png"
    ):

        conceptos = [

            "Personal",

            "Energia",

            "Mantenimiento",

            "Administracion"
        ]

        valores = [

            cost_data["personal"],

            cost_data["energia"],

            cost_data["mantenimiento"],

            cost_data["administracion"]
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
            "Distribucion de Costos Operativos"
        )

        plt.axis("equal")

        plt.savefig(
            output_file,
            dpi=300,
            bbox_inches="tight"
        )

        plt.close()