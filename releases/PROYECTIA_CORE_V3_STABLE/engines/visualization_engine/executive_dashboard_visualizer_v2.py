import matplotlib.pyplot as plt
import numpy as np


class ExecutiveDashboardVisualizerV2:

    def generate(
        self,
        dashboard,
        output_file=
        "outputs/dashboard_ejecutivo_v2.png"
    ):

        fig = plt.figure(
            figsize=(14, 10)
        )

        # KPI
        ax1 = plt.subplot2grid(
            (2, 2),
            (0, 0)
        )

        ax1.axis("off")

        texto = f"""
VAN: {dashboard['VAN']:,.2f}

TIR: {dashboard['TIR']} %

PRI: {dashboard['PRI']} años

B/C: {dashboard['BC']}

Prob. Éxito:
{dashboard['Probabilidad_Exito']} %

Riesgo:
{dashboard['Nivel_Riesgo']}
"""

        ax1.text(
            0,
            0.5,
            texto,
            fontsize=12
        )

        ax1.set_title(
            "KPI Ejecutivos"
        )

        # Radar Chart
        categorias = [

            "VAN",
            "TIR",
            "PRI",
            "BC",
            "Exito"
        ]

        valores = [

            min(
                dashboard["VAN"] / 1000000,
                1
            ) * 100,

            min(
                dashboard["TIR"],
                100
            ),

            100 -
            min(
                dashboard["PRI"] * 10,
                100
            ),

            min(
                dashboard["BC"] * 20,
                100
            ),

            dashboard[
                "Probabilidad_Exito"
            ]
        ]

        valores += valores[:1]

        angulos = np.linspace(

            0,

            2 * np.pi,

            len(categorias),

            endpoint=False
        )

        angulos = np.concatenate(
            (
                angulos,
                [angulos[0]]
            )
        )

        ax2 = plt.subplot(
            222,
            polar=True
        )

        ax2.plot(
            angulos,
            valores
        )

        ax2.fill(
            angulos,
            valores,
            alpha=0.3
        )

        ax2.set_xticks(
            angulos[:-1]
        )

        ax2.set_xticklabels(
            categorias
        )

        ax2.set_title(
            "Radar Financiero"
        )

        # Score
        ax3 = plt.subplot2grid(
            (2, 2),
            (1, 0),
            colspan=2
        )

        ax3.axis("off")

        color = (
            "green"
            if dashboard[
                "Score"
            ] >= 90
            else
            "orange"
        )

        ax3.text(

            0.5,

            0.5,

            f"SCORE = "
            f"{dashboard['Score']}\n"
            f"{dashboard['Clasificacion']}",

            fontsize=20,

            ha="center",

            color=color
        )

        ax3.set_title(
            "Resultado Integral"
        )

        plt.tight_layout()

        plt.savefig(
            output_file,
            dpi=300
        )

        plt.close()