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