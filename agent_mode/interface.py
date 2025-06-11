from agent_mode.smart_completion import get_snippet_by_alias, suggest_completion
from agent_mode.explain_anything import explain_thing
from agent_mode.code_tooling import convert_command, enhance_tool_usage, edit_code_in_place  # New import

# ... existing functions ...

# New code tooling menu
def code_tooling_menu():
    """Interactive menu for code-related tools"""
    print("\n🛠 Tooling Menu")
    print("1. Convert shell command to code")
    print("2. Tool-specific help (git, docker, etc.)")
    print("3. Edit code with instruction")
    
    choice = input("Choose [1-3]: ")

    if choice == "1":
        cmd = input("Shell command to convert:\n> ")
        target = input("Target language (default: python): ") or "python"
        print(convert_command(cmd, target))

    elif choice == "2":
        tool = input("Tool (e.g. git, docker): ")
        task = input("What do you want to do?\n> ")
        print(enhance_tool_usage(tool, task))

    elif choice == "3":
        code = input("Paste code snippet:\n> ")
        instr = input("What should be changed?\n> ")
        print(edit_code_in_place(code, instr))