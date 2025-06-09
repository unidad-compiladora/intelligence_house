from device_menu import mostrar_menu
from aut_controller import mostrar_menu_automatizacion
from users_data_base import users 

def list_user():
    for user in users:
        rol = "Administrador" if user["is_admin"] else "Usuario"
        print("---------------------------------------------------------")
        print(f"- nombre : {user['name']}")
        print(f"- apellido: {user['lastname']}")
        print(f"- email: {user['mail']}" )
        print(f"- rol: {rol}\n")

def change_role(mail):
    for user in users:
        if mail.lower() == user["mail"].lower():
            user["is_admin"] = True
        else:
            user["is_admin"] = False
    if found:
        print(f"El usuario con correo {mail} ahora es administrador.")
    else:
        print("Usuario no encontrado.")

def admin_user(user):
    while True:
        print("\n")
        print(f"----------------- Bienvenido {user['name']} (ADMIN) -----------------")
        print("Administrador")
        print("1 Consultar automatizaciones") 
        print("2 Gestionar dispositivos")
        print("3 Modificar rol de usuario")
        print("4 Salir Sesion\n")

        option = input("Ingrese una opción: ")

        if option == "1":
            mostrar_menu_automatizacion()
        elif option == "2":
            mostrar_menu()
        elif option == "3":
            list_user()
            mail = input("Ingrese el correo del usuario que será administrador: ").strip()
            change_role(mail)
        elif option == "4":
            print("Sesión finalizada.")
            break
        else:
            print("Opción inválida. Por favor intente de nuevo.")
