import gestion_dispositivos as gd
import gestion_automatizacion as gs

def mostrar_menu():
    """Muestra el menú principal."""
    print("\n__ SmartHome Solutions __")
    print("1. Gestionar Dispositivos")
    print("2. Salir")


def menu_dispositivos():
    """Muestra el menú de gestión de dispositivos."""
    while True:
        print("\n__ Gestión de Dispositivos __")
        print("1. Listar Dispositivos")
        print("2. Buscar Dispositivo")
        print("3. Agregar Dispositivo")
        print("4. Eliminar Dispositivo")
        print("5. Modificar Estado")
        print("6. Activar modo noche")
        print("7. Activar modo seguridad")
        print("8. Volver al Menú Principal")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            gd.listar_dispositivos()
        elif opcion == '2':
            identificador = input("Ingrese el nombre del dispositivo a buscar: ")
            dispositivo = gd.buscar_dispositivo(identificador)
            if dispositivo:
                print("Dispositivo encontrado:")
                for clave, valor in dispositivo.items():
                    print(f"{clave.capitalize()}: {valor}")
            else:
                print(f"No se encontró ningún dispositivo con el nombre '{identificador}'.")
        elif opcion == '3':
            gd.agregar_dispositivo()
        elif opcion == '4':
            identificador = input("Ingrese el nombre del dispositivo a eliminar: ")
            gd.eliminar_dispositivo(identificador)
        elif opcion == '5':
            identificador = input("Ingrese el nombre del dispositivo a modificar: ")
            nuevo_estado = input("Ingrese el nuevo estado (encendido/apagado): ")
            gd.modificar_estado_dispositivo(identificador, nuevo_estado)
        elif opcion == '6':
            gs.automatizacion_modo_noche()
            gd.listar_dispositivos()
            
        elif opcion == '7':
            gs.automatizacion_modo_seguridad()
            
        elif opcion == '8':
            break
        else:
            print("Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    while True:
        mostrar_menu()
        opcion_principal = input("Seleccione una opción del menú principal: ")
        if opcion_principal == '1':
            menu_dispositivos()
        elif opcion_principal == '2':
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Intente nuevamente.")