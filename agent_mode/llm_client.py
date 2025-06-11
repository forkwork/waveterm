# agent_mode/llm_client.py

import subprocess

def query_llm(prompt: str) -> str:
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
