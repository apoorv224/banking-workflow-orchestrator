import json
from app.agents.llm_client import LLMClient

class LLMToolPlanner:

    def __init__(self):
        self.llm = LLMClient()  # plug OpenAI later

    def plan(self, intent: dict, user_input: str):

        prompt = f"""
You are a banking workflow planner.

You MUST return ONLY valid JSON.
No explanation. No text.

Return format:
[
  {{"tool": "kyc_check"}},
  {{"tool": "create_account"}},
  {{"tool": "send_welcome_email"}}
]

Available tools:

ACCOUNT_OPENING:
- kyc_check
- create_account
- send_welcome_email

LOAN_APPLICATION:
- loan_eligibility_check
- credit_check
- risk_assessment
- create_loan_application
- approve_loan

KYC_UPDATE:
- validate_documents
- update_kyc
- notify_customer

Rules:
If account opening:
  kyc_check
  create_account
  send_welcome_email

If loan:
  loan_eligibility_check
  create_loan_application

If KYC update:
  update_kyc

If intent is ACCOUNT_OPENING return only account tools.

If intent is LOAN_APPLICATION return only loan tools.

If intent is KYC_UPDATE return only kyc tools.

Intent:
{json.dumps(intent)}

User input:
{user_input}
"""

        raw = self.llm.generate(prompt)
        return self.extract_json(raw)
    def extract_json(self, text: str):
        try:
            return json.loads(text)

        except Exception:

            text = text.strip()

            text = text.replace("```json", "")
            text = text.replace("```", "")

            try:
                return json.loads(text)

            except Exception:
                return []