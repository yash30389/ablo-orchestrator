TENANTS = {
    "tenant1": {"users": {"alice": "admin", "bob": "user"}},
    "tenant2": {"users": {"carol": "manager"}}
}

class AuthManager:
    def get_user_role(self, tenant_id, username):
        return TENANTS.get(tenant_id, {}).get("users", {}).get(username, None)

    def check_permission(self, tenant_id, username, action):
        role = self.get_user_role(tenant_id, username)
        if role == "admin":
            return True
        if role == "manager" and action != "dangerous":
            return True
        return False
