class DiagnosticEngine:

    def generate(self, project_data):

        sector = project_data["sector"]

        # INDUSTRIA
        if sector == "Industria":

            return {

                "problema_central":
                    "Bajo aprovechamiento industrial de la produccion",

                "causas": [

                    "Limitada capacidad de procesamiento",

                    "Escasa tecnologia industrial",

                    "Bajo valor agregado"
                ],

                "efectos": [

                    "Menores ingresos de productores",

                    "Perdida de competitividad",

                    "Desaprovechamiento productivo"
                ]
            }

        # TRANSPORTE
        elif sector == "Transporte":

            return {

                "problema_central":
                    "Deficiente prestacion de servicios de transporte",

                "causas": [

                    "Flota insuficiente",

                    "Altos costos operativos",

                    "Problemas logisticos"
                ],

                "efectos": [

                    "Baja cobertura de servicio",

                    "Incremento de costos",

                    "Perdida de competitividad"
                ]
            }

        # TURISMO
        elif sector == "Turismo":

            return {

                "problema_central":
                    "Baja afluencia de visitantes",

                "causas": [

                    "Escasa promocion turistica",

                    "Infraestructura insuficiente",

                    "Oferta limitada de servicios"
                ],

                "efectos": [

                    "Bajos ingresos locales",

                    "Menor dinamizacion economica",

                    "Poco desarrollo territorial"
                ]
            }

        # RECICLAJE
        elif sector == "Reciclaje":

            return {

                "problema_central":
                    "Bajo aprovechamiento de residuos solidos",

                "causas": [

                    "Escasa separacion en origen",

                    "Infraestructura insuficiente",

                    "Limitada cultura ambiental"
                ],

                "efectos": [

                    "Contaminacion ambiental",

                    "Desperdicio de materiales",

                    "Baja economia circular"
                ]
            }

        return {

            "problema_central":
                "Problema no identificado",

            "causas": [],

            "efectos": []
        }