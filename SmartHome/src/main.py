from users.user_manager import UserManager
from users.user import User
from db.connection import DataBase


def main():
    db=DataBase()
    user_dao=User(db)
    user_manager=UserManager(user_dao)

    while True:

        menu()

        try:
            opcion=int(input("Elija una opcion: "))

        except ValueError:

            print("opcion incorrecta , ingrese nuevamente")
            continue

        if opcion == 1:

            user=input("Ingrese el usuario: ")
            password=input("Ingrese su contraseña: ")

            pass
        if opcion == 2:
          
            data=get_user_registration_data()
            register_user=user_manager.register(data)

            if register_user:
                 print("Usuario cargado correctamente")

            else:
                 print(" Intente nuevamente ")
           
        if opcion == 3:

            break


def get_user_registration_data():
        
        name=input("ingrese su nombre: ")
        lastname=input("ingrese su apellido: ")
        email=input("ingrese su email : ")
        password=input("ingrese su contraseña: ") 
            
        return {
             "name":name,
             "lastname":lastname,
             "email":email,
             "password":password,
        }

def menu():

        print("--- Bienvenido a Smart Home--- ")

        print("1- Iniciar Sesion ")
        print("2- Registrarse ")
        print("3- Salir")



if __name__== "__main__":

    main()