# agent_mode/smart_completion.py

import os
from typing import List

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

class SnippetNotFoundError(Exception):
    pass

def get_snippet_by_alias(alias: str) -> str:
    """Retrieve code snippet by alias name.
    
    Args:
        alias: Snippet identifier
    
    Returns:
        Code snippet content
    
    Raises:
        SnippetNotFoundError: If alias doesn't exist
    """
    key = alias.strip().lower()

    if key in SNIPPET_LIBRARY:
        return SNIPPET_LIBRARY[key]
    
    if key in ALIASES:
        snippet_key = ALIASES[key]
        if snippet_key not in SNIPPET_LIBRARY:
            raise SnippetNotFoundError(f"Alias '{alias}' not found")
        return SNIPPET_LIBRARY[snippet_key]

    raise SnippetNotFoundError(f"Alias '{alias}' not found")


def suggest_completion(partial_code: str, context: str = "") -> List[str]:
    """Suggest code completions based on partial input.
    
    Args:
        partial_code: Incomplete code snippet
        context: Additional context for better suggestions
    
    Returns:
        List of completion suggestions
    """
    matches = [cmd for cmd in SNIPPET_LIBRARY if cmd.startswith(partial_code)]
    if not matches:
        return []
    return [f"{m} → {SNIPPET_LIBRARY[m]}" for m in matches]
