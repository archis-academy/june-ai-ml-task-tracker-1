from user import User


class UserManager:
    def __init__(self):
        self.users = {}  # key value {username:user_object}
