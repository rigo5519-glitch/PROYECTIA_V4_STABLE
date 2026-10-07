class IdeaEngine:

    def analyze(self, idea):

        idea_lower = idea.lower()

        result = {

            "idea_original": idea,

            "sector": "No identificado",

            "subsector": "No identificado",

            "actividad": "No identificada"
        }

        # CACAO
        if any(
            palabra in idea_lower
            for palabra in [
                "cacao",
                "chocolate",
                "acopio de cacao"
            ]
        ):

            result["sector"] = "Industria"

            result["subsector"] = "Agroindustria"

            result["actividad"] = (
                "Acopio y procesamiento de cacao"
            )

        # LACTEOS
        elif any(
            palabra in idea_lower
            for palabra in [
                "lacteo",
                "lacteos",
                "leche",
                "queso",
                "yogur",
                "yogurt",
                "planta procesadora"
            ]
        ):

            result["sector"] = "Industria"

            result["subsector"] = "Agroindustria"

            result["actividad"] = (
                "Procesamiento de lacteos"
            )

        # AGROPECUARIO
        elif any(
            palabra in idea_lower
            for palabra in [
                "cuy",
                "cuyes",
                "ganado",
                "bovino",
                "porcino",
                "avicola",
                "avicultura",
                "tilapia",
                "trucha"
            ]
        ):

            result["sector"] = "Agropecuario"

            result["subsector"] = "Produccion Pecuaria"

            result["actividad"] = (
                "Crianza y comercializacion pecuaria"
            )

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

            result["actividad"] = (
                "Servicios de transporte"
            )

        # TURISMO
        elif any(
            palabra in idea_lower
            for palabra in [
                "turismo",
                "turistico",
                "ecoturismo",
                "hotel",
                "hosteria"
            ]
        ):

            result["sector"] = "Turismo"

            result["subsector"] = (
                "Turismo Comunitario"
            )

            result["actividad"] = (
                "Servicios turisticos"
            )

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

            result["subsector"] = (
                "Residuos Solidos"
            )

            result["actividad"] = (
                "Gestion de residuos"
            )

        return result