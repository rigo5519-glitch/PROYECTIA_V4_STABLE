import matplotlib.pyplot as plt


class ObjectiveTreeVisualizer:

    def generate(
        self,
        objective_tree,
        output_file="outputs/arbol_objetivos.png"
    ):

        fig, ax = plt.subplots(
            figsize=(12, 8)
        )

        ax.axis("off")

        objetivo = (
            objective_tree[
                "objetivo_general"
            ]
        )

        ax.text(

            0.5,

            0.55,

            objetivo,

            ha="center",

            va="center",

            fontsize=12,

            bbox=dict(
                facecolor="gold",
                edgecolor="black"
            )
        )

        # FINES

        y = 0.90

        for fin in (
            objective_tree[
                "fines"
            ]
        ):

            ax.text(

                0.5,

                y,

                fin,

                ha="center",

                fontsize=10,

                bbox=dict(
                    facecolor="lightblue"
                )
            )

            y -= 0.10

        # MEDIOS

        y = 0.30

        for medio in (
            objective_tree[
                "medios"
            ]
        ):

            ax.text(

                0.5,

                y,

                medio,

                ha="center",

                fontsize=10,

                bbox=dict(
                    facecolor="lightgreen"
                )
            )

            y -= 0.10

        plt.title(
            "ARBOL DE OBJETIVOS"
        )

        plt.savefig(
            output_file,
            dpi=300,
            bbox_inches="tight"
        )

        plt.close()