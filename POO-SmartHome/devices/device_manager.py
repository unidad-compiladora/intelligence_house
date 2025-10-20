#necesito hacer la conexion con db para traer los dispositivos
devices=None



class Divice_manager():

    def list_divices(self):

        if devices:
            print("Dispositivos disponibles")

            for nombre in devices.keys():
                print(f"  - {nombre} ")
        else:

            print("No hay dispositivos disponibles")

    def search_divices(self,nombre_dispositivo):
            
        self.list_divices()

        if nombre_dispositivo in devices:
       
            return f"el dispositivos{nombre_dispositivo} fue encontrado"
        else:
            return f"el dispositivos{nombre_dispositivo} no fue encontrado"
    
    def add_devices(self,new_devices):
       
        if  new_devices in devices:
            return "ya se encuentra este dispositivo "
        else:
            devices[new_devices]={"datos":"dato"}

        self.list_divices()

    