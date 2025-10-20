#necesito hacer la conexion con db para traer los dispositivos
devices=None



class Device_manager():

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

    def delete_devices(self,device_name):
     
        if device_name in devices:
            del devices[device_name]
            print(f"Dispositivo '{device_name}' eliminado exitosamente.")
        else:
            print(f"El dispositivo '{device_name}' no fue encontrado.")
    
        self.list_divices()
