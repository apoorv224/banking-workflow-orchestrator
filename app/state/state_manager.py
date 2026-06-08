from app.state.state_store import state_store

class StateManager:

    def create_workflow(self, workflow_id, intent):
        state_store.save(workflow_id, {
            "workflow_id": workflow_id,
            "status": "RUNNING",
            "intent": intent,
            "completed_steps": [],
            "pending_input": None,
            "pending_intent": None
        })

    def add_step(self, workflow_id, step):
        state = state_store.get(workflow_id)

        if state:
            state.setdefault("completed_steps", [])
            state["completed_steps"].append(step)
            state_store.save(workflow_id, state)

    def complete(self, workflow_id):
        state = state_store.get(workflow_id)
        if state:
            state["status"] = "COMPLETED"
            state_store.save(workflow_id, state)

    def get(self, workflow_id):
        return state_store.get(workflow_id)

    def get_workflow(self, workflow_id):
        return state_store.get(workflow_id)