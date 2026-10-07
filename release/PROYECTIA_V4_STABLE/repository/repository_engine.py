import json
import os


class RepositoryEngine:

    def __init__(self):

        self.base_path = "projects"

        os.makedirs(
            self.base_path,
            exist_ok=True
        )

    def generate_project_id(self):

        folders = [

            folder

            for folder in os.listdir(
                self.base_path
            )

            if folder.startswith(
                "PROY_"
            )
        ]

        if not folders:

            return "PROY_0001"

        numbers = []

        for folder in folders:

            number = int(

                folder.replace(
                    "PROY_",
                    ""
                )
            )

            numbers.append(
                number
            )

        next_number = (
            max(numbers) + 1
        )

        return f"PROY_{next_number:04d}"

    def create_project_folder(self):

        project_id = (
            self.generate_project_id()
        )

        project_folder = os.path.join(
            self.base_path,
            project_id
        )

        os.makedirs(
            project_folder,
            exist_ok=True
        )

        return project_id, project_folder

    def save_json(
        self,
        project_folder,
        file_name,
        data
    ):

        file_path = os.path.join(
            project_folder,
            file_name
        )

        with open(
            file_path,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                data,
                f,
                indent=4,
                ensure_ascii=False
            )

    def update_projects_index(
        self,
        metadata
    ):

        index_file = os.path.join(
            self.base_path,
            "projects_index.json"
        )

        if os.path.exists(
            index_file
        ):

            with open(
                index_file,
                "r",
                encoding="utf-8"
            ) as file:

                projects = json.load(
                    file
                )

        else:

            projects = []

        projects.append(
            metadata
        )

        with open(
            index_file,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                projects,
                f,
                indent=4,
                ensure_ascii=False
            )