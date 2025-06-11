# agent_mode/code_tooling.py

import os
from agent_mode.llm_client import ask_llm

DEV_MODE = os.getenv("AGENT_MODE_DEV", "false").lower() == "true"

def convert_command(cmd: str, target_lang: str = "python") -> str:
    """
    Convert shell command to target programming language.
    
    Args:
        cmd: Shell command string
        target_lang: Target programming language
    
    Returns:
        Converted code snippet
    """
    if DEV_MODE:
        return f"[DEV] Would convert this command to {target_lang}: {cmd}"

    prompt = f"""Convert the following shell command to {target_lang} code:\n\n{cmd}"""
    return ask_llm(prompt)


def enhance_tool_usage(tool: str, task_desc: str) -> str:
    """
    Generate tool-specific command with best practices.
    
    Args:
        tool: CLI tool name (git, docker, etc.)
        task_desc: Description of task to accomplish
    
    Returns:
        Formatted command with explanations
    """
    if DEV_MODE:
        return f"[DEV] Tool '{tool}', task: {task_desc}"

    prompt = f"""Using the tool '{tool}', how would I: {task_desc}?\nProvide the best practice commands and brief explanations."""
    return ask_llm(prompt)


def edit_code_in_place(code: str, instruction: str) -> str:
    """
    Edit code based on natural language instruction.
    
    Args:
        code: Original code snippet
        instruction: Edit instructions in natural language
    
    Returns:
        Modified code based on instructions
    """
    if DEV_MODE:
        return f"[DEV] Modify code with instruction: {instruction}"

    prompt = f"""Here is some code:\n\n{code}\n\nPlease update it to: {instruction}"""
    return ask_llm(prompt)
