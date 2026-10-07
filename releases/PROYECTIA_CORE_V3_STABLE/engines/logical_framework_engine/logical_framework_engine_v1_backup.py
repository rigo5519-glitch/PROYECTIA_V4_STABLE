class LogicalFrameworkEngine:

    def generate(self, objective_tree):

        return {

            "fin":
                "Contribuir al desarrollo productivo del sector",

            "proposito":
                objective_tree["objetivo_general"],

            "componentes": [

                "Infraestructura implementada",

                "Tecnologia instalada",

                "Personal capacitado"
            ],

            "actividades": [

                "Construccion de infraestructura",

                "Adquisicion de equipos",

                "Capacitacion del personal"
            ]
        }