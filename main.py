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

            elif command == "complete" and len(cmd) > 1 and cmd[1].isdigit():
                complete_goal(int(cmd[1]))

            elif command == "delete" and len(cmd) > 1 and cmd[1].isdigit():
                delete_goal(int(cmd[1]))      

            elif command == "exit":
                break

            else:
                print("Unknown command.")
                print_help()          

        except KeyboardInterrupt:
            print("\nExiting...")
            break

if __name__ == '__main__':
    main()