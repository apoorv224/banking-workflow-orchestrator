import requests
import json
import re

class WorkflowPlannerAgent:

    def __init__(self):
        self.url = "http://localhost:11434/api/generate"
        self.model = "llama3.1"

    def plan(self, intent):

        prompt = f"""
Return ONLY ONE JSON OBJECT.

Intent:
{json.dumps(intent)}
"""

        response = requests.post(
            self.url,
            json={
                "model": self.model,
                "prompt": prompt,
                "stream": False
            }
        )

        text = response.json()["response"]

        match = re.search(r"\{.*\}", text, re.DOTALL)

        if match:
            try:
                return json.loads(match.group())
            except:
                pass

        return {
            "workflow": "UNKNOWN",
            "steps": []
        }