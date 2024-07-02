from task_manager import TaskManager
from user_manager import UserManager

class CLI:
    def __init__(self, task_manager, user_manager):
        self.task_manager = task_manager
        self.user_manager = user_manager
        self.current_user = None

    def run(self):
        while True:
            command = input("Enter command (register/login/logout/add_task/display_tasks/update_task/exit): ").strip().lower()
            if command == "register":
                self.register()
            elif command == "login":
                self.login()
            elif command == "logout":
                self.logout()
            elif command == "add_task":
                self.add_task()
            elif command == "display_tasks":
                self.display_tasks()
            elif command == "update_task":
                self.update_task()
            elif command == "exit":
                break
            else:
                print("Invalid command.")

    def add_task(self):
        if not self.current_user:
            print("You need to log in first.")
            return
        title = input("Enter task title: ").strip()
        description = input("Enter task description: ").strip()
        category = input("Enter task category: ").strip()
        task = self.task_manager.add_task(title, description, user_id=self.current_user.id, category=category)
        print(f"Task added: {task.get_info()}")

    def display_tasks(self):
        if not self.current_user:
            print("You need to log in first.")
            return
        tasks = self.task_manager.display_all_tasks(self.current_user.id)
        if tasks:
            for task in tasks:
                print(task.get_info())
        else:
            print("No tasks available.")

    def update_task(self):
        if not self.current_user:
            print("You need to log in first.")
            return
        task_id = int(input("Enter task ID: ").strip())
        title = input("Enter new task title (or leave blank to keep current): ").strip() or None
        description = input("Enter new task description (or leave blank to keep current): ").strip() or None
        status = input("Enter new task status (or leave blank to keep current): ").strip() or None
        priority = input("Enter new task priority (or leave blank to keep current): ").strip() or None
        due_date = input("Enter new task due date (or leave blank to keep current): ").strip() or None
        category = input("Enter new task category (or leave blank to keep current): ").strip() or None
        
        updated = self.task_manager.update_task(task_id, title, description, status, priority, due_date, category)
        if updated:
            print("Task updated successfully.")
        else:
            print("Task not found.")

    def logout(self):
        if self.current_user:
            self.current_user = None
            print("Logged out successfully.")
        else:
            print("No user is currently logged in.")

