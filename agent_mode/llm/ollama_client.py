import requests
from .base import LLMClient

class OllamaClient(LLMClient):
    def __init__(self, model="llama3"):
        self.model = model
        self.api_url = "http://localhost:11434/api/generate"

    def query(self, prompt: str) -> str:
        response = requests.post(self.api_url, json={
            "model": self.model,
            "prompt": prompt,
            "stream": False
        })
        response.raise_for_status()
        return response.json()["response"].strip()
