# agent_mode/explain_anything.py

import os
from agent_mode.llm_client import ask_llm

DEV_MODE = os.getenv("AGENT_MODE_DEV", "false").lower() == "true"

def explain_thing(thing: str, context: str = "") -> str:
    """
    Generate explanation for technical concept.
    
    Args:
        thing: Concept to explain
        context: Additional context for personalized explanation
    
    Returns:
        Detailed explanation in markdown format
    """
    if DEV_MODE:
        return f"[DEV] Would explain this: {thing}"

    prompt_map = {
        "command": f"Explain what this shell command does:\n\n{thing}",
        "code": f"Explain this code:\n\n{thing}",
        "output": f"Interpret and summarize this command output:\n\n{thing}",
        "auto": f"Can you explain this?\n\n{thing}",
    }

    prompt = prompt_map.get("auto", prompt_map["auto"])
    return ask_llm(prompt)
