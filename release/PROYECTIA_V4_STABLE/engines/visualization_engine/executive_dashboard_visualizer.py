import matplotlib.pyplot as plt


class ExecutiveDashboardVisualizer:

    def generate(
        self,
        dashboard_data,
        output_file="outputs/dashboard_ejecutivo.png"
    ):

        fig, ax = plt.subplots(
            figsize=(12, 8)
        )

        ax.axis("off")

        contenido = f"""
VAN: {dashboard_data['VAN']:,.2f}

TIR: {dashboard_data['TIR']} %

PRI: {dashboard_data['PRI']} años

B/C: {dashboard_data['BC']}

Probabilidad Éxito:
{dashboard_data['Probabilidad_Exito']} %

Nivel Riesgo:
{dashboard_data['Nivel_Riesgo']}

Score:
{dashboard_data['Score']}

Clasificación:
{dashboard_data['Clasificacion']}
"""

        ax.text(
            0.5,
            0.5,
            contenido,
            ha="center",
            va="center",
            fontsize=12,
            bbox=dict(
                facecolor="lightyellow",
                edgecolor="black"
            )
        )

        plt.title(
            "DASHBOARD EJECUTIVO PROYECTIA"
        )

        plt.savefig(
            output_file,
            dpi=300,
            bbox_inches="tight"
        )

        plt.close()