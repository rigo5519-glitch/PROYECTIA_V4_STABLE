from engines.bc_engine.bc_engine import (
    BCEngine
)

van = {

    "VAN":
        704804.01
}

investment = {

    "inversion_total":
        297500
}

engine = BCEngine()

resultado = engine.generate(

    van,

    investment
)

print(resultado)