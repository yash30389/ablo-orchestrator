from ablo.execution.gateway import ExecutionGateway
from ablo.workflows.human import HumanApproval

# Shared instances
executor = ExecutionGateway()
human = HumanApproval()

async def async_executor(action, payload):
    """
    Async wrapper for WorkflowGraph node execution.
    Handles human approval if required.
    """
    if payload.get("requires_approval"):
        approved = human.request_approval({"action": action, "payload": payload})
        if not approved:
            return {"status": "skipped"}

    # Execute action in sandboxed gateway
    return executor.execute({"action": action, "payload": payload})
