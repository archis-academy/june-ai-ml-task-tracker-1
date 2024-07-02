class CLI:
    def __init__(self, task_manager, user_manager):
        self.task_manager = task_manager
        self.user_manager = user_manager
        self.current_user = None

    def run(self):
        while True:
            command = input("Enter command (register/login/add_task/exit): ").strip().lower() 
            if command == "register":
                self.register()  
            elif command == "login":
                self.login()  
            elif command == "add_task":
                self.add_task() 
            elif command == "exit":
                break
            else:
                print("Invalid command.")

    def register(self):
        username = input("Enter username: ").strip()
        password = input("Enter password: ").strip()
        self.user_manager.register_user(username, password) 

    def login(self):
        username = input("Enter username: ").strip()
        password = input("Enter password: ").strip()
        user = self.user_manager.authenticate_user(username, password)
        if user:
            self.current_user = user
            print("Login successful.")
        else:
            print("Invalid username or password.")       
             
    def add_task(self):
        if not self.current_user:
            print("You need to log in first.")
            return
        title = input("Enter task title: ").strip()
        description = input("Enter task description: ").strip()
        category = input("Enter task category: ").strip()
        task = self.task_manager.add_task(title, description, user_id=self.current_user.id, category=category)
        print(f"Task added: {task.get_info()}")  