import subprocess

class CommandInterceptor:
    def __init__(self, agent_core):
        self.agent = agent_core

    def pre_exec(self, command: str):
        # Optional: Ask for confirmation or show LLM explanation
        print("💡 AI Suggestion:", self.agent.explain_command(command))

    def post_exec(self, command: str, output: str):
        if "error" in output.lower():
            print("🔁 AI Correction:", self.agent.suggest_corrections(command))

    def run_command(self, command: str):
        self.pre_exec(command)
        result = subprocess.getoutput(command)
        print(result)
        self.post_exec(command, result)
