usuarios = []

def registrar_usuario(usuario, email, contraseña, rol=None):
    if rol is None:
        rol = 'admin' if not usuarios else 'general'

    nuevo_usuario = {
        'usuario': usuario,
        'email': email,
        'contraseña': contraseña,
        'rol': rol
    }

    usuarios.append(nuevo_usuario)
    return nuevo_usuario

def iniciar_sesion(usuario, contraseña):
    for u in usuarios:
        if u['usuario'] == usuario and u['contraseña'] == contraseña:
            return u
    return None

def modificar_rol(usuario, nuevo_rol):
    for u in usuarios:
        if u['usuario'] == usuario:
            u['rol'] = nuevo_rol
            return u
    return None

def consultar_datos(usuario_actual):
    for u in usuarios:
        if u['usuario'] == usuario_actual['usuario']:
            return {
                'usuario': u['usuario'],
                'email': u['email'],
                'rol': u['rol']
            }
    return None

def existe_usuario(usuario):
    return any(u['usuario'] == usuario for u in usuarios)

def existe_email(email):
    return any(u['email'] == email for u in usuarios)
