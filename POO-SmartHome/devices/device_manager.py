#necesito hacer la conexion con db para traer los dispositivos
dispositivos=None



class Divice_manager():

    def list_divices(self):

        if dispositivos:
            print("Dispositivos disponibles")

            for nombre in dispositivos.keys():
                print(f"  - {nombre} ")
        else:

            print("No hay dispositivos disponibles")

    def search_divices(self,nombre_dispositivo):
            
        self.list_divices()

        if nombre_dispositivo in dispositivos:
       
            return f"el dispositivos{nombre_dispositivo} fue encontrado"
        else:
            return f"el dispositivos{nombre_dispositivo} no fue encontrado"
    
   