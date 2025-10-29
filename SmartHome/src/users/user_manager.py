
class UserManager:
    
    def __init__(self,user):
        self.__user=user

    def register(self,data):

        self.__user.user_post(data)


    def login(self):

        pass


 
