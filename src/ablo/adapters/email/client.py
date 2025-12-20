class EmailClient:
    def send(self, to: str, subject: str, body: str):
        return {
            "to": to,
            "subject": subject,
            "status": "sent"
        }
