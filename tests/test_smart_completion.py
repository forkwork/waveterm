import pytest
from agent_mode.smart_completion import get_snippet_by_alias, SnippetNotFoundError

# Test cases
SNIPPET_LIBRARY = {"gitlog": "git log --oneline"}
ALIASES = {"gl": "gitlog"}

def test_get_snippet_valid_alias():
    """Test fetching snippet by valid alias"""
    result = get_snippet_by_alias("gitlog")
    assert "git log" in result

def test_get_snippet_invalid_alias():
    """Test handling of invalid alias"""
    with pytest.raises(SnippetNotFoundError):
        get_snippet_by_alias("invalid_alias")
