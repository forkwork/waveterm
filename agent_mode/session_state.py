class SessionState:
    def __init__(self):
        self.history = []

    def build_context(self, prompt: str):
        history = "\n".join([f"User: {u}\nAgent: {a}" for u, a in self.history[-5:]])
        return f"{history}\nUser: {prompt}"

    def update(self, prompt: str, response: str):
        self.history.append((prompt, response))
