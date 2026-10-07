import numpy as np

from engines.visualization_engine.montecarlo_visualizer import (
    MonteCarloVisualizer
)

np.random.seed(42)

resultados = np.random.normal(

    1163082,

    210456,

    10000
)

visualizer = (
    MonteCarloVisualizer()
)

visualizer.generate(
    resultados
)

print(
    "✅ montecarlo_van.png generado"
)