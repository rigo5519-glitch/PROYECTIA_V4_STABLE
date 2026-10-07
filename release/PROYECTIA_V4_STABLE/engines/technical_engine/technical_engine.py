class TechnicalEngine:

    def generate(
        self,
        project_data
    ):

        sector = project_data["sector"]

        if sector == "Agropecuario":

            return {

        "tamano":
            "Centro de producción pecuaria",

        "tecnologia":
            "Crianza tecnificada de cuyes",

        "infraestructura":
            "Galpones de reproducción y engorde",

        "equipos": [

            "Jaulas",

            "Comederos",

            "Bebederos",

            "Balanza",

            "Equipos sanitarios"
        ],

        "personal": [

            "Administrador",

            "Técnico Pecuario",

            "Operarios"
        ]
    }

        if sector == "Industria":

            return {

                "tamano":
                    "Pequeña industria",

                "tecnologia":
                    "Semiindustrial",

                "infraestructura":
                    "Planta de procesamiento",

                "equipos": [

                    "Tanque de enfriamiento",

                    "Pasteurizador",

                    "Envasadora"
                ],

                "personal": [

                    "Operador",

                    "Supervisor",

                    "Administrador"
                ]
            }

        elif sector == "Transporte":

            return {

                "tamano":
                    "Pequeña empresa",

                "tecnologia":
                    "Sistema logístico",

                "infraestructura":
                    "Patio de maniobras",

                "equipos": [

                    "Camiones",

                    "GPS",

                    "Software de gestión"
                ],

                "personal": [

                    "Conductores",

                    "Supervisor",

                    "Administrador"
                ]
            }

        elif sector == "Turismo":

            return {

                "tamano":
                    "Centro turístico",

                "tecnologia":
                    "Servicios turísticos",

                "infraestructura":
                    "Complejo turístico",

                "equipos": [

                    "Mobiliario",

                    "Equipamiento recreativo",

                    "Sistema de reservas"
                ],

                "personal": [

                    "Guías",

                    "Administrador",

                    "Personal operativo"
                ]
            }

        elif sector == "Reciclaje":

            return {

                "tamano":
                    "Planta de reciclaje",

                "tecnologia":
                    "Clasificación y procesamiento",

                "infraestructura":
                    "Centro de acopio",

                "equipos": [

                    "Trituradora",

                    "Clasificadora",

                    "Prensa hidráulica"
                ],

                "personal": [

                    "Operarios",

                    "Supervisor",

                    "Administrador"
                ]
            }

        return {

            "tamano":
                "No identificado"
        }
