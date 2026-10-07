from engines.visualization_engine.sensitivity_visualizer import (
    SensitivityVisualizer
)

sensibilidad = {

    "Pesimista":
        932075.17,

    "Base":
        1149059.03,

    "Optimista":
        1366042.88
}

visualizer = (
    SensitivityVisualizer()
)

visualizer.generate(
    sensibilidad
)

print(
    "✅ sensibilidad_van.png generado"
)