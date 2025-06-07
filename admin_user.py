def admin_user(user):
    
    while True:
        print(f"----------------- Bienvenido {user["nombre"]} -----------------")
        print("Administrador")
        print("\n")
        print("1 Consultar automatizaciones activas")
        print("2 Gestionar dispositivos")
        print("3 Modificar el rol de un usuario")
        print("4 Salir de la sesion \n")
                
        opcion=int(input("ingrese una opcion: "))
        
        if opcion == 1:
            pass 
        if opcion == 2:
            pass 
        if opcion == 3:
            pass
            
        if opcion == 4:
            break
