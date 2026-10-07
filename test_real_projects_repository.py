from engines.real_projects_repository.real_projects_repository import (
    RealProjectsRepository
)

repo = RealProjectsRepository()

proyectos = repo.load_repository()

print(
    f"Proyectos cargados: {len(proyectos)}"
)

for proyecto in proyectos:

    print()

    print(
        proyecto["nombre_proyecto"]
    )