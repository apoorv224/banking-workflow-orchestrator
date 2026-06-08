import requests
import json
import re

class IntentAgent:

    def __init__(self):
        self.url = "http://localhost:11434/api/generate"
        self.model = "llama3.1"

    def detect(self, user_input: str):

        prompt = f"""
You are a banking intent classifier.

Choose ONLY ONE intent:

ACCOUNT_OPENING
LOAN_APPLICATION
KYC_UPDATE

Return ONLY JSON.

Examples:

User: open account
{{"type":"ACCOUNT_OPENING","confidence":0.95}}

User: apply for loan
{{"type":"LOAN_APPLICATION","confidence":0.95}}

User: update kyc
{{"type":"KYC_UPDATE","confidence":0.95}}

User: {user_input}
"""

        res = requests.post(
            self.url,
            json={
                "model": self.model,
                "prompt": prompt,
                "stream": False
            }
        )

        text = res.json().get("response", "")
        print("RAW LLM RESPONSE =", text)
        matches = re.findall(r"\{[^{}]*\}", text)
        if matches:
            try:
                return json.loads(matches[-1])
            except Exception as e:
                print("JSON ERROR =", e)

        if matches:
            try:
                result = json.loads(matches[-1])
                print("PARSED INTENT =", result)
                return result
            except Exception as e:
                print("JSON ERROR =", e)

        return {
            "type": "UNKNOWN",
            "confidence": 0.0
        }