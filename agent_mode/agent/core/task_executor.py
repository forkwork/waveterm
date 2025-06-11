import subprocess

class TaskExecutor:
    """Executes task steps with interactive confirmation and output handling"""
    
    def __init__(self, interactive=True):
        self.interactive = interactive
        self.history = []
    
    def run_step(self, step):
        """
        Execute a single task step with confirmation
        
        Args:
            step: TaskStep object to execute
        """
        print(f"\n🔹 Command: {step.command}")
        print(f"📘 Explanation: {step.explanation}")
        
        # Interactive confirmation
        if self.interactive:
            confirm = input("✅ Run this step? (y/n): ")
            if confirm.strip().lower() != "y":
                print("⏩ Skipped.")
                return
        
        # Execute command
        try:
            result = subprocess.run(
                step.command, 
                shell=True, 
                capture_output=True, 
                text=True,
                check=False
            )
            
            # Record execution
            self.history.append({
                'step': step,
                'result': result,
                'success': result.returncode == 0
            })
            
            # Handle output
            if result.stdout:
                print(f"📤 Output:\n{result.stdout}")
            if result.stderr:
                print(f"⚠️ Errors:\n{result.stderr}")
            if result.returncode != 0:
                print(f"❌ Command failed with exit code {result.returncode}")
        except Exception as e:
            print(f"🔥 Execution error: {str(e)}")
            self.history.append({
                'step': step,
                'error': str(e),
                'success': False
            })