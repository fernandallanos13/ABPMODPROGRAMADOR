from menus.menu_usuario import registrar_usuario_ui, iniciar_sesion_ui
from menus.menu_admin import menu_admin
from menus.menu_usuario import menu_usuario

if __name__ == "__main__":
    while True:
        print("\n__ SmartHome Solutions __")
        print("1. Registrarse")
        print("2. Iniciar Sesión")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            registrar_usuario_ui()
        elif opcion == '2':
            usuario_actual = iniciar_sesion_ui()
            if usuario_actual:
                if usuario_actual['rol'] == 'admin':
                    menu_admin(usuario_actual)
                else:
                    menu_usuario(usuario_actual)
        elif opcion == '3':
            print("Saliendo del sistema.")
            break
        else:
            print("Opción inválida.")
