import mysql.connector
from mysql.connector import Error


class DataBase:
    def __init__(self, host,user,password,database):

        self.host=host,
        self.user=user,
        self.password=password,
        self.database=database
        self.conn=None

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
 
    def get_connection(self):

        if self.con is None or not self.conn.is_connected():
            self.connect()
        return self.conn

    def close(self):
        if self.conn and self.conn.is_connected():
            self.conn.close()