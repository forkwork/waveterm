import pytest
from agent_mode.interface import code_tooling_menu

# Mock input functionality
class MockInput:
    def __init__(self, inputs):
        self.inputs = iter(inputs)
        
    def __call__(self, prompt=""):
        return next(self.inputs)

# Test cases
def test_code_tooling_menu_valid_choice(monkeypatch):
    """Test valid menu choices"""
    inputs = ["1", "ls", "python", "exit"]
    monkeypatch.setattr('builtins.input', MockInput(inputs))
    monkeypatch.setattr('builtins.print', lambda x: None)
    
    # Should execute without errors
    code_tooling_menu()

def test_code_tooling_menu_invalid_choice(monkeypatch, capsys):
    """Test invalid menu choice handling"""
    inputs = ["5", "exit"]
    monkeypatch.setattr('builtins.input', MockInput(inputs))
    
    code_tooling_menu()
    captured = capsys.readouterr()
    assert "Invalid choice" in captured.out

def test_code_tooling_menu_empty_input(monkeypatch, capsys):
    """Test empty input validation"""
    inputs = ["1", "", "exit"]
    monkeypatch.setattr('builtins.input', MockInput(inputs))
    
    code_tooling_menu()
    captured = capsys.readouterr()
    assert "cannot be empty" in captured.out
