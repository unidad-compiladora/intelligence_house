from users.user import User

class AdminUser(User):
    def __init__(self, name, lastname, mail, password):
        super().__init__(name, lastname, mail, password, True)  # siempre admin

    # Método propio del admin
    def manage_system(self):
        return f"Admin {self.get_name()} is managing the system."

    # Podés añadir métodos extra relacionados con rol
    def change_user_role(self, user, is_admin=True):
        user.set_is_admin(is_admin)
        return f"User {user.get_name()} role updated to {'Admin' if is_admin else 'Standard'}."
