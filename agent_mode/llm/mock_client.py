from .base import LLMClient

class MockLLMClient(LLMClient):
    def query(self, prompt: str) -> str:
        return f"[Mocked Response]: {prompt[:50]}..."
