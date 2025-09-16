from users_data_base import users
from admin_user import admin_user
from standard_user import standard_user

def register():
    name = input("- Ingrese su nombre: ").strip()
    lastname = input("- Ingrese su apellido: ").strip()
    mail = input("- Ingrese su mail: ").strip().lower()
    password = input("- Ingrese una contraseña: ").strip()
    is_admin = False

    is_admin = len(users) == 0  # Primer usuario es admin

    if authentication(mail):
        print("El usuario ya está registrado")
        return

    print(f"Usuario registrado, Bienvenido {name}")
    users.append({
        "name": name,
        "lastname": lastname,
        "mail": mail,
        "password": password,
        "is_admin": is_admin
    })

def authentication(mail):
    for user in users:
        if mail == user["mail"].lower():
            return True
    return False

def user_session():
    while True:
        mail = input("Ingrese su mail: ").strip().lower()
        password = input("Ingrese su contraseña: ").strip()

        for user in users:
            if mail == user["mail"].lower() and password == user["password"]:
                if user["is_admin"]:
                    admin_user(user)
                else:
                    standard_user(user)
                return True
        else:
            print("Usuario o contraseña incorrecta, vuelva a intentarlo")
