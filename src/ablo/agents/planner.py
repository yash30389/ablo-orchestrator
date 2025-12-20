from typing import Dict, Any
from ablo.agents.base import BaseAgent
from ablo.agents.auditor import Auditor

class Planner(BaseAgent):
    def generate_plan(self, intent: str):
        if "customer complaint" in intent.lower():
            return [
                {"name": "check_inventory", "action": "check_inventory", "payload": {}},
                {"name": "send_discount_email", "action": "send_email", "payload": {"discount": 10}},
            ]
        return []
