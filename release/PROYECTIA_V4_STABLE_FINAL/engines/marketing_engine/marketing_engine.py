class MarketingEngine:

    def generate(
        self,
        project_data,
        market_data
    ):

        sector = project_data["sector"]

        idea = (
            project_data["idea_original"]
            .lower()
        )

        # AGROPECUARIO
        if sector == "Agropecuario":

            if "cuy" in idea:

                producto = "Carne de cuy"

                canales = [
                    "Restaurantes",
                    "Mercados",
                    "Consumidor final"
                ]

            elif "trucha" in idea:

                producto = "Trucha"

                canales = [
                    "Restaurantes",
                    "Mercados",
                    "Mayoristas"
                ]

            elif "tilapia" in idea:

                producto = "Tilapia"

                canales = [
                    "Mercados",
                    "Mayoristas",
                    "Restaurantes"
                ]

            else:

                producto = "Producto pecuario"

                canales = [
                    "Mercados",
                    "Mayoristas",
                    "Consumidor final"
                ]

        # INDUSTRIA
        elif sector == "Industria":

            if "cacao" in idea:

                producto = "Cacao procesado"

                canales = [
                    "Exportadores",
                    "Industria alimentaria",
                    "Comercializadores"
                ]

            elif "cafe" in idea or "café" in idea:

                producto = "Café procesado"

                canales = [
                    "Exportadores",
                    "Comercializadores"
                ]

            elif any(
                palabra in idea
                for palabra in [
                    "lacteo",
                    "lacteos",
                    "leche",
                    "queso",
                    "yogur",
                    "yogurt"
                ]
            ):

                producto = "Lácteos"

                canales = [
                    "Supermercados",
                    "Tiendas",
                    "Distribuidores"
                ]

            else:

                producto = "Producto industrial"

                canales = [
                    "Distribuidores",
                    "Mayoristas"
                ]

        # RECICLAJE
        elif sector == "Reciclaje":

            producto = "Material Reciclado"

            canales = [
                "Industria",
                "Acopiadores",
                "Municipios"
            ]

        # TURISMO
        elif sector == "Turismo":

            producto = "Servicios Turísticos"

            canales = [
                "Redes Sociales",
                "Agencias",
                "Web"
            ]

        # OTROS
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