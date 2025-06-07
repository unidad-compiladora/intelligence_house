from users_data_base import users
from admin_user import admin_user
from standard_user import standard_user

def register():
    
    name=input("- Ingrese su nombre: ")
    lastname=input("- Ingrese su apellido: ")
    mail=input("- Ingrese su mail: ")
    password=input("- Ingrese una contraseña: ")
    is_admin=False

    if len(users) == 0:
        is_admin= True


    if authentication(mail) :
        
        print("El usuario ya esta registrado")

       
    else:
        
        print(f"Usuario registrado, Bienvenido {name} ")
       
        users.append({
            "name":name,
            "lastname":lastname,
            "mail":mail,
            "password":password,
            "is_admin":is_admin
        })
      
def authentication(mail):

    for user in users:
        if mail == user["email"]:
           
                return True
            
    return False

        
def admin_user_session():
      while True:

        mail=input("ingrese su mail: ")
        password=input("ingrese su contraseña: ")

        for user in users:

            if mail == user["email"] and password == user["password"]:

                if user["es_admin"] :

                    return admin_user(user)
                else:

                    return standard_user(user)
                
        else:
            print(" Usuario o contraseña incorrecta, vuelva antentarlo ")


        

 
    