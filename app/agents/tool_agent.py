class ToolAgent:

    def plan(self, intent: dict):

        intent_type = intent.get("type")

        if intent_type == "ACCOUNT_OPENING":
            return ["kyc_check", "create_account", "send_welcome_email"]

        if intent_type == "LOAN_APPLICATION":
            return ["loan_eligibility_check", "create_loan_application"]

        if intent_type == "KYC_UPDATE":
            return ["update_kyc"]

        return []