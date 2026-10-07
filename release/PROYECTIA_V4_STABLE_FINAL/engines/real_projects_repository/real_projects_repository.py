class RealProjectsRepository:

    def load_repository(self):

        proyectos = [

            {
                "id": 1,

                "institucion": "BID",

                "pais": "Ecuador",

                "nombre_proyecto":
                    "Inversiones Resilientes en Transmisión y Distribución de Energía Eléctrica",

                "sector":
                    "Energia",

                "subsector":
                    "Transmision Electrica",

                "objetivo":
                    "Mejorar confiabilidad y capacidad del sistema electrico",

                "monto_usd":
                    300000000
            },

            {
                "id": 2,

                "institucion": "BID",

                "pais": "Ecuador",

                "nombre_proyecto":
                    "Programa Energias Renovables Ecuador",

                "sector":
                    "Energia",

                "subsector":
                    "Renovables",

                "objetivo":
                    "Respaldar proyectos solares e hidroelectricos",

                "monto_usd":
                    77000000
            },

            {
                "id": 3,

                "institucion": "CAF",

                "pais": "Ecuador",

                "nombre_proyecto":
                    "Programa Integral de Vialidad y Agua Potable",

                "sector":
                    "Infraestructura",

                "subsector":
                    "Movilidad Urbana",

                "objetivo":
                    "Mejorar calidad de vida",

                "monto_usd":
                    87158060
            },

            {
                "id": 4,

                "institucion": "Banco Mundial",

                "pais": "Ecuador",

                "nombre_proyecto":
                    "Guayas Resilient Rural Roads",

                "sector":
                    "Transporte",

                "subsector":
                    "Vialidad Rural",

                "objetivo":
                    "Incrementar resiliencia vial rural",

                "monto_usd":
                    100000000
            }
        ]

        return proyectos