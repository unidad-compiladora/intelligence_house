from device_automa import automatizar_aire_acondicionado, automatizar_luz

def mostrar_menu_automatizacion():
    while True:
        print("\n--- Menú de Automatización ---")
        print("1. Automatizar Aire Acondicionado")
        print("2. Automatizar Luz")
        print("3. Volver al menú anterior")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            try:
                temp = float(input("Ingrese la temperatura ambiente actual (°C): "))
                automatizar_aire_acondicionado(temp)
            except ValueError:
                print("Entrada inválida. Por favor ingrese un número válido.")
        elif opcion == "2":
            presencia = input("¿Hay presencia? (s/n): ").strip().lower() == "s"
            automatizar_luz(presencia)
        elif opcion == "3":
            break
        else:
            print("Opción inválida. Intente de nuevo.")
