from engines.investment_engine.investment_engine import (
    InvestmentEngine
)

size_data = {

    "categoria":
        "MEDIANO"
}

engine = InvestmentEngine()

resultado = engine.generate(
    size_data
)

print(resultado)