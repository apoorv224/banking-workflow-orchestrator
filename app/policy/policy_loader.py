import json
from pathlib import Path

class PolicyLoader:
    """
    Loads policy JSON files from /policies directory
    """

    def __init__(self, base_path: str = "policies"):
        self.base_path = Path(base_path)

    def load_policy(self, filename: str) -> dict:
        """
        Load a single policy JSON file
        """

        file_path = self.base_path / filename

        if not file_path.exists():
            return {
                "status": "ERROR",
                "reason": "POLICY_FILE_NOT_FOUND"
            }

        with open(file_path, "r") as f:
            return json.load(f)

    def list_policies(self) -> list:
        """
        List all available policy files
        """
        return [f.name for f in self.base_path.glob("*.json")]