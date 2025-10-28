import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os

load_dotenv()

DB_HOST=os.getenv("DB_HOST")
DB_USER=os.getenv("DB_USER")
DB_PASSWORD=os.getenv("DB_PASSWORD")
DB_NAME=os.getenv("DB_NAME")

class DataBase:
    
    def __init__(self):
        self.__conn=None
       

    def connect(self):

        if self.__conn is None or not self.__conn.is_connected():
            try: 
                self.__conn=mysql.connector.connect(
        
                    host=DB_HOST,
                    user=DB_USER,
                    password=DB_PASSWORD,
                    database=DB_NAME
                )
                print("CONEXION")
            except Error as e:
                print(f"Error de conexion: {e}")
            
                self.__conn= None
        return self.__conn
    
    def get_connection(self):

        return self.__conn

    def close(self):
        if self.__conn and self.__conn.is_connected():

            self.__conn.close()

            self.__conn=None