import matplotlib.pyplot as plt


class ProblemTreeVisualizer:

    def generate(
        self,
        problem_tree,
        output_file="arbol_problemas.png"
    ):

        fig, ax = plt.subplots(
            figsize=(12, 8)
        )

        ax.axis("off")

        problema = (
            problem_tree[
                "problema_central"
            ]
        )

        ax.text(

            0.5,

            0.55,

            problema,

            ha="center",

            va="center",

            fontsize=12,

            bbox=dict(

                facecolor="gold",

                edgecolor="black"
            )
        )

        # EFECTOS

        y = 0.90

        for efecto in (
            problem_tree[
                "efectos"
            ]
        ):

            ax.text(

                0.5,

                y,

                efecto["efecto"],

                ha="center",

                fontsize=10,

                bbox=dict(

                    facecolor="lightcoral"
                )
            )

            y -= 0.10

        # CAUSAS

        y = 0.30

        for causa in (
            problem_tree[
                "causas"
            ]
        ):

            ax.text(

                0.5,

                y,

                causa["causa"],

                ha="center",

                fontsize=10,

                bbox=dict(

                    facecolor="lightgreen"
                )
            )

            y -= 0.10

        plt.title(
            "ARBOL DE PROBLEMAS"
        )

        plt.savefig(

            output_file,

            dpi=300,

            bbox_inches="tight"
        )

        plt.close()