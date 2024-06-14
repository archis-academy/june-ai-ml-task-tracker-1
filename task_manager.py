from task import Task


class TaskManager:
    def __init__(self):
        self.tasks = {}  # key value
        self.next_id = 1
