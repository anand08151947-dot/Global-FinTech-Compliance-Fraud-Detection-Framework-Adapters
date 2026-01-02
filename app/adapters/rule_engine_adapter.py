from .base_adapter import BaseAdapter

class RuleEngineAdapter(BaseAdapter):
    def connect(self):
        self.connected = True
        return self.connected

    def fetch(self, query=None):
        # Simulate rule evaluation
        return {
            "rule_id": "RULE-20260102-01",
            "triggered": True,
            "description": "High value transaction",
            "timestamp": "2026-01-02T15:40:00Z"
        }

    def transform(self, data):
        # Example: add rule status
        data["rule_status"] = "triggered" if data["triggered"] else "ok"
        return data

    def validate(self, data):
        # Example: pass if not triggered
        return not data["triggered"]
