import pytest
from agent_mode.explain_anything import explain_thing

# Test cases
def test_explain_thing_dev_mode(monkeypatch):
    """Test dev mode functionality"""
    monkeypatch.setenv("AGENT_MODE_DEV", "true")
    result = explain_thing("git status")
    assert "[DEV]" in result

def test_explain_thing_prod_mode(monkeypatch):
    """Test production mode functionality"""
    monkeypatch.setenv("AGENT_MODE_DEV", "false")
    monkeypatch.setattr('agent_mode.explain_anything.ask_llm', 
                       lambda x: f"Explanation for: {x}")
    result = explain_thing("git status")
    assert "Explanation for:" in result
