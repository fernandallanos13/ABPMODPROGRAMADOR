import gestion_dispositivos as gd
import gestion_automatizacion as ga
import menu_automatizaciones as ma
from utilidades import limpiar_pantalla

def menu_dispositivos():
    while True:
        print("\n__ Gestión de Dispositivos __")
        print("1. Listar Dispositivos")
        print("2. Buscar Dispositivo")
        print("3. Agregar Dispositivo")
        print("4. Eliminar Dispositivo")
        print("5. Modificar Estado")
        print("6. Automatizaciones")
        print("7. Volver")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            gd.listar_dispositivos()
        elif opcion == '2':
            identificador = input("Nombre del dispositivo: ")
            dispositivo = gd.buscar_dispositivo(identificador)
            if dispositivo:
                for clave, valor in dispositivo.items():
                    print(f"{clave.capitalize()}: {valor}")
            else:
                print("Dispositivo no encontrado.")
        elif opcion == '3':
            gd.agregar_dispositivo()
        elif opcion == '4':
            identificador = input("Nombre del dispositivo: ")
            gd.eliminar_dispositivo(identificador)
        elif opcion == '5':
            identificador = input("Nombre del dispositivo: ")
            estado = input("Nuevo estado (encendido/apagado): ")
            gd.modificar_estado_dispositivo(identificador, estado)
        elif opcion == '6':
            ma.menu_automatizaciones()
        elif opcion == '7':
            break
        else:
            print("Opción inválida.")
