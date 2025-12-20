from typing import Dict, Any
from uuid import uuid4
from datetime import datetime


class WorkflowState:
    def __init__(self):
        self.id = str(uuid4())
        self.created_at = datetime.utcnow()
        self.context: Dict[str, Any] = {}
        self.history = []

    def update(self, data: Dict[str, Any]):
        self.context.update(data)
        self.history.append(data)

    def snapshot(self):
        return {
            "id": self.id,
            "context": self.context,
            "history": self.history,
        }
