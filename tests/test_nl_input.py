import pytest
from agent_mode.nl_input import parse_natural_language_input

# Test cases
def test_parse_nl_input_valid():
    """Test valid natural language input"""
    result = parse_natural_language_input("show me recent git commits")
    assert isinstance(result, dict)

def test_parse_nl_input_empty():
    """Test empty input validation"""
    with pytest.raises(ValueError):
        parse_natural_language_input("")
