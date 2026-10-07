from engines.semantic_validator_engine.semantic_validator_engine import (
    SemanticValidatorEngine
)

problem_tree = {

    "problema_central":
        "Bajo aprovechamiento industrial de la produccion"
}

objective_tree = {

    "objetivo_general":
        "Incrementar aprovechamiento industrial de la produccion"
}

logical_framework = {

    "indicadores": [
        "Nivel de productividad"
    ]
}

validator = (
    SemanticValidatorEngine()
)

resultado = validator.validate(

    problem_tree,

    objective_tree,

    logical_framework
)

print(resultado)