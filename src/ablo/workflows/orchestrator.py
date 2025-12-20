# src/ablo/workflows/orchestrator.py
from ablo.agents.planner import Planner
from ablo.agents.auditor import Auditor
import asyncio
from ablo.workflows.graph.manager import WorkflowGraph
from ablo.workflows.graph.utils.executor import async_executor

class Orchestrator:
    def __init__(self):
        self.planner = Planner()
        self.auditor = Auditor()

    def run(self, intent: str):
        plan = self.planner.generate_plan(intent)
        plan = self.auditor.validate(plan)

        graph = WorkflowGraph()
        for node in plan:
            graph.add_node(node["name"], node["action"], node.get("payload", {}))
        for i in range(len(plan) - 1):
            graph.add_edge(plan[i]["name"], plan[i + 1]["name"])

        results = asyncio.run(graph.run(async_executor))
        return results
