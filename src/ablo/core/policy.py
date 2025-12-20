class PolicyEngine:
    MAX_DISCOUNT_PERCENT = 10

    @classmethod
    def validate_discount(cls, discount: int):
        if discount > cls.MAX_DISCOUNT_PERCENT:
            raise PermissionError(
                f"Discount {discount}% exceeds max allowed {cls.MAX_DISCOUNT_PERCENT}%"
            )

    @classmethod
    def validate_action(cls, action: str):
        forbidden = {"wire_transfer", "delete_database"}
        if action in forbidden:
            raise PermissionError(f"Forbidden action: {action}")
