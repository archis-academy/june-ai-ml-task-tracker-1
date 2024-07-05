from datetime import datetime as dt

class Task:
    def __init__(self, id, title, description, status="Pending", priority="Normal", due_date=None, user_id=None, category=None):
        self.id = id
        self.title = title
        self.description = description
        self.status = status
        self.priority = priority
        self.due_date = dt.now() if due_date is None else due_date
        self.user_id = user_id
        self.category = category
        self.shared_with = [] 
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
            f"User ID: {self.user_id}\n"
            f"Category: {self.category}\n"
            f"Shared With: {', '.join(self.shared_with) if self.shared_with else 'No one'}\n"
            f"Comments: {', '.join(self.comments) if self.comments else 'No comments'}\n")
        return info
    
    def share_with(self, username):
        if username not in self.shared_with:
            self.shared_with.append(username)

    def set_priority(self, priority):
        self.priority = priority

    def get_priority(self):
        return self.priority
    
    def add_comment(self, comment):
        self.comments.append(comment)

    def mark_complete(self):
        self.status = "Completed"

    def mark_incomplete(self):
        self.status = "Pending"

    def add_subtask(self, subtask):
        self.subtasks.append(subtask)

    def view_subtasks(self):
        if self.subtasks:
            print(f"Subtasks for Task '{self.title}':")
            for subtask in self.subtasks:
                print(subtask.get_info())
        else:
            print(f"No subtasks for Task '{self.title}'.")

    def delete_subtask(self, subtask_id):
        for subtask in self.subtasks:
            if subtask.id == subtask_id:
                self.subtasks.remove(subtask)
                return True
        return False