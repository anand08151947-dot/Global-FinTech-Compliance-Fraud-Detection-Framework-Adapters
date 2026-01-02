from .base_adapter import BaseAdapter

class IAMAdapter(BaseAdapter):
    def connect(self):
        self.connected = True
        return self.connected

    def fetch(self, query=None):
        # Simulate IAM user access review
        return {
            "user_id": "user_123",
            "roles": ["analyst", "viewer"],
            "last_access": "2026-01-01T10:00:00Z",
            "active": True
        }

    def transform(self, data):
        # Example: add compliance check
        data["compliance_check"] = "passed" if "analyst" in data["roles"] else "review"
        return data

    def validate(self, data):
        # Example: ensure user is active
        return data["active"]
