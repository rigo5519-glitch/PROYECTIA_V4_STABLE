class ProblemTreeEngine:

    def generate(self, diagnostic):

        return {

            "problema_central":
                diagnostic["problema_central"],

            "causas":
                diagnostic["causas"],

            "efectos":
                diagnostic["efectos"]
        }