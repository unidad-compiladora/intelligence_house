from dao.interfaces.devices_dao import Devices_dao

#necesito hacer la conexion con db para traer los dispositivos
devices=None



class Device_manager(Devices_dao):

    def list_devices(self):

        if devices:
            print("Dispositivos disponibles")

            for name in devices.keys():
                print(f"  - {name} ")
        else:

            print("No hay dispositivos disponibles")

    def search_devices(self,nombre_dispositivo):
            
        self.list_devices()

        if nombre_dispositivo in devices:
       
            return f"el dispositivos{nombre_dispositivo} fue encontrado"
        else:
            return f"el dispositivos{nombre_dispositivo} no fue encontrado"
    
    def add_devices(self,new_devices):
       
        if  new_devices in devices:
            return "ya se encuentra este dispositivo "
        else:
            devices[new_devices]={"datos":"dato"}

        self.list_devices()

    def delete_devices(self,device_name):
     
        if device_name in devices:
            del devices[device_name]
            print(f"Dispositivo '{device_name}' eliminado exitosamente.")
        else:
            print(f"El dispositivo '{device_name}' no fue encontrado.")
    
        self.list_devices()

    def set_status_devices(self,name,new_state=False):
        if name in devices:
            devices[name]["estado"] = new_state
            print(f"'{name}' ahora está {'encendido' if new_state else 'apagado'}.")
        else:
            print(f"Dispositivo '{name}' no encontrado.")

    
    
    def update_devices(self,name,**kwargs):
        if name in devices:
            devices[name].update(kwargs)
            print(f"'{name}' actualizado con exito")
        else:
            print(f"Dispositivo '{name}' no encontrado.")

    def get_status_devices(name):
        if name in devices:
            print(f"Estado de '{name}':")
            for atribute, value in devices[name].items():
                print(f"  {atribute}: {value}")
        else:
            print(f"Dispositivo '{name}' no encontrado.")
