import datetime

class TaskManager:

    def __init__(self, tasks):
        self.tasks = tasks

    def sort_by_creation_date(self):
        self.tasks.sort(key=lambda task: task.creation_date)

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


class Task:
    ## constructor for the task class 
    ## @param id the unique id of the project
    ## @param status the status of the task (pending as default)

    def __init__(self, user, title, description, duration, priority, ticket_number, id, status='pending'):
        self.creation_date = datetime.datetime.now()
        self.user = user
        self.title = title
        self.description = description
        self.duration = duration
        self.priority = priority
        self.ticket_number = ticket_number
        self.id = id
        self.status = status

    ## method to get the info of the task
    def get_info(self):
        info = (
            f"Ticket number: {self.ticket_number}\n"
            f"Id: {self.id}\n"
            f"Title: {self.title}\n"
            f"Description: {self.description}\n"
            f"Duration: {self.duration}\n"
            f"Priority: {self.priority}\n"
            f"Status: {self.status}\n"
            f"Creation Date: {self.creation_date}\n")
        return info

