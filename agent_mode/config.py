"""
Configuration for LLM backend selection.

Switch between development and production LLM backends using the DEV_MODE toggle
or the DEV_MODE environment variable.
"""

import os
import logging
from typing import Union

from .llm.ollama_client import OllamaClient
from .llm.mock_client import MockLLMClient

logging.basicConfig(level=logging.INFO)

def get_llm_backend(dev_mode: bool) -> Union[MockLLMClient, OllamaClient]:
    """
    Factory to select and initialize the LLM backend.

    Args:
        dev_mode (bool): If True, use the mock backend. If False, use the real backend.

    Returns:
        An instance of the selected LLM client.
    """
    if dev_mode:
        logging.info("Using MockLLMClient (development mode).")
        return MockLLMClient(dev_mode=True)
    logging.info("Using OllamaClient (production mode, model=llama3).")
    return OllamaClient(model="llama3", dev_mode=False)

# Prefer environment variable for toggle; fallback to code default
DEV_MODE = os.getenv("DEV_MODE", "True").lower() in ("true", "1")
LLM_BACKEND = get_llm_backend(DEV_MODE)