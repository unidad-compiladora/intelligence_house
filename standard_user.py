from device_fun import listar_dispositivos
from device_menu import mostrar_menu

def standard_user(user):
    while True:
        print("\n")
        print(f"----------------- Bienvenido {user['name']} -----------------")
        print("Usuario")
        print("1 Datos Personales")
        print("2 Control dispositivos")
        print("3 Dispositivos disponibles")
        print("4 Salir Sesion\n")
        
        try:
            option = int(input("Ingrese una opción: "))
        except ValueError:
            print("Opción inválida. Por favor, ingrese un número.")
            continue

        if option == 1:
            rol = "Administrador" if user["is_admin"] else "Usuario"
            print("-------------------- Datos personales--------------------")
            print(f"- nombre : {user['name']}")
            print(f"- apellido: {user['lastname']}")
            print(f"- email: {user['mail']}")
            print(f"- rol: {rol}")
            print("---------------------------------------------------------")

        elif option == 2:
            mostrar_menu()

        elif option == 3:
            listar_dispositivos()

        elif option == 4:
            break

        else:
            print("Opción inválida. Por favor, intente de nuevo.")
