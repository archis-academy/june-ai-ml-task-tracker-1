class UserManager:
    def __init__(self):
        self.users = {}  # key value {username:user_object}

    def authenticate_user(self, username, password):
        user = self.users.get(username)
        if user and user.password == password:
            return user
        return None
