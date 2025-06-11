import pytest
from unittest.mock import patch
from agent_mode.llm_client import get_llm_response

# Test cases
@patch('agent_mode.llm_client.query_llm')
def test_get_llm_response_success(mock_query):
    """Test successful LLM response"""
    mock_query.return_value = "Test response"
    result = get_llm_response("Test prompt")
    assert result == "Test response"

@patch('agent_mode.llm_client.query_llm')
def test_get_llm_response_failure(mock_query):
    """Test LLM connection failure"""
    mock_query.side_effect = Exception("Connection error")
    with pytest.raises(LLMConnectionError):
        get_llm_response("Test prompt")
