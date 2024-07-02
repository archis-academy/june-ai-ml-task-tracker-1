from task import Task

class TaskManager:
    def __init__(self):
        self.tasks = {}  # key value
        self.next_id = 1
    
    def sort_by_creation_date(self):
        self.tasks.sort(key=lambda task: task.due_date)

    def sort_by_status(self):
        pending_tasks = []
        completed_tasks = []
        cancelled_tasks = []

        for task in self.tasks:
            if task.status == 'pending':
                pending_tasks.append(task)
            elif task.status == 'completed':
                completed_tasks.append(task)
            elif task.status == 'cancelled':
                cancelled_tasks.append(task)
            else:
                print('Invalid status:', task.status)
        return pending_tasks, completed_tasks, cancelled_tasks

    def get_all_info(self):
        for task in self.tasks:
            print(task.get_info())

    def add_task(self, title, description, status="Pending", priority="Normal", due_date=None, user_id=None, category=None):
        task = Task(self.next_id, title, description, status, priority, due_date, user_id, category)
        self.tasks[self.next_id] = task
        self.next_id += 1
        return task
