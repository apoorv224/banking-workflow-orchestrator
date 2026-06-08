import json
from pathlib import Path

class WorkflowRegistry:
    """
    Loads and manages workflow definitions from /workflows
    """

    def __init__(self, base_path: str = "workflows"):
        self.base_path = Path(base_path)
        self._cache = {}

    def load_workflow(self, filename: str) -> dict:
        """
        Load a workflow JSON file
        """

        file_path = self.base_path / filename

        if not file_path.exists():
            return {
                "status": "ERROR",
                "reason": "WORKFLOW_FILE_NOT_FOUND"
            }

        with open(file_path, "r") as f:
            workflow = json.load(f)
            self._cache[filename] = workflow
            return workflow

    def get_workflow(self, name: str) -> dict:
        """
        Get workflow from cache or load if missing
        """

        if name in self._cache:
            return self._cache[name]

        return self.load_workflow(name)

    def list_workflows(self) -> list:
        """
        List available workflow files
        """

        return [f.name for f in self.base_path.glob("*.json")]