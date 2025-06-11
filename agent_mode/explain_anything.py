# agent_mode/explain_anything.py

import os
from agent_mode.llm_client import ask_llm

DEV_MODE = os.getenv("AGENT_MODE_DEV", "false").lower() == "true"

def explain_thing(input_text: str, type_hint: str = "auto") -> str:
    """
    Explain shell command, code, or output.
    Type hint: 'command', 'code', 'output', or 'auto'
    """
    if DEV_MODE:
        return f"[DEV] Would explain this ({type_hint}): {input_text}"

    prompt_map = {
        "command": f"Explain what this shell command does:\n\n{input_text}",
        "code": f"Explain this code:\n\n{input_text}",
        "output": f"Interpret and summarize this command output:\n\n{input_text}",
        "auto": f"Can you explain this?\n\n{input_text}",
    }

    prompt = prompt_map.get(type_hint, prompt_map["auto"])
    return ask_llm(prompt)
