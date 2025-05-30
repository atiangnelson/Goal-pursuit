from lib.models import session
from lib.models.goals import Goal

def list_goals():
    goals = session.query(Goal).all()
    for goal in goals:
        print(goal)

def add_goal(title):
    goal = Goal(title=title)
    session.add(goal)
    session.commit()
    print(f"Added goal: {goal.title}")

def complete_goal(goal_id):
    goal = session.get(Goal, goal_id)
    if goal:
        goal.completed = True
        session.commit()
        print(f"Goal '{goal.title}' is completed.")
    else:
        print("Goal not found.")

def delete_goal(goal_id):
    goal = session.get(Goal, goal_id)
    if goal:
        session.delete(goal)
        session.commit()
        print(f"Deleted goal '{goal.title}'.")
    else:
        print("Goal not found.")
