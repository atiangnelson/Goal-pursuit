#  Goal Tracker CLI

A simple command-line application to help you track your personal goals using Python and SQLAlchemy.

## 📦 Features

- Add new goals
- List all saved goals
- Mark goals as completed
- Delete goals
- SQLite database support
- Alembic integration for database migrations

# Project Structure
Goal-Pursuit/
│
├── lib/
│ └── models/
│ ├── init.py 
│ ├── goal.py 
│ └── cli.py 
│
├── migrations/ 
│ └── versions/
│
├── alembic.ini 
├── main.py 
└── README.md

# Set Up Virtual Environment
python3 -m venv venv
source venv/bin/activate

#  Install Dependencies
pip install sqlalchemy alembic

#  Initialize the Database
alembic upgrade head

#  Run the App
python main.py
 
# Available Commands
add [title]        - Add a new goal
list               - List all goals
complete [id]      - Mark goal as completed
delete [id]        - Delete a goal
exit               - Exit the app

# Example Usage
> add Finish reading "Atomic Habits"
Added goal: Finish reading "Atomic Habits"

> list
1. Finish reading "Atomic Habits" 

> complete 1
Goal 'Finish reading "Atomic Habits"' marked as completed.

> delete 1
Deleted goal 'Finish reading "Atomic Habits"'.

