import datetime

class Task:

## constructor for the task class 
## @param id the uniqe id of the project
## @param status the status of the task (pending as deafault)

    def __init__(self, id, status='pending'):
        self.creation_date = datetime.datetime.now()
        self.id = id
        self.status = status

## methods fot the class task. the object of the class task is given as parameter 

def get_creation_date(task):
    return task.creation_date

def sort_by_creation_date(tasks):
    tasks.sort(key=get_creation_date)

def sort_by_status(tasks):
    pending_tasks = []
    completed_tasks = []
    cancelled_tasks = []

    for task in tasks:
        if task.status == 'pending':
            pending_tasks.append(task)
        elif task.status == 'completed':
            completed_tasks.append(task)
        elif task.status == 'cancelled':
            cancelled_tasks.append(task)
        else:
            print('Invalid input:', task.status)

    return pending_tasks, completed_tasks, cancelled_tasks