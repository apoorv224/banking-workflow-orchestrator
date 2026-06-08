from datetime import datetime

class AuditStore:
    def __init__(self):
        self.logs = []

    def add(self, event_type: str, data: dict):
        self.logs.append({
            "timestamp": datetime.utcnow().isoformat(),
            "event_type": event_type,
            "data": data
        })

    def get_all(self):
        return self.logs

    def get_by_workflow(self, workflow_id: str):
        return [
            log for log in self.logs
            if log["data"].get("workflow_id") == workflow_id
        ]


audit_store = AuditStore()