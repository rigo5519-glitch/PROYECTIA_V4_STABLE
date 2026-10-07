from engines.visualization_engine.clustering_visualizer import (
    ClusteringVisualizer
)

clusters = [

    {
        "Cluster": 0,
        "VAN": 1338526
    },

    {
        "Cluster": 1,
        "VAN": 1002053
    }
]

probabilidades = {

    0: 48.97,

    1: 51.03
}

visualizer = (
    ClusteringVisualizer()
)

visualizer.cluster_distribution(
    probabilidades
)

visualizer.cluster_van(
    clusters
)

print(
    "✅ clustering visualizaciones generadas"
)