class DeviceAutomation:
    def automate_ac(self, temperature):
        if temperature > 25:
            return "AC turned on."
        return "AC remains off."

    def automate_light(self, presence):
        if presence:
            return "Light turned on."
        return "Light turned off."
