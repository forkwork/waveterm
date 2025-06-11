# agent_mode/code_tooling.py

import os
from agent_mode.llm_client import ask_llm

DEV_MODE = os.getenv("AGENT_MODE_DEV", "false").lower() == "true"

def convert_command(input_cmd: str, target: str = "python") -> str:
    """
    Convert shell command to code in desired target language (e.g., Python, JS).
    """
    if DEV_MODE:
        return f"[DEV] Would convert this command to {target}: {input_cmd}"

    prompt = f"""Convert the following shell command to {target} code:\n\n{input_cmd}"""
    return ask_llm(prompt)


def enhance_tool_usage(input_tool: str, task: str) -> str:
    """
    Tool-specific smart command help (e.g., git, docker, kubectl).
    """
    if DEV_MODE:
        return f"[DEV] Tool '{input_tool}', task: {task}"

    prompt = f"""Using the tool '{input_tool}', how would I: {task}?\nProvide the best practice commands and brief explanations."""
    return ask_llm(prompt)


def edit_code_in_place(code_snippet: str, instruction: str) -> str:
    """
    Ask LLM to modify code snippet per instruction.
    """
    if DEV_MODE:
        return f"[DEV] Modify code with instruction: {instruction}"

    prompt = f"""Here is some code:\n\n{code_snippet}\n\nPlease update it to: {instruction}"""
    return ask_llm(prompt)
