from .agent_core import AgentCore

class AgentCommandHooks:
    def __init__(self):
        self.agent = AgentCore()

    def before_command(self, cmd: str):
        print(f"🤖 Explaining: {cmd}")
        print(self.agent.explain(cmd))

    def after_command(self, cmd: str, output: str):
        if "not found" in output or "command not found" in output:
            print(f"🧠 Correction Suggestion: {cmd}")
            print(self.agent.correct(cmd))
