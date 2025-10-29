from db.connection import DataBase

class User_manager():

    db=DataBase()

    def __init__(self):
        
        self.__conn=self.db.connect()