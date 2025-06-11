from typing import Optional

class CommandInterceptor:
    def __init__(self, agent_core):
        self.agent = agent_core

    def pre_exec(self, command: str) -> None:
        """Process before command execution."""
        suggestion = self.agent.explain_command(command)
        if suggestion:
            print("💡 AI Suggestion:", suggestion)

    def post_exec(self, command: str, output: str) -> None:
        """Process after command execution."""
        if "error" in output.lower():
            correction = self.agent.suggest_corrections(command)
            if correction:
                print("🔁 AI Correction:", correction)

    def run_command(self, command: str) -> Optional[str]:
        """Run a command with pre/post processing."""
        self.pre_exec(command)
        try:
            process = subprocess.run(command, shell=True, capture_output=True, text=True)
            result = process.stdout if process.returncode == 0 else process.stderr
            print(result)
            self.post_exec(command, result)
            return result
        except Exception as e:
            print(f"Execution failed: {e}")
            return None