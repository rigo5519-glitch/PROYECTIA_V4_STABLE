from engines.llm_orchestrator.llm_orchestrator_v2 import (
    LLMOrchestratorV2
)


class ExecutiveBriefGenerator:

    def generate(
        self,
        idea
    ):

        orchestrator = (
            LLMOrchestratorV2()
        )

        resultado = (
            orchestrator.analyze(
                idea
            )
        )

        brief = f"""
====================================================
RESUMEN EJECUTIVO DEL PROYECTO
====================================================

PROYECTO

{resultado["idea"]}

----------------------------------------------------

EXPERIENCIA ANALIZADA

Se analizaron
{resultado["proyectos_analizados"]}
proyectos similares del repositorio PROYECTIA.

----------------------------------------------------

INDICADORES REFERENCIALES

Ubicación recomendada:
{resultado["ubicacion_frecuente"]}

Inversión promedio:
USD {resultado["inversion_promedio"]:,.2f}

VAN promedio:
USD {resultado["van_promedio"]:,.2f}

----------------------------------------------------

FACTIBILIDAD

Nivel estimado:
{resultado["factibilidad"]}

----------------------------------------------------

ANÁLISIS EJECUTIVO

El análisis de proyectos históricos indica
que iniciativas similares presentan resultados
económicos favorables y niveles aceptables
de rentabilidad.

La ubicación más frecuente encontrada en
los proyectos analizados es:

{resultado["ubicacion_frecuente"]}

----------------------------------------------------

RECOMENDACIÓN ESTRATÉGICA

{resultado["recomendacion"]}

Se recomienda avanzar a la fase de
prefactibilidad para validar mercado,
ingeniería e inversión con mayor detalle.

====================================================
"""

        return brief