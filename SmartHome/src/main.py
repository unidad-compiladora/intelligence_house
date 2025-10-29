
def main():

    while True:

        print("--- Bienvenido a Smart Home--- ")

        print("1- Iniciar Sesion ")
        print("2- Registrarse ")
        print("3- Salir")

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
            pass

        if opcion == 3:

            break

if __name__== "__main__":

    main()