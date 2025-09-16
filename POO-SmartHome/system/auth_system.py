class AuthSystem:
    def __init__(self):
        self.__users = []

    def register(self, user):
        self.__users.append(user)
        return "User registered."

    def authenticate(self, mail, password):
        for user in self.__users:
            if user.get_mail() == mail and user.get_password() == password:
                return True
        return False

    def user_session(self, user):
        return f"Session started for {user.get_name()}."
