from datetime import datetime as dt


class Task:
    def __init__(self, id, title, description, status="Pending", priority="Normal", due_date=None, user_id=None,category=None):
        self.id = id
        self.title = title
        self.description = description
        self.status = status
        self.priority = priority
        self.due_date = dt.now()
        self.user_id = user_id
        self.category = category
        self.subtasks = []
        self.comments = []
        self.tags = []

    def get_info(self):
        info = (
            f"Id: {self.id}\n"
            f"Title: {self.title}\n"
            f"Description: {self.description}\n"
            f"Due Date: {self.due_date}\n"
            f"Priority: {self.priority}\n"
            f"Status: {self.status}\n"
            f"User ID: {self.user_id}\n")
        return info
