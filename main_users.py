from auth_system import register,admin_user_session

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
            admin_user_session()
        if option == 2:
            register()
        if option == 3:

            print("---------------- Hasto prontos!!! ----------------")

            break

if __name__ == "__main__":
    
    login()