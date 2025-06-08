import gestion_automatizacion as ga
import usuarios as us
import gestion_dispositivos as gd
from utilidades import limpiar_pantalla

#TODO: Cambiar ejecuciones de modo noche y seguridad por 1 sola opcion. Ejecutar/Configurar Automatizaciones. Que esten deshabilitadas de Inicio
def menu_usuario(usuario_actual):
    while True:
        print("\n__ Menú Usuario __")
        print("1. Consultar Datos Personales")
        print("2. Ejecutar Modo Noche")
        print("3. Ejecutar Modo Seguridad")
        print("4. Consultar Dispositivos")
        print("5. Cerrar Sesión")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            limpiar_pantalla()
            us.consultar_datos(usuario_actual)
        elif opcion == '2':
            limpiar_pantalla()
            ga.automatizacion_modo_noche()
        elif opcion == '3':
            limpiar_pantalla()
            ga.automatizacion_modo_seguridad()
        elif opcion == '4':
            limpiar_pantalla()
            gd.listar_dispositivos()
        elif opcion == '5':
            limpiar_pantalla()
            break
        else:
            print("Opción inválida.")
