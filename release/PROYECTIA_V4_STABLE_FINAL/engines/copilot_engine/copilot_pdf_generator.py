from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

from engines.copilot_engine.copilot_engine import (
    CopilotEngine
)


class CopilotPDFGenerator:

    def generate(
        self,
        idea,
        output_file="copilot_report.pdf"
    ):

        copilot = CopilotEngine()

        resultado = copilot.generate_report(
            idea
        )

        pdf = canvas.Canvas(
            output_file,
            pagesize=A4
        )

        y = 800

        lineas = [

            "PROYECTIA COPILOT REPORT",
            "",
            f"Idea: {resultado['idea']}",
            "",
            f"Proyectos Analizados: {resultado['proyectos_analizados']}",
            "",
            f"Ubicacion Recomendada: {resultado['ubicacion_frecuente']}",
            "",
            f"Inversion Promedio: USD {resultado['inversion_promedio']:,.2f}",
            "",
            f"VAN Promedio: USD {resultado['van_promedio']:,.2f}",
            "",
            f"Factibilidad: {resultado['factibilidad']}",
            "",
            "Recomendacion:",
            resultado['recomendacion']
        ]

        for linea in lineas:

            pdf.drawString(
                50,
                y,
                str(linea)
            )

            y -= 20

        pdf.save()

        return output_file
