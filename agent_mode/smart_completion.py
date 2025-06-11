# agent_mode/smart_completion.py

import os

DEV_MODE = os.getenv("AGENT_MODE_DEV", "false").lower() == "true"

SNIPPET_LIBRARY = {
    "create_venv": "python3 -m venv venv && source venv/bin/activate",
    "docker_cleanup": "docker system prune -a",
    "git_log_table": "git log -n 5 --pretty=format:'%h | %an | %s'",
}

ALIASES = {
    "venv": "create_venv",
    "clean_docker": "docker_cleanup",
    "log_table": "git_log_table",
}

def get_snippet_by_alias(user_input: str) -> str:
    key = user_input.strip().lower()

    if key in SNIPPET_LIBRARY:
        return SNIPPET_LIBRARY[key]
    
    if key in ALIASES:
        snippet_key = ALIASES[key]
        return SNIPPET_LIBRARY.get(snippet_key, "# Unknown alias")

    return "# No snippet found"


def suggest_completion(partial_command: str) -> str:
    """
    Suggest command or snippet completions based on partial input.
    """
    matches = [cmd for cmd in SNIPPET_LIBRARY if cmd.startswith(partial_command)]
    if not matches:
        return "# No suggestion"
    return "\n".join([f"{m} → {SNIPPET_LIBRARY[m]}" for m in matches])
