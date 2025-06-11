from agent_mode.smart_completion import get_snippet_by_alias, suggest_completion
from agent_mode.explain_anything import explain_thing
from agent_mode.code_tooling import convert_command, enhance_tool_usage, edit_code_in_place  # New import

# ... existing functions ...

# New code tooling menu
def code_tooling_menu() -> None:
    """Interactive menu for code-related tools with error handling and validation.
    
    Provides options to:
    1. Convert shell commands to code
    2. Get tool-specific help
    3. Edit code with instructions
    """
    print("\n🛠 Tooling Menu")
    print("1. Convert shell command to code")
    print("2. Tool-specific help (git, docker, etc.)")
    print("3. Edit code with instruction")
    
    try:
        choice = input("Choose [1-3]: ")
        
        # Validate choice
        if choice not in ["1", "2", "3"]:
            print("⚠️ Invalid choice. Please select 1, 2, or 3.")
            return
            
        if choice == "1":
            cmd = input("Shell command to convert:\n> ")
            if not cmd.strip():
                print("⚠️ Command cannot be empty")
                return
                
            target = input("Target language (default: python): ") or "python"
            print(convert_command(cmd, target))
            
        elif choice == "2":
            tool = input("Tool (e.g. git, docker): ")
            if not tool.strip():
                print("⚠️ Tool name cannot be empty")
                return
                
            task = input("What do you want to do?\n> ")
            print(enhance_tool_usage(tool, task))
            
        elif choice == "3":
            code = input("Paste code snippet:\n> ")
            if not code.strip():
                print("⚠️ Code snippet cannot be empty")
                return
                
            instr = input("What should be changed?\n> ")
            print(edit_code_in_place(code, instr))
            
    except Exception as e:
        print(f"⚠️ An error occurred: {str(e)}")