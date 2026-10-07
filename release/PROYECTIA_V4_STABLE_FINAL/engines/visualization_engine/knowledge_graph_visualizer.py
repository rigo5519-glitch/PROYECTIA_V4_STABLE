import matplotlib.pyplot as plt


class KnowledgeGraphVisualizer:

    def generate(
        self,
        graph_data,
        output_file="outputs/knowledge_graph.png"
    ):

        fig, ax = plt.subplots(
            figsize=(10, 8)
        )

        ax.axis("off")

        nodos = graph_data["nodos"]

        y = 0.9

        posiciones = {}

        for nodo in nodos:

            posiciones[
                nodo["id"]
            ] = (0.5, y)

            ax.text(

                0.5,

                y,

                nodo["label"],

                ha="center",

                va="center",

                fontsize=10,

                bbox=dict(

                    facecolor="lightblue",

                    edgecolor="black"
                )
            )

            y -= 0.15

        for relacion in (
            graph_data["relaciones"]
        ):

            origen = (
                posiciones[
                    relacion["source"]
                ]
            )

            destino = (
                posiciones[
                    relacion["target"]
                ]
            )

            ax.arrow(

                origen[0],

                origen[1] - 0.03,

                0,

                destino[1]
                -
                origen[1]
                +
                0.06,

                head_width=0.02,

                length_includes_head=True,

                color="black"
            )

        plt.title(
            "KNOWLEDGE GRAPH PROYECTIA"
        )

        plt.savefig(
            output_file,
            dpi=300,
            bbox_inches="tight"
        )

        plt.close()