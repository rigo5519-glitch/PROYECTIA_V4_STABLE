import sys
import os

BASE_DIR = os.path.join(
    os.path.dirname(__file__),
    "PROYECTIA_V4_STABLE"
)

sys.path.append(BASE_DIR)

from project_generator import ProjectGenerator

from engines.copilot_engine.executive_brief_docx import (
    ExecutiveBriefDOCX
)

from engines.copilot_engine.copilot_pdf_generator import (
    CopilotPDFGenerator
)

from engines.copilot_engine.prefeasibility_generator import (
    PrefeasibilityGenerator
)

from engines.factibility_engine.factibility_docx import (
    FactibilityDOCX
)



def main():

    idea = input(
        "\nIngrese la idea del proyecto:\n\n"
    )

    print(
        "\n🚀 GENERANDO PROYECTO...\n"
    )

    generator = ProjectGenerator()

    resultado = generator.generate_project(
        idea
    )

    projects = [

        p for p in os.listdir(
            "projects"
        )

        if p.startswith(
            "PROY_"
        )
    ]

    project_id = sorted(
        projects
    )[-1]

    project_path = os.path.join(
        "projects",
        project_id
    )

    project_master = resultado

    print(
        "✅ Project Master generado"
    )

    ExecutiveBriefDOCX().generate(
        idea,
        output_file=os.path.join(
            project_path,
            "executive_brief.docx"
        )
    )

    print(
        "✅ Executive Brief DOCX"
    )

    CopilotPDFGenerator().generate(
        idea,
        output_file=os.path.join(
            project_path,
            "copilot_report.pdf"
        )
    )

    print(
        "✅ PDF Ejecutivo"
    )

    PrefeasibilityGenerator().generate(
        project_master,
        output_file=os.path.join(
            project_path,
            "prefactibilidad.docx"
        )
    )

    FactibilityDOCX().generate(
    resultado["factibilidad"],
    output_file=os.path.join(
        project_path,
        "factibilidad.docx"
    )
)

    print(
        "✅ Factibilidad DOCX"
)

    print(
        "✅ Prefactibilidad DOCX"
    )

    print(
        "\n🏁 PROYECTO COMPLETADO\n"
    )


if __name__ == "__main__":

    main()