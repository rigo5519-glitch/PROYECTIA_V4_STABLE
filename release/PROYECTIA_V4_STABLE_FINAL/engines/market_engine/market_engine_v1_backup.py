class MarketEngine:

    def generate(
        self,
        project_data
    ):

        sector = project_data["sector"]

        actividad = project_data["actividad"]

        if sector == "Industria":

            return {

                "producto":
                    "Lácteos",

                "mercado_objetivo":
                    "Consumidores finales",

                "clientes":
                    "Hogares y comercios",

                "demanda":
                    "Por estimar",

                "oferta":
                    "Por estimar",

                "competencia":
                    "Por identificar"
            }

        elif sector == "Transporte":

            return {

                "producto":
                    "Servicio de transporte",

                "mercado_objetivo":
                    "Empresas y productores",

                "clientes":
                    "Sector logístico",

                "demanda":
                    "Por estimar",

                "oferta":
                    "Por estimar",

                "competencia":
                    "Por identificar"
            }

        elif sector == "Turismo":

            return {

                "producto":
                    "Servicios turísticos",

                "mercado_objetivo":
                    "Visitantes",

                "clientes":
                    "Turistas nacionales e internacionales",

                "demanda":
                    "Por estimar",

                "oferta":
                    "Por estimar",

                "competencia":
                    "Por identificar"
            }

        elif sector == "Reciclaje":

            return {

                "producto":
                    "Material reciclado",

                "mercado_objetivo":
                    "Empresas recicladoras",

                "clientes":
                    "Industria y municipios",

                "demanda":
                    "Por estimar",

                "oferta":
                    "Por estimar",

                "competencia":
                    "Por identificar"
            }

        return {

            "producto":
                "No identificado"
        }
