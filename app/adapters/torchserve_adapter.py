from .base_adapter import BaseAdapter

class TorchServeAdapter(BaseAdapter):
    def connect(self):
        self.connected = True
        return self.connected

    def fetch(self, query=None):
        # Simulate TorchServe heavy-duty inference
        return {
            "model": "fraud_detector_torch",
            "input": {"amount": 5000, "country": "IN"},
            "prediction": "fraud",
            "confidence": 0.92
        }

    def transform(self, data):
        # Example: add model latency
        data["latency_ms"] = 120
        return data

    def validate(self, data):
        # Example: check for high-confidence fraud
        return data.get("prediction") == "fraud" and data.get("confidence", 0) > 0.9
