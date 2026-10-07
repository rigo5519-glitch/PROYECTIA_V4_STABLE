class ProblemTreeEngine:

    def generate(self, diagnostic):

        problema = diagnostic["problema_central"]

        causas = diagnostic["causas"]

        efectos = diagnostic["efectos"]

        arbol = {

            "problema_central": problema,

            "causas": [],

            "efectos": []
        }

        for causa in causas:

            arbol["causas"].append({

                "causa": causa,

                "subcausas": [

                    f"Origen relacionado con {causa}",

                    f"Limitaciones asociadas a {causa}"
                ]
            })

        for efecto in efectos:

            arbol["efectos"].append({

                "efecto": efecto,

                "subefectos": [

                    f"Impacto asociado a {efecto}",

                    f"Consecuencia derivada de {efecto}"
                ]
            })

        return arbol