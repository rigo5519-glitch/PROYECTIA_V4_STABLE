from engines.organizational_engine.organizational_engine import (
    OrganizationalEngine
)

workforce = {

    "personal": {

        "Gerente": 1,

        "Supervisor": 2,

        "Operarios": 8,

        "Administrativo": 2
    }
}

engine = (
    OrganizationalEngine()
)

resultado = engine.generate(
    workforce
)

print(resultado)
