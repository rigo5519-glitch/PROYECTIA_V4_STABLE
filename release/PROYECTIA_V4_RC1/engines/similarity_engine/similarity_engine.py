from engines.search_engine.search_engine import SearchEngine


class SimilarityEngine:

    def find_similar_projects(
        self,
        project_data
    ):

        sector = project_data["sector"]

        search = SearchEngine()

        projects = search.search_by_sector(
            sector
        )

        return projects

    def get_best_match(
        self,
        project_data
    ):

        projects = self.find_similar_projects(
            project_data
        )

        if not projects:

            return None

        return projects[0]