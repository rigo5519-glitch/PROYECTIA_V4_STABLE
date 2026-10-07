import json
import os


def get_last_project():

    projects = [

        p for p in os.listdir(
            "projects"
        )

        if p.startswith(
            "PROY_"
        )
    ]

    ultimo = sorted(
        projects
    )[-1]

    return os.path.join(
        "projects",
        ultimo
    )


def load_project_master():

    project_path = get_last_project()

    with open(
        os.path.join(
            project_path,
            "project_master.json"
        ),
        encoding="utf-8"
    ) as f:

        return json.load(f)