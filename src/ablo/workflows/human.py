class HumanApproval:
    def request_approval(self, action_node):
        """
        Sends a notification to human and waits for approval.
        For demo, we just auto-approve
        """
        print(f"Requesting approval for: {action_node}")
        # Here you could integrate Slack/email notification
        return True  # auto-approve for now
