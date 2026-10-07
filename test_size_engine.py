from engines.size_engine.size_engine import (
    SizeEngine
)

market_data = {

    "demanda_efectiva": 10500
}

localization_data = {

    "ubicacion_optima":
        "Riobamba",

    "score_integral":
        62.5
}

engine = SizeEngine()

resultado = engine.generate(

    market_data,

    localization_data
)

print(resultado)