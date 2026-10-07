class MarketingEngine:

    def generate(
        self,
        project_data,
        market_data
    ):

        sector = project_data["sector"]

        if sector == "Industria":

            producto = "Lácteos"

            canales = [

                "Supermercados",

                "Tiendas",

                "Distribuidores"
            ]

        elif sector == "Reciclaje":

            producto = "Material Reciclado"

            canales = [

                "Industria",

                "Acopiadores",

                "Municipios"
            ]

        elif sector == "Turismo":

            producto = "Servicios Turísticos"

            canales = [

                "Redes Sociales",

                "Agencias",

                "Web"
            ]

        else:

            producto = "Servicio"

            canales = [

                "Directo",

                "Digital"
            ]

        return {

            "producto":
                producto,

            "precio":
                "Competitivo",

            "plaza":
                "Mercado regional",

            "promocion": [

                "Redes Sociales",

                "Página Web",

                "Publicidad local"
            ],

            "canales":
                canales,

            "segmentacion": {

                "geografica":
                    "Regional",

                "demografica":
                    "Población económicamente activa",

                "socioeconomica":
                    "Media"
            },

            "estrategia":

                "Penetración de mercado",

            "mercado_objetivo":

                market_data[
                    "mercado_objetivo"
                ]
        }