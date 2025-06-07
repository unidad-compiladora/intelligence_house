from users_data_base import users

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
        
        


        

 
    