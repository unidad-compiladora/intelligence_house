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
        if mail.lower() == user["mail"].lower():
             user["is_admin"] = True
        if mail.lower() != user["mail"].lower() and user["is_admin"] == True:
             user["is_admin"] = False

def admin_user(user):    
    
    while True:
        print(f"----------------- Bienvenido {user["name"]} -----------------")
        print("Administrador")
        print("\n")
        print("1 Consultar automatizaciones activas")
        print("2 Gestionar dispositivos")
        print("3 Modificar el rol de un usuario")
        print("4 Salir de la sesion \n")
                
        try:
            option = int(input("Ingrese una opción: "))
        except ValueError:
            print("❌ Opción inválida. Por favor, ingrese un número.")
            continue

        if option == 1:
            pass 
        if option == 2:
            pass 
        if option == 3:
            list_user()

            mail=input("ingresar el mail del usaurio: ").strip()
            
            change_role(mail)
            print("Usted ya no es mas Administrador...")
            break
        if option == 4:
            break
