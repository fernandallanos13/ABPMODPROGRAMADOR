import gestion_automatizacion as ga
import usuarios as us
import gestion_dispositivos as gd
import menu_automatizaciones as ma
from utilidades import limpiar_pantalla

def menu_usuario(usuario_actual):
    while True:
        print("\n__ Menú Usuario __")
        print("1. Consultar Datos Personales")
        print("2. Ejecutar Automatizacion")
        print("3. Consultar Dispositivos")
        print("4. Cerrar Sesión")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            limpiar_pantalla()
            us.consultar_datos(usuario_actual)
        elif opcion == '2':
            limpiar_pantalla()
            ma.menu_automatizaciones()
        elif opcion == '3':
            limpiar_pantalla()
            gd.listar_dispositivos()
        elif opcion == '4':
            limpiar_pantalla()
            break
        else:
            print("Opción inválida.")
