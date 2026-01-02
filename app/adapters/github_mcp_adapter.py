from .base_adapter import BaseAdapter

class GitHubMCPAdapter(BaseAdapter):
    def connect(self):
        self.connected = True
        return self.connected

    def fetch(self, query=None):
        # Simulate fetching version changes
        return {
            "repo": "fintech-infra",
            "commit_id": "abc123def",
            "author": "devops-bot",
            "message": "Update dbt pipeline config",
            "timestamp": "2026-01-02T08:00:00Z"
        }

    def transform(self, data):
        # Example: summarize commit message
        data["summary"] = data["message"][:30]
        return data

    def validate(self, data):
        # Example: check if commit message is present
        return bool(data.get("message"))
