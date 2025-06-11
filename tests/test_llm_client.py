import pytest
from unittest.mock import patch
from agent_mode.llm_client import get_llm_response, LLMConnectionError

# Test cases
@patch('agent_mode.llm_client.ask_llm')
def test_get_llm_response_success(mock_ask_llm):
    """Test successful LLM response"""
    mock_ask_llm.return_value = "Test response"
    result = get_llm_response("Test prompt")
    assert result == "Test response"

@patch('agent_mode.llm_client.ask_llm')
def test_get_llm_response_failure(mock_ask_llm):
    """Test LLM connection failure"""
    mock_ask_llm.side_effect = Exception("Connection error")
    with pytest.raises(LLMConnectionError):
        get_llm_response("Test prompt")
