from db.connection import DataBase




class UserManager():


    def __init__(self,db:DataBase):

        self.__db=db
        self.__conn=self.__db.connect()

    def register(self,username:str,password: str):

        pass

    def login(self,data:dict):

        pass

db=DataBase()
user=UserManager(db)

