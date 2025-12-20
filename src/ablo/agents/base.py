# src/ablo/agents/base.py

class BaseAgent:
    """
    Base class for all agents (Planner, Auditor, etc.)
    Provides shared utilities if needed.
    """

    def log(self, message: str):
        print(f"[{self.__class__.__name__}] {message}")
