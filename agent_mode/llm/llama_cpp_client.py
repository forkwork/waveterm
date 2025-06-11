from llama_cpp import Llama
from .base import LLMClient

class LlamaCppClient(LLMClient):
    def __init__(self, model_path="models/llama-2.gguf"):
        self.llm = Llama(model_path=model_path)

    def query(self, prompt: str) -> str:
        output = self.llm(prompt, max_tokens=256)
        return output["choices"][0]["text"].strip()
