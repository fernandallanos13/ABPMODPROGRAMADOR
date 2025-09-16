import modelos.usuarios as us
from menus.menu_dispositivos import menu_dispositivos
from automatizaciones.gestion_automatizacion import listar_automatizaciones
from utilidades.utilidades import limpiar_pantalla

def menu_admin(usuario_actual):
    while True:
        print("\n__ Menú Administrador __")
        print("-"*20)
        print("1. Consultar Automatizaciones")
        print("2. Gestionar Dispositivos")
        print("3. Modificar Rol de Usuario")
        print("4. Cerrar Sesión")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            limpiar_pantalla()
            listar_automatizaciones()
        elif opcion == '2':
            limpiar_pantalla()
            menu_dispositivos()
        elif opcion == '3':
            limpiar_pantalla()
            us.modificar_rol()
        elif opcion == '4':
            limpiar_pantalla()
            break
        else:
            print("Opción inválida.")
