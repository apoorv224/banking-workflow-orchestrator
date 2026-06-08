class StateStore:
    def __init__(self):
        self.store = {}

    def save(self, workflow_id, state):
        self.store[workflow_id] = state

    def get(self, workflow_id):
        return self.store.get(workflow_id)

    def update_status(self, workflow_id, status):
        if workflow_id in self.store:
            self.store[workflow_id]["status"] = status


state_store = StateStore()