from users_data_base import users 
def list_user():
    for user in users:
        rol="Administrador" if user["is_admin"] else "Usuario"
                    
        print("---------------------------------------------------------")

        print(f"- nombre : {user["name"]}")
        print(f"- apellido: {user["lastname"]}")
        print(f"- email: {user['mail']}" )
        print(f"- rol: {rol}\n")

def change_role(mail):
   for user in users:
        if mail == user["mail"]:
             user["is_admin"] = True
        if mail != user["mail"] and user["is_admin"] == True:
             user["is_admin"] = False






def admin_user(user):
    
    while True:
        print(f"----------------- Bienvenido {user["nombre"]} -----------------")
        print("Administrador")
        print("\n")
        print("1 Consultar automatizaciones activas")
        print("2 Gestionar dispositivos")
        print("3 Modificar el rol de un usuario")
        print("4 Salir de la sesion \n")
                
        option=int(input("ingrese una opcion: "))
        
        if option == 1:
            pass 
        if option == 2:
            pass 
        if option == 3:
            list_user()

            mail=input("ingresar el mail del usaurio: ")
            
            change_role(mail)
            print("Usted ya no es mas Administrador...")
            break
        if option == 4:
            break
