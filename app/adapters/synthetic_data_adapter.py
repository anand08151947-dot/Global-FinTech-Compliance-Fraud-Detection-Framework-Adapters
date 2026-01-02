from .base_adapter import BaseAdapter

class SyntheticDataAdapter(BaseAdapter):
    def connect(self):
        self.connected = True
        return self.connected

    def fetch(self, query=None):
        # Simulate synthetic data generation
        return {
            "batch_id": "SYN-20260102-01",
            "rows": 1000,
            "fields": ["amount", "country", "device"],
            "timestamp": "2026-01-02T16:20:00Z"
        }

    def transform(self, data):
        # Example: add field count
        data["field_count"] = len(data["fields"])
        return data

    def validate(self, data):
        # Example: pass if rows > 0
        return data["rows"] > 0
