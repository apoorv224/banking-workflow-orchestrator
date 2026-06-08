import random

class StepExecutor:

    def execute(self, step: dict):

        name = step.get("name")

        # simulate occasional failure (for realism)
        fail_chance = random.random()

        if fail_chance < 0.1:
            return {
                "step": name,
                "status": "FAILED",
                "result": f"{name} failed due to system error"
            }

        if name == "kyc_check":
            return {
                "step": name,
                "status": "SUCCESS",
                "result": "KYC completed"
            }

        if name == "create_account":
            return {
                "step": name,
                "status": "SUCCESS",
                "result": "Account created"
            }

        if name == "send_welcome_email":
            return {
                "step": name,
                "status": "SUCCESS",
                "result": "Email sent"
            }

        return {
            "step": name,
            "status": "UNKNOWN",
            "result": "Step not recognized"
        }