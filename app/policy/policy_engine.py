class PolicyEngine:

    def evaluate(self, intent: dict):

        intent_type = intent.get("type")

        if intent_type == "ACCOUNT_OPENING":
            return {
                "allowed": True,
                "reason": "Account opening allowed"
            }

        if intent_type == "LOAN_APPLICATION":
            return {
                "allowed": True,
                "reason": "Loan application allowed"
            }

        if intent_type == "KYC_UPDATE":
            return {
                "allowed": True,
                "reason": "KYC update allowed"
            }

        return {
            "allowed": False,
            "reason": "Unknown or blocked intent"
        }