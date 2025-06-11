def before_command(self, cmd: str):
    print(f"🤖 Explaining: {cmd}")
    try:
        explanation = self.agent.explain(cmd)
        print(explanation)
    except Exception as e:
        print(f"Error explaining command: {e}")

def after_command(self, cmd: str, output: str):
    if "not found" in output or "command not found" in output:
        print(f"🧠 Correction Suggestion: {cmd}")
        try:
            correction = self.agent.correct(cmd)
            print(correction)
        except Exception as e:
            print(f"Error correcting command: {e}")