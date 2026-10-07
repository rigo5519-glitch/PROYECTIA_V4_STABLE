import json
import os


class SearchEngine:

    def __init__(self):

        self.index_file = os.path.join(
            "projects",
            "projects_index.json"
        )

    def load_projects(self):

        if not os.path.exists(
            self.index_file
        ):
            return []

        with open(
            self.index_file,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)

    def search_by_sector(
        self,
        sector
    ):

        projects = self.load_projects()

        return [

            project

            for project in projects

            if project["sector"] == sector
        ]
    def search_by_text(
        self,
        text
    ):

        projects = self.load_projects()

        text = text.lower()

        results = []

        for project in projects:

            if text in project["idea"].lower():

                results.append(project)

        return results