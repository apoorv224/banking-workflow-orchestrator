class PolicyStore:
    """
    In-memory policy version store (Phase 5 skeleton)
    """

    def __init__(self):
        self._store = {}

    def save_policy(self, name: str, version: str, policy: dict):
        """
        Save a policy version
        """

        if name not in self._store:
            self._store[name] = {}

        self._store[name][version] = policy

    def get_policy(self, name: str, version: str):
        """
        Retrieve a specific policy version
        """

        return self._store.get(name, {}).get(version, None)

    def list_versions(self, name: str):
        """
        List all versions of a policy
        """

        return list(self._store.get(name, {}).keys())