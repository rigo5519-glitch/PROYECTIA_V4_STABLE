from engines.search_engine.search_engine import SearchEngine


engine = SearchEngine()

resultado = engine.search_by_sector(
    "Industria"
)

print(resultado)