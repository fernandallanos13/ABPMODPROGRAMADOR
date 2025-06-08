usuarios = []

def registrar_usuario():
    #TODO: Hacer chequeos de usuario, contraseña y agregar correo. Gracias
    print("\n__ Registro de Usuario __")
    usuario = input("Ingrese su nombre de usuario: ")
    email = input("Ingrese su correo: ")
    contraseña = input("Ingrese una contraseña: ")

    if any(e['email'] == email for e in usuarios):
        print("Error: El correo utilizado ya se encuentra registrado.")
        return

    # Si es el primer usuario, se convierte en admin
    rol = 'admin' if not usuarios else 'general'

    nuevo_usuario = {
        'usuario': usuario,
        'email': email,
        'contraseña': contraseña,
        'rol': rol
    }

    usuarios.append(nuevo_usuario)
    print(f"Usuario registrado exitosamente como '{rol}'.")

def iniciar_sesion():
    print("\n__ Inicio de Sesión __")
    usuario = input("Usuario: ")
    contraseña = input("Contraseña: ")

    for u in usuarios:
        if u['usuario'] == usuario and u['contraseña'] == contraseña:
            print(f"Bienvenido, {u['usuario']} ({u['rol']})")
            return u

    print("Credenciales incorrectas.")
    return None

def modificar_rol():
    print("\n__ Modificar Rol de Usuario __")
    usuario = input("Ingrese el nombre de usuario a modificar: ")
    for u in usuarios:
        if u['usuario'] == usuario:
            nuevo_rol = input("Nuevo rol (admin/general): ").lower()
            if nuevo_rol in ['admin', 'general']:
                u['rol'] = nuevo_rol
                print(f"Rol actualizado a '{nuevo_rol}'.")
            else:
                print("Rol inválido.")
            return
    print("Usuario no encontrado.")

def consultar_datos(usuario_actual):
    print("\n__ Datos Personales __")
    print(f"Nombre: {usuario_actual['usuario']}")
    print(f"Email: {usuario_actual['email']}")
    print(f"Rol: {usuario_actual['rol']}")
