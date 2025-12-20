from typing import Dict, Any


class ActionRegistry:
    ALLOWED_ACTIONS = {
        "send_email": {"max_discount": 10},
        "post_slack_message": {},
        "check_inventory": {},
    }

    @classmethod
    def is_allowed(cls, action_name: str) -> bool:
        return action_name in cls.ALLOWED_ACTIONS

    @classmethod
    def get_policy(cls, action_name: str) -> Dict[str, Any]:
        return cls.ALLOWED_ACTIONS.get(action_name, {})
