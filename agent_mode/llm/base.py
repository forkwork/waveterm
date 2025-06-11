from abc import ABC, abstractmethod

class LLMClient(ABC):
    def __init__(self, dev_mode: bool = False):
        self.dev_mode = dev_mode

    @abstractmethod
    def query(self, prompt: str) -> str:
        pass
