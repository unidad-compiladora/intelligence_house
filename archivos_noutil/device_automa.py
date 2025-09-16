from device import dispositivos
from device_fun import cambiar_estado

def automatizar_aire_acondicionado(temp_ambiente, temp_umbral = 28):
    if temp_ambiente > temp_umbral:
        dispositivos["aire acondicionado"]["estado"] = True
        print("El aire acondicionado se ha encendido porque la temperatura supera los 28 °C.")
    elif temp_ambiente <= 22:
        dispositivos["aire acondicionado"]["estado"] = False
        print("El aire acondicionado se ha apagado porque la temperatura ha bajado a 22 °C o menos.")
    else:
        print("El aire acondicionado mantiene su estado actual.")

""" Simulación de temperaturas
temperaturas = [30, 27, 25, 22, 21]
for temp in temperaturas:
    print(f"\nTemperatura ambiente actual: {temp} °C")
    automatizar_aire_acondicionado(temp)
    print(f"Estado actual del aire acondicionado: {dispositivos['aire acondicionado']['estado']}")
"""

# luz automatica
def automatizar_luz(presencia):
    if presencia:
        cambiar_estado("luz", True)
        print("Presencia detectada. Luz encendida.")
    else:
        cambiar_estado("luz", False)
        print("Sin presencia. Luz apagada.")
