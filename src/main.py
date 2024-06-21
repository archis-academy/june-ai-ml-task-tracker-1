from task_manager import TaskManager
from user_manager import UserManager
from src.cli import CLI

if __name__ == "__main__":
    task_manager = TaskManager()
    user_manager = UserManager()
    cli = CLI(task_manager, user_manager)
