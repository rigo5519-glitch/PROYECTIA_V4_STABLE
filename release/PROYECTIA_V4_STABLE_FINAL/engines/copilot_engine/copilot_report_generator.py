from engines.copilot_engine.copilot_engine import (
    CopilotEngine
)


class CopilotReportGenerator:

    def generate(
        self,
        idea
    ):

        copilot = CopilotEngine()

        resultado = copilot.generate_report(
            idea
        )

        reporte = f"""
==================================================
PROYECTIA COPILOT REPORT
==================================================

IDEA DEL PROYECTO

{resultado["idea"]}

--------------------------------------------------

PROYECTOS ANALIZADOS

{resultado["proyectos_analizados"]}

--------------------------------------------------

UBICACION RECOMENDADA

{resultado["ubicacion_frecuente"]}

--------------------------------------------------

INVERSION PROMEDIO

USD {resultado["inversion_promedio"]:,.2f}

--------------------------------------------------

VAN PROMEDIO

USD {resultado["van_promedio"]:,.2f}

--------------------------------------------------

FACTIBILIDAD

{resultado["factibilidad"]}

--------------------------------------------------

RECOMENDACION

{resultado["recomendacion"]}

------------------------------------------------

CONCLUSION

La experiencia almacenada en PROYECTIA indica
que proyectos similares presentan resultados
favorables y condiciones de factibilidad positivas.

Se recomienda avanzar a la siguiente fase de
formulacion y evaluacion detallada del proyecto.

==================================================
"""

        return reporte