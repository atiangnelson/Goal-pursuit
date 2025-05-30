from lib.models.cli import list_goals, add_goal, complete_goal, delete_goal

def print_help():
    print("""
Commands:
  add [title]        - Add a goal
  list               - List all goals
  complete [id]      - Mark goal as complete
  delete [id]        - Delete a goal
  exit               - Exit app
""")
    
def main():
    print("Welcome to Goal Tracker CLI")
    print_help()    

    while True:
        try:
            cmd = input("\n> ").strip().split()
            if not cmd:
                continue

        command = cmd[0]
        if command == "add":
            add_goal(" ".join(cmd[1:]))

        elif command == "list":
            list_goals()