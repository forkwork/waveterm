class TaskStep:
    def __init__(self, command: str, explanation: str):
        self.command = command
        self.explanation = explanation

class TaskPlanner:
    def __init__(self, llm_client):
        self.llm = llm_client
        self.step_pattern = r"(\d+\.)?\s*(.+?)\s*\|\s*(.+)"
    
    def plan(self, prompt: str) -> list[TaskStep]:
        """Generate executable steps using LLM"""
        system_prompt = (
            "You are a command planning assistant. Break user requests into executable steps.\n"
            "Format each step as: command | explanation\n"
            "Example:\n"
            "git status | Check current branch status\n"
            "git add . | Stage all changes\n"
            "git commit -m 'message' | Commit changes\n\n"
            "Guidelines:\n"
            "1. Use concise but complete commands\n"
            "2. Provide clear justifications\n"
            "3. Include all necessary steps\n"
            "4. Use common CLI tools (bash, git, npm, etc)"
        )
        
        # Get LLM response
        response = self.llm.query(
            system_prompt=system_prompt,
            user_prompt=prompt,
            max_tokens=500
        )
        
        # Parse response into steps
        return self.parse_response(response)
    
    def parse_response(self, response: str) -> list[TaskStep]:
        """Parse LLM response into TaskStep objects"""
        steps = []
        for line in response.split('\n'):
            line = line.strip()
            if not line or line.startswith('#'):
                continue
                
            # Handle both numbered and unnumbered steps
            if '|' in line:
                parts = line.split('|', 1)
                command = parts[0].strip()
                explanation = parts[1].strip()
                
                # Remove numbering if present
                if command.split('.')[0].isdigit():
                    command = command.split('.', 1)[1].strip()
                
                steps.append(TaskStep(command, explanation))
        
        return steps