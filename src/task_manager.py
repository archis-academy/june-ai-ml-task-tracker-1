from task import Task

class TaskManager:
    def __init__(self):
        self.tasks = {}

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

