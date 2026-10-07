from engines.idea_engine.idea_engine import IdeaEngine
from engines.diagnostic_engine.diagnostic_engine import DiagnosticEngine


# Motor de ideas
idea_engine = IdeaEngine()

project_data = idea_engine.analyze(
    "Quiero implementar una planta procesadora de lacteos"
)

# Motor de diagnóstico
diagnostic_engine = DiagnosticEngine()

diagnostico = diagnostic_engine.generate(
    project_data
)

print("\n=== INFORMACION DEL PROYECTO ===")
print(project_data)

print("\n=== DIAGNOSTICO ===")
print(diagnostico)