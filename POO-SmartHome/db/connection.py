import mysql.connector
from mysql.connector import Error


class DataBase:
    def __init__(self, host,user,password,database):

        self.__host=host,
        self.__user=user,
        self.__password=password,
        self.__database=database
        self.__conn=None

    def connect(self):

        try: 
            self.__conn=mysql.connector.connect(
        
                host=self.__host,
                user=self.__user,
                password=self.__password,
                database=self.__database

            )
        except Error as e:
            print(f"Error de conexion: {e}")
 
    def get_connection(self):

        if self.con is None or not self.__conn.is_connected():
            self.connect()
        return self.__conn

    def close(self):
        if self.__conn and self.__conn.is_connected():
            self.__conn.close()