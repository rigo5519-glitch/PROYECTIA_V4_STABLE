from engines.idea_engine.idea_engine import IdeaEngine
from engines.diagnostic_engine.diagnostic_engine import DiagnosticEngine
from engines.problem_tree_engine.problem_tree_engine import ProblemTreeEngine
from engines.objective_tree_engine.objective_tree_engine import ObjectiveTreeEngine
from engines.logical_framework_engine.logical_framework_engine import LogicalFrameworkEngine
from repository.repository_engine import RepositoryEngine
from engines.market_engine.market_engine import MarketEngine
from engines.technical_engine.technical_engine import TechnicalEngine
from engines.consolidator_engine.consolidator_engine import (ConsolidatorEngine)
from engines.localization_engine.localization_engine import (LocalizationEngine)
from engines.size_engine.size_engine import (SizeEngine)
from engines.cash_flow_engine.cash_flow_engine import (CashFlowEngine)
from engines.investment_engine.investment_engine import (InvestmentEngine)
from engines.cost_engine.cost_engine import (CostEngine)
from engines.revenue_engine.revenue_engine import (RevenueEngine)
from engines.van_engine.van_engine import (VANEngine)
from engines.workforce_engine.workforce_engine import (WorkforceEngine)
from engines.process_engine.process_engine import (ProcessEngine)
from engines.marketing_engine.marketing_engine import (MarketingEngine)
from engines.tir_engine.tir_engine import (TIREngine)
from engines.pri_engine.pri_engine import (PRIEngine)
from engines.bc_engine.bc_engine import (BCEngine)
from engines.sensitivity_engine.sensitivity_engine import (SensitivityEngine)
from engines.montecarlo_engine.montecarlo_engine import (MonteCarloEngine)
from engines.pca_engine.pca_engine import (PCAEngine)
from engines.clustering_engine.clustering_engine import (ClusteringEngine)
from engines.executive_dashboard_engine.executive_dashboard_engine import (ExecutiveDashboardEngine)
from engines.organizational_engine.organizational_engine import (OrganizationalEngine)
from engines.layout_engine.layout_engine import (LayoutEngine)
from engines.knowledge_graph_engine.knowledge_graph_engine_v3 import (KnowledgeGraphEngineV3)



class ProjectGenerator:

    def generate_project(self, idea):

        # IDEA
        idea_engine = IdeaEngine()
        project_data = idea_engine.analyze(idea)

        # DIAGNOSTICO
        diagnostic_engine = DiagnosticEngine()
        diagnostic = diagnostic_engine.generate(project_data)

        # ARBOL DE PROBLEMAS
        problem_tree_engine = ProblemTreeEngine()
        problem_tree = problem_tree_engine.generate(diagnostic)

        # ARBOL DE OBJETIVOS
        objective_tree_engine = ObjectiveTreeEngine()
        objective_tree = objective_tree_engine.generate(problem_tree)

        # MARCO LOGICO
        logical_framework_engine = LogicalFrameworkEngine()
        logical_framework = logical_framework_engine.generate(
            objective_tree
        )
        market_engine = MarketEngine()

        market = market_engine.generate(
        project_data
)

        marketing_engine = MarketingEngine()

        marketing = marketing_engine.generate(
        project_data,
        market
)

        technical_engine = TechnicalEngine()
        
        technical = technical_engine.generate(
         project_data
        )
        localization_engine = LocalizationEngine()
        
        localization = localization_engine.generate()
        
        size_engine = SizeEngine()
        
        size = size_engine.generate(
        market,
        localization
        )
        
        workforce_engine = WorkforceEngine()

        workforce = workforce_engine.generate(
        size
)

        organizational_engine = OrganizationalEngine()

        organizational = organizational_engine.generate(
        workforce
)

        process_engine = ProcessEngine()

        process = process_engine.generate(
        project_data
)

        layout_engine = LayoutEngine()

        layout = layout_engine.generate(
        size,
        process
)
        
        investment_engine = InvestmentEngine()
        
        investment = investment_engine.generate(
                size
        )
        
        cost_engine = CostEngine()
        
        costs = cost_engine.generate(
                size
        )
        
        revenue_engine = RevenueEngine()
        
        revenue = revenue_engine.generate(
        market,
         size
        )
        
        
        cash_flow_engine = CashFlowEngine()
        
        cash_flow = cash_flow_engine.generate(
        
                investment,
        
                costs,
        
                revenue
        )
        van_engine = VANEngine()
        
        van = van_engine.generate(
        cash_flow
        )
        tir_engine = TIREngine()

        tir = tir_engine.generate(
        cash_flow
)
        pri_engine = PRIEngine()

        pri = pri_engine.generate(
        cash_flow
)

        bc_engine = BCEngine()

        bc = bc_engine.generate(
           van,
          investment
)

        sensitivity_engine = SensitivityEngine()

        sensitivity = sensitivity_engine.generate(
        investment,
        revenue,
        costs
)

        montecarlo_engine = MonteCarloEngine()

        montecarlo = montecarlo_engine.generate(

         investment,

        revenue,

         costs
)

# PCA ENGINE

        import pandas as pd

        df_multi = pd.DataFrame(
        montecarlo["dataset"]
)

        pca_engine = PCAEngine()

        pca = pca_engine.generate(
        df_multi
)

   # CLUSTERING

        clustering_engine = ClusteringEngine()

        clustering = clustering_engine.generate(
        df_multi
)

        # DASHBOARD

        dashboard_engine = ExecutiveDashboardEngine()

        dashboard = dashboard_engine.generate(
         van,
         tir,
         pri,
         bc,
         montecarlo
)



        # CONSOLIDADOR

        consolidator = ConsolidatorEngine()

        project_master = consolidator.consolidate(
         project_data,
         diagnostic,
         problem_tree,
         objective_tree,
         logical_framework,

         market,
         marketing,

         technical,
         localization,
         size,

         workforce,
         process,

         organizational,

         layout,

         investment,
         costs,
         revenue,

         cash_flow,

         van,
         tir,
         pri,
         bc,

         sensitivity,

         montecarlo,

         pca,

         clustering,

         dashboard
)

        # KNOWLEDGE GRAPH

        knowledge_graph_engine = KnowledgeGraphEngineV3()

        knowledge_graph = knowledge_graph_engine.generate(
        project_master
)

        project_master["knowledge_graph"] = (
        knowledge_graph
)


        repo = RepositoryEngine()

        project_id, project_folder = (
        repo.create_project_folder()
)

        repo.save_json(
        project_folder,
        "idea.json",
        project_data
)

        repo.save_json(
        project_folder,
        "diagnostic.json",
        diagnostic
)

        repo.save_json(
        project_folder,
        "problem_tree.json",
        problem_tree
)

        repo.save_json(
        project_folder,
        "objective_tree.json",
        objective_tree
)

        repo.save_json(
        project_folder,
        "logical_framework.json",
        logical_framework
)
        repo.save_json(
        project_folder,
        "market.json",
        market
)
        repo.save_json(
        project_folder,
        "technical.json",
        technical
)

        repo.save_json(
        project_folder,
        "size.json",
        size
)
        repo.save_json(
        project_folder,
        "cash_flow.json",
         cash_flow
)

        repo.save_json(
        project_folder,
         "investment.json",
         investment
)

        repo.save_json(
         project_folder,
         "costs.json",
         costs
)

        repo.save_json(
         project_folder,
         "revenue.json",
         revenue
)

        repo.save_json(
        project_folder,
        "process.json",
        process
)

        repo.save_json(
         project_folder,
        "marketing.json",
        marketing
)

        repo.save_json(
        project_folder,
        "tir.json",
        tir
)

        repo.save_json(
        project_folder,
        "pri.json",
        pri
)
        repo.save_json(
        project_folder,
        "bc.json",
        bc
)


        metadata = {

        "project_id":
        project_id,

        "idea":
        project_data["idea_original"],

        "sector":
        project_data["sector"],

        "subsector":
        project_data["subsector"],

        "actividad":
        project_data["actividad"]
}

        repo.save_json(
        project_folder,
        "metadata.json",
        metadata
)
        repo.update_projects_index(
        metadata
)
        repo.save_json(
        project_folder,
        "project_master.json",
        project_master
      
)

        repo.save_json(
        project_folder,
        "localization.json",
        localization
)

       


        repo.save_json(
        project_folder,
        "van.json",
         van
)

        repo.save_json(
        project_folder,
         "workforce.json",
         workforce
)

        repo.save_json(
          project_folder,
         "sensitivity.json",
         sensitivity
)
        repo.save_json(
         project_folder,
         "montecarlo.json",
         montecarlo
)

        repo.save_json(
         project_folder,
         "pca.json",
        pca
)

        repo.save_json(
         project_folder,
         "clustering.json",
         clustering
)

        repo.save_json(
         project_folder,
         "dashboard.json",
         dashboard
)

        repo.save_json(
        project_folder,
        "organizational.json",
         organizational
)

        repo.save_json(
        project_folder,
        "layout.json",
        layout
)

        repo.save_json(
         project_folder,
        "knowledge_graph.json",
        knowledge_graph
)



        print("\nPROJECT MASTER GENERADO")
        print(project_master)

        return {

        "idea": project_data,

        "diagnostic": diagnostic,

        "problem_tree": problem_tree,

        "objective_tree": objective_tree,

        "logical_framework": logical_framework,

        "market": market,

        "technical": technical,
       
        "project_master": project_master,

        "localization": localization,

        "size": size,

        "cash_flow": cash_flow,

        "investment": investment,

        "costs": costs,

        "revenue": revenue,

        "van":van,

        "workforce": workforce,
      
        "process":process,

        "organizational": organizational,

        "marketing":marketing,

        "tir": tir,

        "pri": pri,

        "bc": bc,

        "sensitivity": sensitivity,

        "montecarlo": montecarlo,

        "pca": pca,

        "clustering": clustering,

        "dashboard": dashboard,
        
        "layout": layout,

        "knowledge_graph": knowledge_graph
        
}
       