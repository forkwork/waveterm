from .llm.ollama_client import OllamaClient
from .llm.mock_client import MockLLMClient

DEV_MODE = True  # 🔁 Toggle this to False for real model

if DEV_MODE:
    LLM_BACKEND = MockLLMClient(dev_mode=True)
else:
    LLM_BACKEND = OllamaClient(model="llama3", dev_mode=False)
