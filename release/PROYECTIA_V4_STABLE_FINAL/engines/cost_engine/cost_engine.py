class CostEngine:

    def generate(
        self,
        size_data
    ):

        categoria = (
            size_data["categoria"]
        )

        capacidad_instalada = (
            size_data[
                "capacidad_instalada"
            ]
        )

        if categoria == "PEQUEÑO":

            personal = 25000

        elif categoria == "MEDIANO":

            personal = 60000

        else:

            personal = 120000

        energia = (
            capacidad_instalada * 1.20
        )

        mantenimiento = (
            energia * 0.30
        )

        administracion = (
            personal * 0.20
        )

        costos_operativos = (

            personal +

            energia +

            mantenimiento +

            administracion
        )

        return {

            "personal":
                personal,

            "energia":
                round(
                    energia,
                    2
                ),

            "mantenimiento":
                round(
                    mantenimiento,
                    2
                ),

            "administracion":
                round(
                    administracion,
                    2
                ),

            "costos_operativos":
                round(
                    costos_operativos,
                    2
                )
        }