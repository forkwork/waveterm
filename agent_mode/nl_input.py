# agent_mode/nl_input.py

import os

DEV_MODE = os.getenv("AGENT_MODE_DEV", "false").lower() == "true"

# Mock examples (used when DEV_MODE=True)
MOCK_RESPONSES = {
    "what's taking up the most disk space?": "du -sh * | sort -hr | head",
    "show running docker containers": "docker ps",
    "git log but only show the last 5 commits in a table": "git log -n 5 --pretty=format:'%h | %an | %s'"
}

def translate_nl_to_command(prompt: str) -> str:
    """
    Translate natural language prompt into shell command.
    """
    if DEV_MODE:
        return MOCK_RESPONSES.get(prompt.lower(), "# TODO: Unknown command (dev mode)")

    # Real LLM integration
    from agent_mode.llm_client import query_llm

    prompt_template = f"""
Translate the following natural language instruction into a concise Unix shell command.

Instruction: {prompt}

Command:
"""
    return query_llm(prompt_template).strip()
