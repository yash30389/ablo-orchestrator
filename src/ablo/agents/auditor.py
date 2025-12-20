from ablo.agents.base import BaseAgent

class Auditor(BaseAgent):
    MAX_DISCOUNT = 15

    def validate(self, plan: list):
        for node in plan:
            if node["action"] == "send_email":
                discount = node["payload"].get("discount", 0)
                if discount > self.MAX_DISCOUNT:
                    node["payload"]["discount"] = self.MAX_DISCOUNT
        return plan
