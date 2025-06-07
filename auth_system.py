from users_data_base import users

def register():
    
    name=input("- Ingrese su nombre: ")
    lastname=input("- Ingrese su apellido: ")
    mail=input("- Ingrese su mail: ")
    password=input("- Ingrese una contraseña: ")
    is_admin=False

    if len(users) == 0:
        es_administrador = True


        users.append({
            "name":name,
            "lastname":lastname,
            "mail":mail,
            "password":password,
            "is_admin":is_admin
        })

        

 
    