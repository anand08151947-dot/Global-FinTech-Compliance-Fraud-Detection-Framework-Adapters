from .base_adapter import BaseAdapter

class FastAPIServingAdapter(BaseAdapter):
    def connect(self):
        self.connected = True
        return self.connected

    def fetch(self, query=None):
        # Simulate serving a lightweight fraud detection model
        return {
            "model": "fraud_detector_v1",
            "input": {"amount": 1000, "country": "US"},
            "prediction": "not_fraud",
            "confidence": 0.98
        }

    def transform(self, data):
        # Example: add explanation
        data["explanation"] = "Low risk transaction."
        return data

    def validate(self, data):
        # Example: check prediction confidence
        return data.get("confidence", 0) > 0.9
