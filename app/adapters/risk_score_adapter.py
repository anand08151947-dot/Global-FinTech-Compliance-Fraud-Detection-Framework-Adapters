from .base_adapter import BaseAdapter

class RiskScoreAdapter(BaseAdapter):
    def connect(self):
        self.connected = True
        return self.connected

    def fetch(self, query=None):
        # Simulate risk scoring
        return {
            "entity_id": "C12345",
            "risk_score": 0.65,
            "category": "customer",
            "timestamp": "2026-01-02T15:50:00Z"
        }

    def transform(self, data):
        # Example: add risk label
        data["risk_label"] = "medium" if 0.4 < data["risk_score"] < 0.8 else "low"
        return data

    def validate(self, data):
        # Example: pass if not high risk
        return data["risk_label"] != "high"
