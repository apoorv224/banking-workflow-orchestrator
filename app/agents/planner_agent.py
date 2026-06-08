import requests
import json
import re

class PlannerAgent:

    def __init__(self):
        self.url = "http://localhost:11434/api/generate"
        self.model = "llama3"

    def plan(self, intent: dict):

        prompt = f"""
You are a workflow planner.

Return ONLY valid JSON:

{{
  "type": "ACCOUNT_OPENING_WORKFLOW",
  "steps": [
    {{"name": "kyc_check"}},
    {{"name": "create_account"}},
    {{"name": "send_welcome_email"}}
  ]
}}

Rules:
- ONLY JSON
- NO explanation
- NO markdown

Intent:
{intent}
"""

        res = requests.post(self.url, json={
            "model": self.model,
            "prompt": prompt,
            "stream": False
        })

        text = res.json().get("response", "")

        match = re.search(r"\{.*\}", text, re.DOTALL)

        if match:
            try:
                return json.loads(match.group())
            except:
                pass

        # HARD fallback (full workflow, not partial)
        return {
            "type": "ACCOUNT_OPENING_WORKFLOW",
            "steps": [
                {"name": "kyc_check"},
                {"name": "create_account"},
                {"name": "send_welcome_email"}
            ]
        }