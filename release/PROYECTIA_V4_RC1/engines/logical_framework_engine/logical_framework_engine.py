class LogicalFrameworkEngine:

    def generate(
        self,
        objective_tree
    ):

        return {

            "fin":
                "Contribuir al desarrollo sostenible del sector",

            "proposito":
                objective_tree[
                    "objetivo_general"
                ],

            "componentes": [

                "Infraestructura implementada",

                "Tecnologia instalada",

                "Capacitacion ejecutada"
            ],

            "actividades": [

                "Diseño",

                "Adquisicion",

                "Implementacion",

                "Operacion"
            ],

            "indicadores": [

                "Porcentaje de avance",

                "Cobertura alcanzada",

                "Nivel de productividad"
            ],

            "medios_verificacion": [

                "Informes tecnicos",

                "Registros operativos",

                "Actas de seguimiento"
            ],

            "supuestos": [

                "Disponibilidad financiera",

                "Apoyo institucional",

                "Condiciones favorables del entorno"
            ]
        }