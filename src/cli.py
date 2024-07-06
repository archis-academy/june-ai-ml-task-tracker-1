from task_manager import TaskManager
from user_manager import UserManager
from datetime import datetime as dt, timedelta

class CLI:
    def __init__(self, task_manager, user_manager):
        self.task_manager = task_manager
        self.user_manager = user_manager
        self.current_user = None

    def run(self):
        while True:
            command = input("Enter command (register/login/logout/add_task/display_tasks/sort_tasks/filter_tasks/search_tasks/filter_status/filter_category/share_task/add_comment/update_task/delete_task/mark_complete/mark_incomplete/archive_completed_tasks/display_archived_tasks/upcoming_tasks/overdue_tasks/task_counts/exit): ").strip().lower()
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
            elif command == "add_comment":
                self.add_comment()
            elif command == "update_task":
                self.update_task()
            elif command == "delete_task":
                self.delete_task()
            elif command == "mark_complete":
                self.mark_complete()
            elif command == "mark_incomplete":
                self.mark_incomplete()
            elif command == "archive_completed_tasks":
                self.archive_completed_tasks()
            elif command == "display_archived_tasks":
                self.display_archived_tasks()
            elif command == "upcoming_tasks":
                self.show_upcoming_tasks()
            elif command == "overdue_tasks":
                self.show_overdue_tasks()
            elif command == "task_counts":
                self.display_task_counts()
            elif command == "save":
                self.save_tasks()
            elif command == "load":
                self.load_tasks()
            elif command == "exit":
                break
            else:
                print("Invalid command.")

    def register(self):
        username = input("Enter username: ").strip()
        password = input("Enter password: ").strip()
        user_id = len(self.user_manager.users) + 1
        user = self.user_manager.register_user(user_id, username, password)
        if user:
            print(f"User '{username}' registered successfully.")
        else:
            print(f"Failed to register user '{username}'. Username may already be taken.")

    def login(self):
        if self.current_user:
            print("You are already logged in.")
            return
        username = input("Enter username: ").strip()
        password = input("Enter password: ").strip()
        self.current_user = self.user_manager.authenticate_user(username, password)
        if self.current_user:
            print(f"Logged in as '{username}'.")
        else:
            print("Login failed. Invalid username or password.")

    def logout(self):
        if self.current_user:
            self.current_user = None
            print("Logged out successfully.")
        else:
            print("No user is currently logged in.")

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
        tasks = self.task_manager.display_all_tasks(self.current_user.id)
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

    def filter_status(self):
        if not self.current_user:
            print("You need to log in first.")
            return

        status = input("Enter status to filter (Pending/Completed): ").strip().capitalize()
        if status not in ["Pending", "Completed"]:
            print("Invalid status. Please enter 'Pending' or 'Completed'.")
            return
        
        filtered_tasks = [task for task in self.task_manager.tasks.values() if task.status == status]
        if filtered_tasks:
            print(f"Tasks with status '{status}':")
            for task in filtered_tasks:
                print(task.get_info())
        else:
            print(f"No tasks found with status '{status}'.")

    def filter_category(self):
        if not self.current_user:
            print("You need to log in first.")
            return
        category = input("Enter category to filter: ").strip()
        filtered_tasks = self.task_manager.filter_by_category(category)
        if filtered_tasks:
            for task in filtered_tasks:
                print(task.get_info())
        else:
            print(f"No tasks found in category '{category}'.")

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

    def add_comment(self):
        if not self.current_user:
            print("You need to log in first.")
            return
        task_id = int(input("Enter task ID to comment on: ").strip())
        comment = input("Enter your comment: ").strip()
        task = self.task_manager.add_comment_to_task(task_id, comment)
        if task:
            print(f"Comment added to task {task_id}.")
        else:
            print("Task not found.")

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

    def delete_task(self):
        if not self.current_user:
            print("You need to log in first.")
            return
        task_id = int(input("Enter task ID to delete: ").strip())
        success = self.task_manager.delete_task(task_id)
        if success:
            print(f"Task {task_id} deleted.")
        else:
            print("Task not found.")

    def mark_complete(self):
        if not self.current_user:
            print("You need to log in first.")
            return
        task_id = int(input("Enter task ID to mark as complete: ").strip())
        task = self.task_manager.tasks.get(task_id)
        if task:
            task.mark_complete()
            print(f"Task {task_id} marked as complete.")
        else:
            print("Task not found.")

    def mark_incomplete(self):
        if not self.current_user:
            print("You need to log in first.")
            return
        task_id = int(input("Enter task ID to mark as incomplete: ").strip())
        task = self.task_manager.tasks.get(task_id)
        if task:
            task.mark_incomplete()
            print(f"Task {task_id} marked as incomplete.")
        else:
            print("Task not found.")

    def archive_completed_tasks(self):
        if not self.current_user:
            print("You need to log in first.")
            return
        archived_tasks = self.task_manager.archive_completed_tasks()
        if archived_tasks:
            print("Completed tasks archived successfully.")
        else:
            print("No completed tasks to archive.")

    def display_archived_tasks(self):
        if not self.current_user:
            print("You need to log in first.")
            return
        archived_tasks = self.task_manager.get_archived_tasks()
        if archived_tasks:
            print("Archived Tasks:")
            for task in archived_tasks:
                print(task.get_info())
        else:
            print("No archived tasks.")

    def show_upcoming_tasks(self):
        if not self.current_user:
            print("You need to log in first.")
            return
        upcoming_tasks = self.task_manager.get_upcoming_tasks()
        if upcoming_tasks:
            print("Upcoming Tasks:")
            for task in upcoming_tasks:
                print(task.get_info())
        else:
            print("No upcoming tasks.")

    def show_overdue_tasks(self):
        if not self.current_user:
            print("You need to log in first.")
            return
        overdue_tasks = self.task_manager.get_overdue_tasks()
        if overdue_tasks:
            print("Overdue Tasks:")
            for task in overdue_tasks:
                print(task.get_info())
        else:
            print("No overdue tasks.")

    def display_task_counts(self):
        if not self.current_user:
            print("You need to log in first.")
            return
        total_tasks = len(self.task_manager.tasks)
        completed_tasks = len([task for task in self.task_manager.tasks.values() if task.status == "Completed"])
        print(f"Total Tasks: {total_tasks}")
        print(f"Completed Tasks: {completed_tasks}")

    def save_tasks(self):
        filename = input("Enter filename to save tasks: ").strip()
        self.task_manager.save_to_file(filename)

    def load_tasks(self):
        filename = input("Enter filename to load tasks from: ").strip()
        self.task_manager.load_from_file(filename)