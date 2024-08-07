from task import Task
from datetime import datetime, timedelta
import json

class TaskManager:
    def __init__(self):
        self.tasks = {}
        self.archived_tasks = {}  
        self.next_id = 1

    def add_task(self, title, description, status="Pending", priority="Normal", due_date=None, user_id=None, category=None):
        task = Task(self.next_id, title, description, status, priority, due_date, user_id, category)
        self.tasks[self.next_id] = task
        self.next_id += 1
        return task

    def display_all_tasks(self, user_id):
        return [task for task in self.tasks.values() if task.user_id == user_id]

    def update_task(self, task_id, title=None, description=None, status=None, priority=None, due_date=None, category=None):
        task = self.tasks.get(task_id)
        if not task:
            return False
        
        if title is not None:
            task.title = title
        if description is not None:
            task.description = description
        if status is not None:
            task.status = status
        if priority is not None:
            task.priority = priority
        if due_date is not None:
            task.due_date = due_date
        if category is not None:
            task.category = category
        
        return True
    def sort_by_priority(self):
        return sorted(self.tasks.values(), key=lambda task: task.get_priority())

    def filter_by_priority(self, priority):
        return [task for task in self.tasks.values() if task.get_priority() == priority]


    def search_tasks(self, keyword):
        matched_tasks = []
        for task in self.tasks.values():
            if keyword.lower() in task.title.lower() or keyword.lower() in task.description.lower():
                matched_tasks.append(task)
        return matched_tasks
    
    def share_task(self, task_id, username):
        if task_id in self.tasks:
            task = self.tasks[task_id]
            task.share_with(username)
            return task
        else:
            return None

    def add_comment_to_task(self, task_id, comment):
        if task_id in self.tasks:
            task = self.tasks[task_id]
            task.add_comment(comment)
            return task
        else:
            return None

    def delete_task(self, task_id):
        if task_id in self.tasks:
            del self.tasks[task_id]
            return True
        else:
            return False

    def get_upcoming_tasks(self, days=7):
        today = datetime.now().date()
        end_date = today + timedelta(days=days)
        upcoming_tasks = [task for task in self.tasks.values() if task.due_date.date() <= end_date and task.due_date.date() >= today]
        return upcoming_tasks

    def get_overdue_tasks(self):
        overdue_tasks = [task for task in self.tasks.values() if task.due_date.date() < datetime.now().date() and task.status != "Completed"]
        return overdue_tasks
    
    def filter_by_tag(self, tag):
        return [task for task in self.tasks.values() if task.has_tag(tag)]
    
    def archive_completed_tasks(self):
        tasks_to_archive = [task for task in self.tasks.values() if task.status == "Completed"]
        for task in tasks_to_archive:
            self.archived_tasks[task.id] = task
            del self.tasks[task.id]

    def get_archived_tasks(self):
        return list(self.archived_tasks.values())
    
    def count_total_tasks(self):
        return len(self.tasks) + len(self.archived_tasks)

    def count_completed_tasks(self):
        completed_count = 0
        for task in self.tasks.values():
            if task.status == "Completed":
                completed_count += 1
        for task in self.archived_tasks.values():
            if task.status == "Completed":
                completed_count += 1
        return completed_count
    
    def save_to_file(self, filename):
        data = {
            'tasks': [task.__dict__ for task in self.tasks.values()],
            'archived_tasks': [task.__dict__ for task in self.archived_tasks.values()]
        }
        with open(filename, 'w') as file:
            json.dump(data, file)
        print("Tasks saved to file.")

    def load_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                self.tasks = {task['id']: Task(**task) for task in data['tasks']}
                self.archived_tasks = {task['id']: Task(**task) for task in data['archived_tasks']}
            print("Tasks loaded from file.")
        except FileNotFoundError:
            print("File not found.")