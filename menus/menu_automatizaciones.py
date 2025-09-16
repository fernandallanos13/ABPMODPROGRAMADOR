import automatizaciones.gestion_automatizacion as ga
from utilidades.utilidades import limpiar_pantalla

def menu_automatizaciones():
    while True:
        print("\n__ Ejecutar Automatizaciones __")
        print("1. Ejecutar Modo Noche")
        print("2. Ejecutar Modo Seguridad")
        print("3. Volver al Menú Principal")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            limpiar_pantalla()
            ga.automatizacion_modo_noche()
        elif opcion == '2':
            limpiar_pantalla()
            ga.automatizacion_modo_seguridad()
        elif opcion == '3':
            limpiar_pantalla()
            break
        else:
            print("Opción inválida.")