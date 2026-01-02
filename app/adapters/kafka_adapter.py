from .base_adapter import BaseAdapter

class KafkaAdapter(BaseAdapter):
    def connect(self):
        self.connected = True
        return self.connected

    def fetch(self, query=None):
        # Simulate Kafka event
        return {
            "topic": "fraud_alerts",
            "message": "High risk transaction detected",
            "partition": 0,
            "offset": 12345,
            "timestamp": "2026-01-02T14:20:00Z"
        }

    def transform(self, data):
        # Example: add message key
        data["key"] = "txn_98765"
        return data

    def validate(self, data):
        # Example: check if message is present
        return bool(data["message"])
