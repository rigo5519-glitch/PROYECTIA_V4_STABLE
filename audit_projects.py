import os
import json

projects_path = "projects"

validos = []
invalidos = []

for carpeta in os.listdir(projects_path):

    ruta = os.path.join(
        projects_path,
        carpeta,
        "project_master.json"
    )

    if not os.path.exists(ruta):
        continue

    try:

        with open(
            ruta,
            encoding="utf-8"
        ) as f:

            json.load(f)

        validos.append(carpeta)

    except Exception as e:

        invalidos.append(
            (carpeta, str(e))
        )

print("\nPROYECTOS VALIDOS\n")

print(len(validos))

print("\nPROYECTOS INVALIDOS\n")

for p, err in invalidos:

    print(
        p,
        "->",
        err
    )