class InvestmentEngine:

    def generate(
        self,
        size_data
    ):

        categoria = (
            size_data["categoria"]
        )

        if categoria == "PEQUEÑO":

            equipos = 50000

        elif categoria == "MEDIANO":

            equipos = 150000

        else:

            equipos = 300000

        infraestructura = (
            equipos * 0.50
        )

        terreno = (
            infraestructura * 0.40
        )

        capital_trabajo = (
            equipos * 0.15
        )

        if categoria == "GRANDE":

            vehiculo = 50000

        else:

            vehiculo = 20000

        inversion_total = (

            terreno +

            infraestructura +

            equipos +

            vehiculo +

            capital_trabajo
        )

        return {

            "categoria":
                categoria,

            "terreno":
                terreno,

            "infraestructura":
                infraestructura,

            "equipos":
                equipos,

            "vehiculo":
                vehiculo,

            "capital_trabajo":
                capital_trabajo,

            "inversion_total":
                inversion_total
        }