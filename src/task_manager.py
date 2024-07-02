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

    def display_all_tasks(self):
        return list(self.tasks.values()) 
    
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