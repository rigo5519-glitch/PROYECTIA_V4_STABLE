from engines.marketing_engine.marketing_engine import (
    MarketingEngine
)

project = {

    "sector":
        "Industria"
}

market = {

    "mercado_objetivo":
        14000
}

engine = MarketingEngine()

resultado = engine.generate(

    project,

    market
)

print(resultado)