import json
import os


class KnowledgeEngine:

    def __init__(self):

        self.base_path = "knowledge_base"

    def load_sector(self, sector_file):

        file_path = os.path.join(
            self.base_path,
            sector_file
        )

        with open(
            file_path,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)

    def get_all_knowledge(self):

        knowledge = []

        for file in os.listdir(self.base_path):

            if file.endswith(".json"):

                knowledge.append(
                    self.load_sector(file)
                )

        return knowledge