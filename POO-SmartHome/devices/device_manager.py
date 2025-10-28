#from dao.interfaces.devices_dao import Devices_dao
from db.connection import DataBase



class Device_manager():

    db=DataBase()

    def __init__(self):
        self.conn=self.db.connect()


    def get_by_id(self, id):
        
        cursor=self.conn.cursor()
        query="SELECT * FROM Devices WHERE device_id = %s"
        cursor.execute(query,(id,))
        device=cursor.fetchone()        

        if device is not None:   
            print(f"device:{device[2]}")
        else: 
            print("este dispositivo no esta en nuestra base de datos")

        cursor.close()
        

    def get_all(self):



        cursor=self.conn.cursor()
        cursor.execute("SELECT * FROM Devices")
        resultado = cursor.fetchall()

        if device is not None:
            for device in resultado:
                print(f"{device[0]}device:{ device[2]}")
        else: 
            print("vacio")

        cursor.close()

    
    def update(self, id, data):

        pass
    

    def delete_by_id(self, id):

        cursor=self.conn.cursor()
        query="DELETE FROM Devices WHERE device_id = %s"
        cursor.execute(query,(id,))

        self.conn.commit()

        cursor.close()

    def post(self,data):
        pass
    
    db.close()


   
    # def add_devices(self,new_devices):
       
    #     if  new_devices in devices:
    #         return "ya se encuentra este dispositivo "
    #     else:
    #         devices[new_devices]={"datos":"dato"}

    #     self.list_devices()


    # def set_status_devices(self,name,new_state=False):
    #     if name in devices:
    #         devices[name]["estado"] = new_state
    #         print(f"'{name}' ahora está {'encendido' if new_state else 'apagado'}.")
    #     else:
    #         print(f"Dispositivo '{name}' no encontrado.")

    
    
    # def update_devices(self,name,**kwargs):
    #     if name in devices:
    #         devices[name].update(kwargs)
    #         print(f"'{name}' actualizado con exito")
    #     else:
    #         print(f"Dispositivo '{name}' no encontrado.")

    # def get_status_devices(name):
    #     if name in devices:
    #         print(f"Estado de '{name}':")
    #         for atribute, value in devices[name].items():
    #             print(f"  {atribute}: {value}")
    #     else:
    #         print(f"Dispositivo '{name}' no encontrado.")


device=Device_manager()
device.get_by_id(1)
