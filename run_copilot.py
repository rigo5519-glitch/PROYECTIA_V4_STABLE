from project_generator import ProjectGenerator

from engines.copilot_engine.executive_brief_docx import (
    ExecutiveBriefDOCX
)

from engines.copilot_engine.copilot_pdf_generator import (
    CopilotPDFGenerator
)

idea = input(
    "Ingrese la idea del proyecto: "
)

generator = ProjectGenerator()

generator.generate_project(
    idea
)

ExecutiveBriefDOCX().generate(
    idea
)

CopilotPDFGenerator().generate(
    idea
)

print(
    "\n✅ Proyecto generado"
)

print(
    "✅ Executive Brief DOCX generado"
)

print(
    "✅ PDF generado"
)