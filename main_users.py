from auth_system import register, user_session

def login():
    
    while True:

        print("---------------- Bienvenido a Intelligence house ----------------")
        print("1-  Iniciar sesion ")
        print("2-  Registrarse ")
        print("3-  Cerrar Aplicacion  ")
        print("\n")
        
        try:
            option = int(input("Ingrese una opción: "))
        except ValueError:
            print(" Opción inválida. Por favor, ingrese un número.")
            continue

        if option == 1:
            user_session()
        if option == 2:
            register()
        if option == 3:
            print("---------------- Hasta pronto!!! ----------------")
            break
        else:
            print("Opción inválida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    
    login()
    