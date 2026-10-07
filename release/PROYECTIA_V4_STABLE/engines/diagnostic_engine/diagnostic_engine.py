from engines.similarity_engine.similarity_engine import SimilarityEngine


class DiagnosticEngine:

    def generate(self, project_data):

        similarity = SimilarityEngine()

        similar_project = (
            similarity.get_best_match(
                project_data
            )
        )

        sector = project_data["sector"]

        if similar_project:

            experiencia = (
                f"Experiencia recuperada: "
                f"{similar_project['project_id']}"
            )

        else:

            experiencia = (
                "No existen proyectos similares"
            )

        if sector == "Industria":

            return {

                "experiencia":
                    experiencia,

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

        elif sector == "Transporte":

            return {

                "experiencia":
                    experiencia,

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

        elif sector == "Turismo":

            return {

                "experiencia":
                    experiencia,

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

        elif sector == "Reciclaje":

            return {

                "experiencia":
                    experiencia,

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

        elif sector == "Agropecuario":

            return {

            "experiencia":
            experiencia,

        "problema_central":
            "Baja producción tecnificada y comercialización de cuyes",

        "causas": [

            "Limitado manejo técnico",

            "Escasa asistencia veterinaria",

            "Baja organización comercial"
        ],

        "efectos": [

            "Bajos ingresos de productores",

            "Menor productividad",

            "Oferta insuficiente para el mercado"
        ]
    }

        return {

            "experiencia":
                experiencia,

            "problema_central":
                "Problema no identificado",

            "causas": [],

            "efectos": []
        }