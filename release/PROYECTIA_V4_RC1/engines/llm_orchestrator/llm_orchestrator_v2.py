from collections import Counter

from engines.rag_engine.rag_engine import (
    RAGEngine
)


class LLMOrchestratorV2:

    def analyze(
        self,
        idea
    ):

        rag = RAGEngine()

        proyectos = rag.retrieve(
            idea
        )

        if not proyectos:

            return {

                "idea": idea,

                "factibilidad":
                    "SIN DATOS"
            }

        inversiones = []

        vans = []

        ubicaciones = []

        procesados = 0

        for proyecto in proyectos:

            pm = (
                rag.retrieve_project_master(
                    proyecto["project_id"]
                )
            )

            if pm is None:
                continue

            procesados += 1

            if "investment" in pm:

                inversiones.append(

                    pm["investment"]
                    .get(
                        "inversion_total",
                        0
                    )
                )

            if "van" in pm:

                vans.append(

                    pm["van"]
                    .get(
                        "VAN",
                        0
                    )
                )

            if "localization" in pm:

                ubicaciones.append(

                    pm["localization"]
                    .get(
                        "ubicacion_optima",
                        "N/D"
                    )
                )

        inversion_promedio = (
            sum(inversiones)
            /
            len(inversiones)
            if inversiones
            else 0
        )

        van_promedio = (
            sum(vans)
            /
            len(vans)
            if vans
            else 0
        )

        ubicacion_frecuente = (
            Counter(
                ubicaciones
            ).most_common(1)[0][0]
            if ubicaciones
            else "N/D"
        )

        if van_promedio > 0:

            factibilidad = "ALTA"

        else:

            factibilidad = "BAJA"

        return {

            "idea":
                idea,

            "proyectos_analizados":
                procesados,

            "inversion_promedio":
                round(
                    inversion_promedio,
                    2
                ),

            "van_promedio":
                round(
                    van_promedio,
                    2
                ),

            "ubicacion_frecuente":
                ubicacion_frecuente,

            "factibilidad":
                factibilidad,

            "recomendacion":

                f"Se analizaron "
                f"{procesados} proyectos similares "
                f"con una inversión promedio de "
                f"{round(inversion_promedio,2)} USD "
                f"y un VAN promedio de "
                f"{round(van_promedio,2)} USD."
        }