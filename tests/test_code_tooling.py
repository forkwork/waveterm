import pytest
from agent_mode.code_tooling import convert_command

# Mock LLM call
def mock_ask_llm(prompt):
    return f"Mock response for: {prompt}"

# Test cases
def test_convert_command_dev_mode(monkeypatch):
    """Test dev mode functionality"""
    monkeypatch.setenv("AGENT_MODE_DEV", "true")
    monkeypatch.setattr('agent_mode.code_tooling.ask_llm', mock_ask_llm)
    result = convert_command("ls -l", "python")
    assert "[DEV]" in result

def test_convert_command_prod_mode(monkeypatch):
    """Test production mode functionality"""
    monkeypatch.setenv("AGENT_MODE_DEV", "false")
    monkeypatch.setattr('agent_mode.code_tooling.ask_llm', mock_ask_llm)
    result = convert_command("ls -l", "python")
    assert "Mock response for:" in result
