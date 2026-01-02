from .base_adapter import BaseAdapter

class RegChangeAdapter(BaseAdapter):
    def connect(self):
        self.connected = True
        return self.connected

    def fetch(self, query=None):
        # Simulate regulatory change monitoring
        return {
            "change_id": "REG-20260102-01",
            "regulation": "AML",
            "impact": "medium",
            "timestamp": "2026-01-02T16:25:00Z"
        }

    def transform(self, data):
        # Example: add impact label
        data["impact_label"] = data["impact"].capitalize()
        return data

    def validate(self, data):
        # Example: pass if not high impact
        return data["impact"] != "high"
