from engines.objective_tree_engine.objective_tree_engine import ObjectiveTreeEngine

engine = ObjectiveTreeEngine()

problema = {
    "problema_central":
    "Deficiente prestacion de servicios de transporte"
}

print(engine.generate(problema))