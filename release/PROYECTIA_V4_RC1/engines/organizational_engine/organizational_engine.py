class OrganizationalEngine:

    def generate(
        self,
        workforce_data
    ):

        estructura = {

            "nivel_estrategico": [

                "Gerente General"
            ],

            "nivel_tactico": [

                "Supervisor de Operaciones"
            ],

            "nivel_operativo": [

                "Operarios"
            ],

            "nivel_apoyo": [

                "Administrativo"
            ]
        }

        funciones = {

            "Gerente General":
                "Dirigir y controlar el proyecto",

            "Supervisor de Operaciones":
                "Coordinar procesos productivos",

            "Operarios":
                "Ejecutar actividades operativas",

            "Administrativo":
                "Gestionar documentación y soporte"
        }

        return {

            "estructura":
                estructura,

            "funciones":
                funciones,

            "personal":
                workforce_data["personal"]
        }