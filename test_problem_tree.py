from engines.idea_engine.idea_engine import IdeaEngine
from engines.diagnostic_engine.diagnostic_engine import DiagnosticEngine
from engines.problem_tree_engine.problem_tree_engine import ProblemTreeEngine


# IDEA ENGINE
idea_engine = IdeaEngine()

project_data = idea_engine.analyze(
    "Quiero implementar una planta procesadora de lacteos"
)

# DIAGNOSTIC ENGINE
diagnostic_engine = DiagnosticEngine()

diagnostic = diagnostic_engine.generate(
    project_data
)

# PROBLEM TREE ENGINE
problem_tree_engine = ProblemTreeEngine()

problem_tree = problem_tree_engine.generate(
    diagnostic
)

print("\n==============================")
print("PROYECTIA CORE V3")
print("==============================")

print("\nIDEA")
print(project_data)

print("\nDIAGNOSTICO")
print(diagnostic)

print("\nARBOL DE PROBLEMAS")
print(problem_tree)