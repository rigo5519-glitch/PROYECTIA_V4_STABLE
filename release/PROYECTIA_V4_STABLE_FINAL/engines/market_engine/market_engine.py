class MarketEngine:

    def generate(
        self,
        project_data
    ):

        sector = project_data["sector"]

        # Valores base
        poblacion_objetivo = 50000

        aceptacion = 80.0

        factor_penetracion = 0.35

        factor_uso = 0.75

        mercado_potencial = (
            poblacion_objetivo *
            aceptacion / 100
        )

        mercado_objetivo = (
            mercado_potencial *
            factor_penetracion
        )

        demanda_potencial = (
            mercado_objetivo
        )

        demanda_efectiva = (
            demanda_potencial *
            factor_uso
        )

        oferta_actual = 12000

        demanda_insatisfecha = max(
            demanda_efectiva -
            oferta_actual,
            0
        )

        indice_saturacion = (
            oferta_actual /
            mercado_potencial
        ) * 100

        indice_viabilidad = min(
            (
                demanda_efectiva /
                max(oferta_actual, 1)
            ) * 100,
            100
        )

        if indice_viabilidad >= 80:

            clasificacion = "ALTA"

        elif indice_viabilidad >= 60:

            clasificacion = "MEDIA"

        else:

            clasificacion = "BAJA"

        return {

            "poblacion_objetivo":
                poblacion_objetivo,

            "aceptacion":
                aceptacion,

            "mercado_potencial":
                mercado_potencial,

            "mercado_objetivo":
                mercado_objetivo,

            "demanda_potencial":
                demanda_potencial,

            "demanda_efectiva":
                demanda_efectiva,

            "oferta_actual":
                oferta_actual,

            "demanda_insatisfecha":
                demanda_insatisfecha,

            "indice_saturacion":
                round(
                    indice_saturacion,
                    2
                ),

            "indice_viabilidad":
                round(
                    indice_viabilidad,
                    2
                ),

            "clasificacion":
                clasificacion
        }