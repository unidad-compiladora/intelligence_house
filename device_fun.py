from device import dispositivos

def listar_dispositivos():

    if dispositivos:

        print("Dispositivos disponibles: ")

        for nombre in dispositivos.keys():
            print(f"  - {nombre} ")

    else:

        print("No hay dispositivos disponibles")


def buscar_dispositivos(nombre_dispositivo):
    listar_dispositivos()
    if nombre_dispositivo in dispositivos:
       
       return f"el dispositivos{nombre_dispositivo} fue encontrado"
    else:
        return f"el dispositivos{nombre_dispositivo} no fue encontrado"
    
    
def agregar_dispositivos(nuevo_dispositivo):

    if  nuevo_dispositivo in dispositivos:
       return "ya se encuentra este dispositivo "
    else:
        dispositivos[nuevo_dispositivo]={"datos":"dato"}

    listar_dispositivos()

    

def eliminar_dispositivos(dispositivo_eliminado):
     
    if dispositivo_eliminado in dispositivos:
        del dispositivos[dispositivo_eliminado]
        print(f"Dispositivo '{dispositivo_eliminado}' eliminado exitosamente.")
    else:
        print(f"El dispositivo '{dispositivo_eliminado}' no fue encontrado.")
    
    listar_dispositivos()

def cambiar_estado(nombre, nuevo_estado=False):
    if nombre in dispositivos:
        dispositivos[nombre]["estado"] = nuevo_estado
        print(f"'{nombre}' ahora está {'encendido' if nuevo_estado else 'apagado'}.")
    else:
        print(f"Dispositivo '{nombre}' no encontrado.")

def modificar_dispositivo(nombre,**kwargs):
    if nombre in dispositivos:
        dispositivos[nombre].update(kwargs)
        print(f"'{nombre}' actualizado con exito")
    else:
        print(f"Dispositivo '{nombre}' no encontrado.")

def consultar_estado(nombre):
    if nombre in dispositivos:
        print(f"Estado de '{nombre}':")
        for clave, valor in dispositivos[nombre].items():
            print(f"  {clave}: {valor}")
    else:
        print(f"Dispositivo '{nombre}' no encontrado.")