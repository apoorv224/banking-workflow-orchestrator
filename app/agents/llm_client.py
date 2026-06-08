import requests

class LLMClient:

    def __init__(self, model="llama3.1"):
        self.model = model
        self.url = "http://localhost:11434/api/generate"

    def generate(self, prompt: str):

        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False,
            "format": "json"
        }

        response = requests.post(self.url, json=payload)

        if response.status_code != 200:
            raise Exception(f"Ollama error: {response.text}")

        return response.json()["response"]