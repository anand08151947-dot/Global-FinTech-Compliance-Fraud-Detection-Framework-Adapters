from .base_adapter import BaseAdapter

class SanctionsListAdapter(BaseAdapter):
    def connect(self):
        self.connected = True
        return self.connected

    def fetch(self, query=None):
        # Simulate sanctions list screening
        return {
            "customer_id": "C12345",
            "on_list": False,
            "list_type": "OFAC",
            "timestamp": "2026-01-02T14:25:00Z"
        }

    def transform(self, data):
        # Example: add screening result
        data["screening_result"] = "clear" if not data["on_list"] else "flagged"
        return data

    def validate(self, data):
        # Example: pass if not on list
        return not data["on_list"]
