class ApprovalStore:

    def __init__(self):
        self.requests = {}

    def create(self, workflow_id):
        self.requests[workflow_id] = "PENDING"

    def approve(self, workflow_id):
        self.requests[workflow_id] = "APPROVED"

    def get(self, workflow_id):
        return self.requests.get(workflow_id)


approval_store = ApprovalStore()