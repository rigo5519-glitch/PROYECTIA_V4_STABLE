class IdeaEngine:

    def analyze(self, idea):

        idea_lower = idea.lower()

        result = {

            "idea_original": idea,

            "sector": "No identificado",

            "subsector": "No identificado",

            "actividad": "No identificada"
        }

        # INDUSTRIA
        if any(
            palabra in idea_lower
            for palabra in [
                "lacteo",
                "lacteos",
                "leche",
                "queso",
                "yogur",
                "planta procesadora"
            ]
        ):

            result["sector"] = "Industria"
            result["subsector"] = "Agroindustria"
            result["actividad"] = "Procesamiento de lacteos"

        # TRANSPORTE
        elif any(
            palabra in idea_lower
            for palabra in [
                "transporte",
                "camiones",
                "logistica",
                "carga pesada"
            ]
        ):

            result["sector"] = "Transporte"
            result["subsector"] = "Carga Pesada"
            result["actividad"] = "Servicios de transporte"

        # TURISMO
        elif any(
            palabra in idea_lower
            for palabra in [
                "turismo",
                "turistico",
                "ecoturismo",
                "hotel"
            ]
        ):

            result["sector"] = "Turismo"
            result["subsector"] = "Turismo Comunitario"
            result["actividad"] = "Servicios turisticos"

        # RECICLAJE
        elif any(
            palabra in idea_lower
            for palabra in [
                "reciclaje",
                "residuos",
                "neumaticos",
                "plastico"
            ]
        ):

            result["sector"] = "Reciclaje"
            result["subsector"] = "Residuos Solidos"
            result["actividad"] = "Gestion de residuos"

        return result