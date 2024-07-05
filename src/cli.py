from task_manager import TaskManager
from user_manager import UserManager

class CLI:
    def __init__(self, task_manager, user_manager):
        self.task_manager = task_manager
        self.user_manager = user_manager
        self.current_user = None

    def run(self):
        while True:
            command = input("Enter command (register/login/logout/add_task/display_tasks/sort_tasks/filter_tasks/search_tasks/filter_status/filter_category/share_task/update_task/exit): ").strip().lower()
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
            elif command == "sort_tasks":
                self.sort_tasks()
            elif command == "filter_tasks":
                self.filter_tasks()
            elif command == "search_tasks":
                self.search_tasks()
            elif command == "filter_status":
                self.filter_status()
            elif command == "filter_category":
                self.filter_category()
            elif command == "share_task":
                self.share_task()
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
        priority = input("Enter task priority (High/Medium/Low): ").strip().capitalize()
        category = input("Enter task category: ").strip()
        task = self.task_manager.add_task(title, description, priority=priority, user_id=self.current_user.id, category=category)
        print(f"Task added: {task.get_info()}")

    def display_tasks(self):
        if not self.current_user:
            print("You need to log in first.")
            return
        tasks = self.task_manager.tasks.values()
        if tasks:
            for task in tasks:
                print(task.get_info())
        else:
            print("No tasks available.")

    def sort_tasks(self):
        if not self.current_user:
            print("You need to log in first.")
            return
        sorted_tasks = self.task_manager.sort_by_priority()
        if sorted_tasks:
            for task in sorted_tasks:
                print(task.get_info())
        else:
            print("No tasks available to sort.")

    def filter_tasks(self):
        if not self.current_user:
            print("You need to log in first.")
            return
        priority = input("Enter priority to filter (High/Medium/Low): ").strip().capitalize()
        filtered_tasks = self.task_manager.filter_by_priority(priority)
        if filtered_tasks:
            for task in filtered_tasks:
                print(task.get_info())
        else:
            print(f"No tasks found with priority {priority}.")

    def update_task(self):
        if not self.current_user:
            print("You need to log in first.")
            return
        task_id = int(input("Enter task ID: ").strip())
        title = input("Enter new task title (or leave blank to keep current): ").strip() or None
        description = input("Enter new task description (or leave blank to keep current): ").strip() or None
        status = input("Enter new task status (or leave blank to keep current): ").strip() or None
        priority = input("Enter new task priority (or leave blank to keep current): ").strip().capitalize() or None
        due_date = input("Enter new task due date (or leave blank to keep current): ").strip() or None
        category = input("Enter new task category (or leave blank to keep current): ").strip() or None
        
        updated = self.task_manager.update_task(task_id, title, description, status, priority, due_date, category)
        if updated:
            print("Task updated successfully.")
        else:
            print("Task not found.")

    def share_task(self):
        if not self.current_user:
            print("You need to log in first.")
            return
        task_id = int(input("Enter task ID to share: ").strip())
        username = input("Enter username to share with: ").strip()
        user = self.user_manager.users.get(username)
        if user:
            task = self.task_manager.share_task(task_id, username)
            if task:
                print(f"Task shared with {username}.")
            else:
                print("Task not found.")
        else:
            print("User not found.")

    def logout(self):
        if self.current_user:
            self.current_user = None
            print("Logged out successfully.")
        else:
            print("No user is currently logged in.")

    def search_tasks(self):
        if not self.current_user:
            print("You need to log in first.")
            return
        keyword = input("Enter keyword to search: ").strip()
        matched_tasks = self.task_manager.search_tasks(keyword)
        if matched_tasks:
            for task in matched_tasks:
                print(task.get_info())
        else:
            print("No tasks found matching the keyword.")

if __name__ == "__main__":
    task_manager = TaskManager()
    user_manager = UserManager()
    cli = CLI(task_manager, user_manager)
    cli.run()
