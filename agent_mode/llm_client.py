# agent_mode/llm_client.py

import subprocess

class LLMConnectionError(Exception):
    pass

def ask_llm(prompt: str) -> str:
    """
    Send prompt to local LLM using Ollama or llama.cpp
    """
    # Example: using Ollama
    process = subprocess.run(
        ["ollama", "run", "llama3"],
        input=prompt.encode(),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    if process.returncode != 0:
        return f"# Error from LLM: {process.stderr.decode()}"
    
    return process.stdout.decode()

def get_llm_response(prompt: str, model: str = "gpt-4") -> str:
    """Get response from LLM with error handling.
    
    Args:
        prompt: Complete prompt for LLM
        model: Model identifier
    
    Returns:
        LLM response text
    
    Raises:
        LLMConnectionError: On connection failures
    """
    try:
        return ask_llm(prompt)
    except Exception as e:
        raise LLMConnectionError(f"LLM request failed: {str(e)}")
