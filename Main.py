class Task:
    def __init__(self, id, title, description="",status="Pending"):
        self.id = id
        self.title = title
        self.description = description
        self.status = status

    def search_tasks(self, query):
        """Search for tasks by title or description."""
        query = query.lower()
        """ To make it case-insensitive"""

        results = [task for task in self.tasks if query in task.title.lower() or query in task.description.lower()]
        """ query result for description or title of a task"""
        return results