import subprocess
from waveterm.agent_mode.command_hooks import AgentCommandHooks
agent_hooks = AgentCommandHooks()

def run_shell_command(command):
    agent_hooks.before_command(command)
    
    output = subprocess.getoutput(command)
    
    agent_hooks.after_command(command, output)
    return output