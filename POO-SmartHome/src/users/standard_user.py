from users.user import User

class StandardUser(User):
    def __init__(self, name, lastname, mail, password):
        super().__init__(name, lastname, mail, password, False)

    def view_device(self, device_name):
        return f"User {self.get_name()} is viewing {device_name}."

    def run_automation(self, automation_name):
        return f"User {self.get_name()} executed {automation_name} automation."
