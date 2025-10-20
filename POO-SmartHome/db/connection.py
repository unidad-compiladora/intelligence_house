import mysql.connector
from mysql.connector import Error


class DataBase:
    def __init__(self, host,user,password,database):

        self.host=host,
        self.user=user,
        self.password=password,
        self.database=database
        self.con=None

    def connect(self):

        try: 
            self.conn=mysql.connector.connect(
        
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database

            )
        except Error as e:
            print(f"Error de conexion: {e}")
 

