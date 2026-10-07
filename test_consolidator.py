from engines.consolidator_engine.consolidator_engine import (
    ConsolidatorEngine
)

engine = ConsolidatorEngine()

resultado = engine.consolidate(

    {"idea": "demo"},

    {"diagnostic": "demo"},

    {"problem_tree": "demo"},

    {"objective_tree": "demo"},

    {"logical_framework": "demo"},

    {"market": "demo"},

    {"technical": "demo"}
)

print(resultado)