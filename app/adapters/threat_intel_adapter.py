from .base_adapter import BaseAdapter

class ThreatIntelAdapter(BaseAdapter):
    def connect(self):
        self.connected = True
        return self.connected

    def fetch(self, query=None):
        # Simulate threat intelligence feed
        return {
            "threat_id": "TI-20260102-01",
            "type": "phishing",
            "severity": "medium",
            "indicator": "malicious-domain.com",
            "timestamp": "2026-01-02T15:00:00Z"
        }

    def transform(self, data):
        # Example: add threat status
        data["threat_status"] = "investigate" if data["severity"] != "low" else "ignore"
        return data

    def validate(self, data):
        # Example: alert if severity is high
        return data["severity"] != "high"
