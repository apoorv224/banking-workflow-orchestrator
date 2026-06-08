from app.workflow.step_executor import StepExecutor

class WorkflowEngine:

    def __init__(self):
        self.executor = StepExecutor()

    def run(self, workflow: dict):

        results = []

        for step in workflow.get("steps", []):

            result = self.executor.execute(step)
            results.append(result)

            # IMPORTANT: continue even if failure happens
            # (no crash, no stop)

        return {
            "status": "COMPLETED",
            "steps": results
        }