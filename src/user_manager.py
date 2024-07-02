from user import User
class UserManager:
    def __init__(self):
        self.users = {}  # key value {username:user_object}
        self.next_id = 1

    def authenticate_user(self, username, password):
        user = self.users.get(username)
        if user and user.password == password:
            return user
        return None
    
    def register_user(self, username, password):
        if username in self.users:
            print("Username already exists.")
            return None
        user = User(self.next_id, username, password)
        self.users[username] = user
        self.next_id += 1
        print("User registered successfully.")
        return user