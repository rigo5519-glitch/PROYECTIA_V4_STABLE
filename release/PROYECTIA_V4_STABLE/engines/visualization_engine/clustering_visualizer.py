import matplotlib.pyplot as plt
import pandas as pd


class ClusteringVisualizer:

    def cluster_distribution(
        self,
        probabilidades,
        output_file=
        "outputs/clustering_probabilidades.png"
    ):

        labels = [
            f"Cluster {k}"
            for k in probabilidades.keys()
        ]

        valores = list(
            probabilidades.values()
        )

        plt.figure(
            figsize=(8, 5)
        )

        plt.bar(
            labels,
            valores,
            color="steelblue"
        )

        plt.title(
            "Probabilidad por Cluster"
        )

        plt.ylabel("%")

        plt.grid(
            axis="y",
            alpha=0.3
        )

        plt.tight_layout()

        plt.savefig(
            output_file,
            dpi=300
        )

        plt.close()

    def cluster_van(
        self,
        clusters,
        output_file=
        "outputs/clustering_van.png"
    ):

        df = pd.DataFrame(
            clusters
        )

        plt.figure(
            figsize=(8, 5)
        )

        plt.bar(

            df["Cluster"]
            .astype(str),

            df["VAN"],

            color="green"
        )

        plt.title(
            "VAN Promedio por Cluster"
        )

        plt.ylabel(
            "VAN"
        )

        plt.grid(
            axis="y",
            alpha=0.3
        )

        plt.tight_layout()

        plt.savefig(
            output_file,
            dpi=300
        )

        plt.close()