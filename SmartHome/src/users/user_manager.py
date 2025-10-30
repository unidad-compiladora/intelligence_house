
class UserManager:
    
    def __init__(self,user):
        self.__user=user

    def register(self,data):

        register_user=self.__user.user_post(data)
        return register_user


    def login(self):

        pass


 
