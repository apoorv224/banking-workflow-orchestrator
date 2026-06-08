import json
from datetime import datetime

class AuditLogger:

    def __init__(self):
        self.logs = []

    def log(self, event_type: str, data: dict):
        self.logs.append({
            "timestamp": datetime.utcnow().isoformat(),
            "event_type": event_type,
            "data": data
        })

    def get_logs(self):
        return self.logs