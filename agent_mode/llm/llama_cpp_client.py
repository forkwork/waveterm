from llama_cpp import Llama
from .base import LLMClient
import logging

logger = logging.getLogger(__name__)

class LlamaCppClient(LLMClient):
    """
    A client to interact with a Llama model using llama_cpp.
    """

    def __init__(self, model_path: str = "models/llama-2.gguf"):
        """
        Initialize the LlamaCppClient.

        Args:
            model_path (str): Path to the Llama model file.
        """
        try:
            self.llm = Llama(model_path=model_path)
        except Exception as e:
            logger.error(f"Could not initialize Llama model: {e}")
            raise RuntimeError(f"Initialization failed: {e}")

    def query(
        self, 
        prompt: str, 
        max_tokens: int = 256, 
        temperature: float = 0.7, 
        **kwargs
    ) -> str:
        """
        Query the Llama model with a prompt.

        Args:
            prompt (str): The input prompt for the model.
            max_tokens (int): Maximum number of tokens to generate.
            temperature (float): Sampling temperature.
            **kwargs: Additional parameters for Llama.

        Returns:
            str: The generated response.
        """
        if not isinstance(prompt, str) or not prompt.strip():
            raise ValueError("Prompt must be a non-empty string.")

        logger.info(f"Querying model with prompt: {prompt[:50]}...")

        try:
            output = self.llm(prompt, max_tokens=max_tokens, temperature=temperature, **kwargs)
            return output["choices"][0]["text"].strip()
        except Exception as e:
            logger.error(f"Query failed: {e}")
            raise RuntimeError(f"Query failed: {e}")