class FactibilityEngine:

    def generate(
        self,
        project_master
    ):

        return {

            "resumen_ejecutivo":
                self.generar_resumen(
                    project_master
                ),

            "mercado":
                project_master["market"],

            "marketing":
                project_master["marketing"],

            "tecnico":
                project_master["technical"],

            "financiero":
                self.generar_financiero(
                    project_master
                ),

            "riesgos":
                self.generar_riesgos(
                    project_master
                ),

            "conclusion":
                self.generar_conclusion(
                    project_master
                )
        }

    def generar_financiero(
        self,
        pm
    ):

        return {

            "van":
                pm["van"],

            "tir":
                pm["tir"],

            "pri":
                pm["pri"],

            "bc":
                pm["bc"]
        }

    def generar_riesgos(
        self,
        pm
    ):

        return {

            "sensibilidad":
                pm["sensitivity"],

            "montecarlo":
                pm["montecarlo"],

            "pca":
                pm["pca"],

            "clustering":
                pm["clustering"]
        }

    def generar_resumen(
        self,
        pm
    ):

        return {

            "idea":
                pm["idea"][
                    "idea_original"
                ],

            "problema":
                pm["diagnostic"][
                    "problema_central"
                ],

            "objetivo":
                pm["objective_tree"][
                    "objetivo_general"
                ]
        }

    def generar_conclusion(
        self,
        pm
    ):

        van = float(
            pm["van"]["VAN"]
        )

        tir = float(
            pm["tir"]["TIR"]
        )

        bc = float(
            pm["bc"]["BC"]
        )

        if (
            van > 0
            and tir > 12
            and bc > 1
        ):

            return (
                "El proyecto es económica y "
                "financieramente factible."
            )

        return (
            "El proyecto requiere "
            "revisión y ajustes."
        )