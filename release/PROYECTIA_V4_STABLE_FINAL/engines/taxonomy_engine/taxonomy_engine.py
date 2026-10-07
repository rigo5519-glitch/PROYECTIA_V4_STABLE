import json


class TaxonomyEngine:

    def __init__(self):

        with open(
            "repository/taxonomy.json",
            encoding="utf-8"
        ) as f:

            self.taxonomy = json.load(f)

    def classify(
        self,
        idea
    ):

        idea_lower = idea.lower()

        for sector, datos in self.taxonomy.items():

            for keyword in datos["keywords"]:

                if keyword in idea_lower:

                    return {

                        "sector":
                        sector,

                        "subsector":
                        datos["subsector"],

                        "productos":
                        datos["productos"]
                    }

        return {

            "sector":
            "No identificado",

            "subsector":
            "No identificado",

            "productos":
            []
        }