from agent.core.task_planner import TaskPlanner
from agent.core.task_explainer import TaskExplainer
from agent.core.task_executor import TaskExecutor
from .config import LLM_BACKEND

class AgentCore:
    """
    Core agent class for handling session responses and multi-step task execution.
    """

    def session_response(self, prompt: str) -> str:
        """
        Generate a response from the session using the provided prompt.

        Args:
            prompt (str): The user input prompt.

        Returns:
            str: The generated response.
        """
        full_prompt = self.session.build_context(prompt)
        response = LLM_BACKEND.query(full_prompt)
        self.session.update(prompt, response)
        return response

    def run_multistep(self, user_prompt: str):
        """
        Execute a multi-step task from a natural language prompt.

        Args:
            user_prompt (str): Natural language description of the task.
        """
        planner = TaskPlanner(llm_client=self.llm)
        executor = TaskExecutor(interactive=True)

        try:
            steps = planner.plan(user_prompt)
            print(f"📋 Generated {len(steps)} steps for: {user_prompt}")

            for step in steps:
                executor.run_step(step)

            print("✅ Task execution completed")
        except RuntimeError as e:
            print(f"❌ Task planning failed: {str(e)}")
        except Exception as e:
            print(f"⚠️ Unexpected error during multi-step execution: {str(e)}")
