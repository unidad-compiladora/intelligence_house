from dao.interfaces.users_dao import Users_dao
from db.connection import  DataBase

class User(Users_dao):
   
    def __init__ (self,db:DataBase):
        self.__db=db
        self.__conn=self.__db.connect()
        

    def get_all(self):

        cursor=self.__conn.cursor()

        cursor.execute("SELECT * FROM Users")   
        users=cursor.fetchall()
        cursor.close()

        return users

    def get_by_id(self,id):
        
        cursor=self.__conn.cursor()
        query="SELECT * FROM Users WHERE user_id = %s"
        cursor.execute(query,(id,))
        cursor.close()
        return cursor.fetchone()
      

    def delete_by_id(self,id):
        pass

    def update(self,id:int,data:dict):
        pass

    
    def user_post(self,data):

        cursor= self.__conn.cursor()
        query="INSERT INTO Users (name,lastname,email,password) VALUES (%s,%s,%s,%s)"
        value=(data["name"],data["lastname"],data["email"],data["password"])
        cursor.execute(query,value)
        self.__conn.commit()
        cursor.close




        
db=DataBase()
user=User(db)
user.get_by_id(1)
db.close()

   
""" def __init__(self, name, lastname, mail, password, is_admin=False):
        self.__name = name
        self.__lastname = lastname
        self.__mail = mail
        self.__password = password
        self.__is_admin = is_admin

    # Getters
    def get_name(self): return self.__name
    def get_lastname(self): return self.__lastname
    def get_mail(self): return self.__mail
    def get_password(self): return self.__password
    def get_is_admin(self): return self.__is_admin

    # Setters
    def set_name(self, name): self.__name = name
    def set_lastname(self, lastname): self.__lastname = lastname
    def set_mail(self, mail): self.__mail = mail
    def set_password(self, password): self.__password = password
    def set_is_admin(self, is_admin): self.__is_admin = is_admin

    # Métodos públicos
    def register(self):
        return f"User {self.__name} registered successfully."

    def login(self, mail, password):
        return self.__mail == mail and self.__password == password
"""