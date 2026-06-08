class ToolRegistry:

    def __init__(self):

        self.tools = {

            # Account Opening
            "kyc_check": self.kyc_check,
            "create_account": self.create_account,
            "send_welcome_email": self.send_welcome_email,

            # Loan
            "loan_eligibility_check": self.loan_eligibility_check,
            "credit_check": self.credit_check,
            "risk_assessment": self.risk_assessment,
            "create_loan_application": self.create_loan_application,
            "approve_loan": self.approve_loan,

            # KYC
            "validate_documents": self.validate_documents,
            "update_kyc": self.update_kyc,
            "notify_customer": self.notify_customer,
        }

    def get(self, tool_name):
        return self.tools.get(tool_name)

    # ----------------------
    # ACCOUNT OPENING
    # ----------------------

    def kyc_check(self):
        return "KYC completed"

    def create_account(self):
        return "Account created"

    def send_welcome_email(self):
        return "Welcome email sent"

    # ----------------------
    # LOAN
    # ----------------------

    def loan_eligibility_check(self):
        return "Customer eligible for loan"

    def credit_check(self):
        return "Credit score = 742"

    def risk_assessment(self):
        return "Risk level = LOW"

    def create_loan_application(self):
        return "Loan application created"

    def approve_loan(self):
        return "Loan approved"

    # ----------------------
    # KYC
    # ----------------------

    def validate_documents(self):
        return "Documents validated"

    def update_kyc(self):
        return "KYC updated"

    def notify_customer(self):
        return "Customer notified"