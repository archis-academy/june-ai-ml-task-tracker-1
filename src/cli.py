class CLI:
    def __init__(self, task_manager, user_manager):
        self.task_manager = task_manager
        self.user_manager = user_manager
        self.current_user = None
        
    def run(self):
        while True:
            command = input("Enter command (register/login/add_task/display_tasks/exit): ").strip().lower()
            if command == "register":
                self.register()  
            elif command == "login":
                self.login() 
            elif command == "add_task":
                self.add_task() 
            elif command == "display_tasks":
                self.display_tasks()  
            elif command == "exit":
                break
            else:
                print("Invalid command.")

    def display_tasks(self):
        if not self.current_user:
            print("You need to log in first.")
            return
        tasks = self.task_manager.display_all_tasks()
        if tasks:
            for task in tasks:
                print(task.get_info())
        else:
            print("No tasks available.")