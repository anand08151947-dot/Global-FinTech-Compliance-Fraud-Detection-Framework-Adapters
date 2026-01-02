from .base_adapter import BaseAdapter

class GeoIPAdapter(BaseAdapter):
    def connect(self):
        self.connected = True
        return self.connected

    def fetch(self, query=None):
        # Simulate geolocation risk scoring
        return {
            "ip": "203.0.113.42",
            "country": "RU",
            "risk_score": 0.8,
            "timestamp": "2026-01-02T15:10:00Z"
        }

    def transform(self, data):
        # Example: add risk label
        data["risk_label"] = "high" if data["risk_score"] > 0.7 else "low"
        return data

    def validate(self, data):
        # Example: pass if risk is not high
        return data["risk_label"] != "high"
