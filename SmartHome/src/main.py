
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

        

if __name__== "__main__":

    main()