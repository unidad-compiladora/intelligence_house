from device_fun import listar_dispositivos

def standard_user(user):
   
    while True:
        print("\n")
        print(f"----------------- Bienvenido {user["nombre"]} -----------------")
        print("Usuario")
        print("1 Datos Personales")
        print("2 Control dispositivos")
        print("3 Dispositivos disponibles")
        print("4 Salir Sesion\n")
        
        option=int(input("ingrese una opcion: "))
                
        try:
            option = int(input("Ingrese una opción: "))
        except ValueError:
            print("Opción inválida. Por favor, ingrese un número.")
            continue


        if option== 1:
           
                    rol="Administrador" if user["is_admin"] else "Usuario"

                    print("-------------------- Datos personales--------------------")

                    print(f"- nombre : {user["nombre"]}")
                    print(f"- apellido: {user["apellido"]}")
                    print(f"- email: {user['email']}" )
                    print(f"- rol:{rol}")
                    
                    
                    print("---------------------------------------------------------")
                 

        if option == 2:
            pass

        if option == 3:
            listar_dispositivos()
        if option == 4:
            break


        