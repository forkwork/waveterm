class TaskExplainer:
    """Generates human-readable explanations for CLI commands"""
    
    def __init__(self, llm_client):
        self.llm = llm_client
    
    def explain(self, command: str) -> str:
        """
        Generate explanation for a CLI command
        
        Args:
            command: CLI command to explain
            
        Returns:
            Human-readable explanation of the command
        """
        # Simple commands dictionary for common operations
        command_explanations = {
            "git status": "Show the working tree status",
            "git add": "Add file contents to the index",
            "git commit": "Record changes to the repository",
            "git push": "Update remote references along with associated objects",
            "npm install": "Install package dependencies",
            "docker build": "Build an image from a Dockerfile",
            "ls": "List directory contents",
            "cd": "Change the working directory"
        }
        
        # Check if we have a simple explanation
        for cmd_prefix, explanation in command_explanations.items():
            if command.startswith(cmd_prefix):
                return explanation
        
        # For complex commands, use LLM
        return self.llm.query(
            system_prompt="Explain this CLI command in simple terms:",
            user_prompt=command,
            max_tokens=150
        )