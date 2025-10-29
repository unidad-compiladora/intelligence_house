class User:
    def __init__(self, name, lastname, mail, password, is_admin=False):
        self.__name = name
        self.__lastname = lastname
        self.__mail = mail
        self.__password = password
        self.__is_admin = is_admin

    # Getters
    def get_name(self): return self.__name
    def get_lastname(self): return self.__lastname
    def get_mail(self): return self.__mail
    def get_password(self): return self.__password
    def get_is_admin(self): return self.__is_admin

    # Setters
    def set_name(self, name): self.__name = name
    def set_lastname(self, lastname): self.__lastname = lastname
    def set_mail(self, mail): self.__mail = mail
    def set_password(self, password): self.__password = password
    def set_is_admin(self, is_admin): self.__is_admin = is_admin

    # Métodos públicos
    def register(self):
        return f"User {self.__name} registered successfully."

    def login(self, mail, password):
        return self.__mail == mail and self.__password == password
