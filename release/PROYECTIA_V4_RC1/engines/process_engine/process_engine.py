class ProcessEngine:

    def generate(
        self,
        project_data
    ):

        sector = project_data["sector"]

        if sector == "Industria":

            procesos = [

                "Recepcion de Materia Prima",

                "Clasificacion",

                "Procesamiento",

                "Control de Calidad",

                "Almacenamiento",

                "Despacho"
            ]

        elif sector == "Reciclaje":

            procesos = [

                "Recepcion de NFU",

                "Clasificacion",

                "Trituracion",

                "Separacion",

                "Almacenamiento",

                "Comercializacion"
            ]

        elif sector == "Turismo":

            procesos = [

                "Captacion de Clientes",

                "Reservas",

                "Prestacion del Servicio",

                "Seguimiento",

                "Fidelizacion"
            ]

        else:

            procesos = [

                "Captacion",

                "Validacion",

                "Procesamiento",

                "Entrega"
            ]

        sipoc = {

            "Proveedor":
                "Usuarios",

            "Entrada":
                "Datos",

            "Proceso":
                "Evaluacion",

            "Salida":
                "Resultados",

            "Cliente":
                "Gerencia"
        }

        cadena_valor = [

            "Captacion",

            "Validacion",

            "Analitica",

            "IA",

            "XAI",

            "Reportes"
        ]

        return {

            "procesos":
                procesos,

            "sipoc":
                sipoc,

            "cadena_valor":
                cadena_valor
        }