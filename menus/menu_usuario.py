import automatizaciones.gestion_automatizacion as ga
import modelos.usuarios as us
import modelos.gestion_dispositivos as gd
import menus.menu_automatizaciones as ma
from utilidades.utilidades import limpiar_pantalla

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


def registrar_usuario_ui():
    print("\n__ Registro de Usuario __")
    while True:
        usuario = input("Ingrese su nombre de usuario: ").strip()
        if not usuario:
            print("¡ATENCIÓN! El nombre de usuario no puede estar vacío.")
            continue
        if us.existe_usuario(usuario):
            print("El nombre de usuario ya está en uso.")
            continue
        break

    while True:
        email = input("Ingrese su correo: ").strip().lower()
        if not email:
            print("El correo no puede estar vacío")
            continue
        if "@" not in email or "." not in email:
            print("El correo debe tener @ y un dominio válido")
            continue
        if us.existe_email(email):
            print("Error: El correo ya está registrado.")
            continue
        break

    while True:
        contraseña = input("Ingrese una contraseña: ").strip()
        if not contraseña:
            print("La contraseña no puede estar vacía.")
            continue
        if len(contraseña) < 6:
            print("La contraseña es demasiado corta. Debe tener al menos 6 caracteres.")
            continue
        confirmar = input("Confirme su contraseña: ").strip()
        if contraseña != confirmar:
            print("Las contraseñas no coinciden.")
            continue
        break

    nuevo_usuario = us.registrar_usuario(usuario, email, contraseña)
    print(f"Usuario registrado exitosamente como '{nuevo_usuario['rol']}'.")

def iniciar_sesion_ui():
    print("\n__ Inicio de Sesión __")
    usuario = input("Usuario: ")
    contraseña = input("Contraseña: ")
    usuario_actual = us.iniciar_sesion(usuario, contraseña)
    if usuario_actual:
        print(f"Bienvenido, {usuario_actual['usuario']} ({usuario_actual['rol']})")
        return usuario_actual
    else:
        print("Credenciales incorrectas.")
        return None

def modificar_rol_ui():
    print("\n__ Modificar Rol de Usuario __")
    usuario = input("Ingrese el nombre de usuario a modificar: ")
    nuevo_rol = input("Nuevo rol (admin/general): ").lower()
    if nuevo_rol not in ['admin', 'general']:
        print("Rol inválido.")
        return
    actualizado = us.modificar_rol(usuario, nuevo_rol)
    if actualizado:
        print(f"Rol actualizado a '{nuevo_rol}'.")
    else:
        print("Usuario no encontrado.")

def consultar_datos_ui(usuario_actual):
    datos = us.obtener_datos(usuario_actual['usuario'])
    if datos:
        print("\n__ Datos Personales __")
        print(f"Nombre: {datos['usuario']}")
        print(f"Email: {datos['email']}")
        print(f"Rol: {datos['rol']}")
    else:
        print("Usuario no encontrado.")