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
        self.history = []

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
            f"Comments: {', '.join(self.comments) if self.comments else 'No comments'}\n"
            f"History: {self.history}\n")
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
    
    def add_tag(self, tag):
        self.tags.add(tag.lower()) 

    def remove_tag(self, tag):
        self.tags.discard(tag.lower()) 

    def has_tag(self, tag):
        return tag.lower() in self.tags
    
    def update_task_details(self, new_title=None, new_description=None, new_due_date=None, new_category=None):
        updates = []
        if new_title and self.title != new_title:
            self.title = new_title
            updates.append(f"Updated title to {new_title}")
        if new_description and self.description != new_description:
            self.description = new_description
            updates.append(f"Updated description to {new_description}")
        if new_due_date and self.due_date != new_due_date:
            self.due_date = new_due_date
            updates.append(f"Updated due date to {new_due_date}")
        if new_category and self.category != new_category:
            self.category = new_category
            updates.append(f"Updated category to {new_category}")
        if updates:
            self._add_to_history(", ".join(updates))

    def _add_to_history(self, action):
        timestamp = dt.now()
        self.history.append((timestamp, action))

    def view_history(self):
        if self.history:
            for timestamp, action in self.history:
                print(f"{timestamp}: {action}")
        else:
            print("No history available.")