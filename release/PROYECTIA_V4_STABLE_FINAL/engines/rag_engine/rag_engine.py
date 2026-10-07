import json
import os


class RAGEngine:

    def retrieve(
        self,
        idea,
        projects_path="projects"
    ):

        palabras = set(
            idea.lower().split()
        )

        resultados = []

        for carpeta in os.listdir(
            projects_path
        ):

            metadata_path = os.path.join(
                projects_path,
                carpeta,
                "metadata.json"
            )

            project_master_path = os.path.join(
                projects_path,
                carpeta,
                "project_master.json"
            )

            if not os.path.exists(
                metadata_path
            ):
                continue

            if not os.path.exists(
                project_master_path
            ):
                continue

            try:

                with open(
                    metadata_path,
                    encoding="utf-8"
                ) as f:

                    metadata = json.load(f)

                with open(
                    project_master_path,
                    encoding="utf-8"
                ) as f:

                    pm = json.load(f)

                required_fields = [
                    "investment",
                    "van"
                ]

                if not all(
                    field in pm
                    for field in required_fields
                ):
                    continue

                texto = (
                    metadata.get(
                        "idea",
                        ""
                    ).lower()
                )

                coincidencias = sum(
                    palabra in texto
                    for palabra in palabras
                )

                resultados.append({

                    "project_id":
                        metadata.get(
                            "project_id"
                        ),

                    "idea":
                        metadata.get(
                            "idea"
                        ),

                    "sector":
                        metadata.get(
                            "sector"
                        ),

                    "subsector":
                        metadata.get(
                            "subsector"
                        ),

                    "score":
                        coincidencias
                })

            except Exception as e:

                print(
                    "ERROR:",
                    carpeta,
                    e
                )

                continue

        resultados.sort(
            key=lambda x: (
                x["score"],
                x["project_id"]
            ),
            reverse=True
        )

        return resultados[:5]

    def retrieve_project_master(
        self,
        project_id,
        projects_path="projects"
    ):

        ruta = os.path.join(
            projects_path,
            project_id,
            "project_master.json"
        )

        if not os.path.exists(
            ruta
        ):
            return None

        with open(
            ruta,
            encoding="utf-8"
        ) as f:

            return json.load(f)