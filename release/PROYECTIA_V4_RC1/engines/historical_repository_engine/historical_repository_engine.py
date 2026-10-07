from datetime import datetime


class HistoricalRepositoryEngine:

    def create_record(
        self,
        project_master,
        semantic_result,
        xai_result
    ):

        return {

            "problema":
                project_master[
                    "problem_tree"
                ][
                    "problema_central"
                ],

            "objetivo":
                project_master[
                    "objective_tree"
                ][
                    "objetivo_general"
                ],

            "score_semantico":
                semantic_result[
                    "indice_global"
                ],

            "estado_xai":
                xai_result[
                    "nivel"
                ],

            "fecha":
                str(
                    datetime.now()
                ),

            "estado_proyecto":
                "Pendiente"
        }