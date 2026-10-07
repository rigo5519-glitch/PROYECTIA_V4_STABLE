class WorkforceEngine:

    def generate(
        self,
        size_data
    ):

        categoria = (
            size_data["categoria"]
        )

        if categoria == "PEQUEÑO":

            personal = {

                "Gerente": 1,

                "Supervisor": 1,

                "Operarios": 3,

                "Administrativo": 1
            }

        elif categoria == "MEDIANO":

            personal = {

                "Gerente": 1,

                "Supervisor": 2,

                "Operarios": 8,

                "Administrativo": 2
            }

        else:

            personal = {

                "Gerente": 1,

                "Supervisor": 3,

                "Operarios": 15,

                "Administrativo": 3
            }

        salarios = {

            "Gerente": 1800,

            "Supervisor": 1200,

            "Operarios": 700,

            "Administrativo": 900
        }

        costo_mensual = 0

        for cargo, cantidad in personal.items():

            costo_mensual += (

                salarios[cargo]

                * cantidad
            )

        costo_anual = (
            costo_mensual * 12
        )

        return {

            "categoria":
                categoria,

            "personal":
                personal,

            "salarios":
                salarios,

            "costo_mensual":
                costo_mensual,

            "costo_anual":
                costo_anual
        }