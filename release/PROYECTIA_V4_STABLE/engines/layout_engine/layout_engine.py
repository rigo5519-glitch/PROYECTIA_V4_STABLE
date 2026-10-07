class LayoutEngine:

    def generate(
        self,
        size_data,
        process_data
    ):

        categoria = (
            size_data["categoria"]
        )

        if categoria == "PEQUEÑO":

            superficie = 500

        elif categoria == "MEDIANO":

            superficie = 1200

        else:

            superficie = 2500

        areas = [

            {
                "nombre":
                    "Recepcion",

                "porcentaje":
                    15
            },

            {
                "nombre":
                    "Produccion",

                "porcentaje":
                    40
            },

            {
                "nombre":
                    "Control Calidad",

                "porcentaje":
                    10
            },

            {
                "nombre":
                    "Almacenamiento",

                "porcentaje":
                    20
            },

            {
                "nombre":
                    "Administracion",

                "porcentaje":
                    10
            },

            {
                "nombre":
                    "Servicios",

                "porcentaje":
                    5
            }
        ]

        for area in areas:

            area["m2"] = round(

                superficie *

                area["porcentaje"] / 100,

                2
            )

        flujo = [

            "Recepcion",

            "Produccion",

            "Control Calidad",

            "Almacenamiento",

            "Despacho"
        ]

        return {

            "categoria":
                categoria,

            "superficie_total_m2":
                superficie,

            "areas":
                areas,

            "flujo":
                flujo,

            "layout_tipo":
                "Lineal"
        }