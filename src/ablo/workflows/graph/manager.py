import networkx as nx
import asyncio
from typing import Dict, Any


class WorkflowGraph:
    def __init__(self):
        self.graph = nx.DiGraph()
        self.node_results: Dict[str, Any] = {}

    def add_node(self, name: str, action: str, payload: Dict[str, Any] = None):
        self.graph.add_node(name, action=action, payload=payload or {})

    def add_edge(self, from_node: str, to_node: str):
        self.graph.add_edge(from_node, to_node)

    async def execute_node(self, node_name: str, executor):
        node = self.graph.nodes[node_name]
        result = await executor(node["action"], node["payload"])
        self.node_results[node_name] = result
        return result

    async def run(self, executor):
        """Runs all nodes respecting dependencies"""
        visited = set()

        async def visit(node):
            if node in visited:
                return
            for pred in self.graph.predecessors(node):
                await visit(pred)
            await self.execute_node(node, executor)
            visited.add(node)

        for node in self.graph.nodes:
            await visit(node)
        return self.node_results
