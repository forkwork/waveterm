import pytest
from unittest.mock import MagicMock
from agent_mode.explain_anything import explain_thing

# Test cases
def test_explain_thing_dev_mode(monkeypatch):
    """Test dev mode functionality"""
    monkeypatch.setenv("AGENT_MODE_DEV", "true")
    mock_ask_llm = MagicMock(return_value="[DEV] Explanation for: git status")
    monkeypatch.setattr('agent_mode.explain_anything.ask_llm', mock_ask_llm)
    result = explain_thing("git status")
    assert "[DEV]" in result

def test_explain_thing_prod_mode(monkeypatch):
    """Test production mode functionality"""
    monkeypatch.setenv("AGENT_MODE_DEV", "false")
    mock_ask_llm = MagicMock(return_value="Explanation for: git status")
    monkeypatch.setattr('agent_mode.explain_anything.ask_llm', mock_ask_llm)
    result = explain_thing("git status")
    assert "Explanation for:" in result
