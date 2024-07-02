class CLI:
    def __init__(self, task_manager, user_manager):
        self.task_manager = task_manager
        self.user_manager = user_manager
        self.current_user = None
## my run method from previous commits of prev branches updated to handle logout as well when executed. new branch thats why copied form previous
    def run(self):
        while True:
            command = input("Enter command (register/login/logout/add_task/display_tasks/update_task/exit): ").strip().lower() 
            if command == "register":
                self.register()
            elif command == "login":
                self.login()
            elif command == "logout":
                self.logout() 
            elif command == "add_task":
                self.add_task()
            elif command == "display_tasks":
                self.display_tasks()
            elif command == "update_task":
                self.update_task()
            elif command == "exit":
                break
            else:
                print("Invalid command.")

    def logout(self):

        if self.current_user:
            self.current_user = None
            print("Logged out successfully.")  
        else:
            print("No user is currently logged in.")