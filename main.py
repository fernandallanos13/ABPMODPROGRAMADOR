import usuarios as us
from menu_admin import menu_admin
from menu_usuario import menu_usuario

#TODO: Evaluar dejar limpio el main y hacer un menu de login.

if __name__ == "__main__":
    while True:
        print("\n__ SmartHome Solutions __")
        print("1. Registrarse")
        print("2. Iniciar Sesión")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            us.registrar_usuario()
        elif opcion == '2':
            usuario_actual = us.iniciar_sesion()
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
