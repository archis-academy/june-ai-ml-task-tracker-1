class UserManager:
    def __init__(self):
        self.users = {} #we are going to use dictionary data type in order to store user object with a key value pair

        #for example,{"example@gmail.com" : user object}


    def authenticate_user(self,username,password):
        user = self.users.get(username)
        if user and user.password == password:
            return user
        return None



