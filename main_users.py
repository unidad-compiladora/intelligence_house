
def login():
    
    while True:

        print("---------------- Bienvenido a Intelligence house ----------------")
        print("1-  Iniciar sesion ")
        print("2-  Registrarse ")
        print("3-  Cerrar Aplicacion  ")
        print("\n")

        opcion=int(input("Ingrese una opcion: "))

        if opcion == 1:
            admin_user_session()
        if opcion == 2:
            register()
        if opcion == 3:

            print("---------------- Hasto prontos!!! ----------------")

            break

if __name__ == "__main__":
    
    login()