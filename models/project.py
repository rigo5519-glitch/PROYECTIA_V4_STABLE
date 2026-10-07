from dataclasses import dataclass, field


@dataclass
class Project:

    # Información básica
    project_id: str = ""

    project_name: str = ""

    sector: str = ""

    subsector: str = ""

    project_type: str = ""

    # Idea inicial
    idea: dict = field(default_factory=dict)

    # Diagnóstico
    diagnosis: dict = field(default_factory=dict)

    # Árbol de problemas
    problem_tree: dict = field(default_factory=dict)

    # Árbol de objetivos
    objective_tree: dict = field(default_factory=dict)

    # Marco lógico
    logical_framework: dict = field(default_factory=dict)