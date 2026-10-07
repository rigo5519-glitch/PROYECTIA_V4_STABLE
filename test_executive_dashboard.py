from engines.executive_dashboard_engine.executive_dashboard_engine import (
    ExecutiveDashboardEngine
)

van = {

    "VAN": 704804.01
}

tir = {

    "TIR": 53.73
}

pri = {

    "PRI_Exacto": 2.02
}

bc = {

    "BC": 3.37
}

montecarlo = {

    "probabilidad_exito": 100.0,

    "nivel_riesgo": "BAJO"
}

engine = ExecutiveDashboardEngine()

resultado = engine.generate(

    van,

    tir,

    pri,

    bc,

    montecarlo
)

print(resultado)