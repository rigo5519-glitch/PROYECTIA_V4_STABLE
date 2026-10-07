from engines.search_engine.search_engine import SearchEngine


engine = SearchEngine()

results = engine.search_by_text(
    "lacteos"
)

print(results)