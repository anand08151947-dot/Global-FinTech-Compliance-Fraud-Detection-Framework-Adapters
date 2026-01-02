from .base_adapter import BaseAdapter

class DeviceFingerprintAdapter(BaseAdapter):
    def connect(self):
        self.connected = True
        return self.connected

    def fetch(self, query=None):
        # Simulate device fingerprinting
        return {
            "device_id": "dev-001",
            "user_id": "user_123",
            "anomaly": False,
            "location": "US",
            "timestamp": "2026-01-02T15:05:00Z"
        }

    def transform(self, data):
        # Example: add anomaly status
        data["anomaly_status"] = "ok" if not data["anomaly"] else "alert"
        return data

    def validate(self, data):
        # Example: pass if no anomaly
        return not data["anomaly"]
