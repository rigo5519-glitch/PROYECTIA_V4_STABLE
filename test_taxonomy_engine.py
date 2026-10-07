from engines.taxonomy_engine.taxonomy_engine import (
    TaxonomyEngine
)

taxonomy = TaxonomyEngine()

resultado = taxonomy.classify(
    "Proyecto productivo de crianza y comercializacion de cuyes"
)

print(resultado)