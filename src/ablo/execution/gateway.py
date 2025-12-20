from ablo.execution.actions import ActionRegistry


class ExecutionGateway:
    def execute(self, step: dict):
        action = step["action"]
        payload = step.get("payload", {})

        if not ActionRegistry.is_allowed(action):
            raise PermissionError(f"Action not allowed: {action}")

        # Stubbed execution
        return {
            "action": action,
            "status": "executed",
            "result": "ok"
        }
