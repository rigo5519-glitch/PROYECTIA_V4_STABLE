class DiagnosticEngine:

    def generate(self, project_data):

        sector = project_data["sector"]

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

        return {

            "problema_central":
            "Problema no identificado",

            "causas": [],

            "efectos": []
        }