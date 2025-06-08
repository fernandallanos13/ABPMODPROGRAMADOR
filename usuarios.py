usuarios = []

def registrar_usuario():
    print("\n__ Registro de Usuario __")
    #Aca pedias los datos de inicio y luego chequeabas si estaban correctos, es mejor si a medida que completa
    #chequeamos los datos, cosa de no tener que repetir todo si ingresas mal algo.
    while True:
        usuario = input("Ingrese su nombre de usuario: ").strip()
         #cambie el if usuario == '' por el if not, si no es un valor entonces:
        if not usuario:
            print("¡ATENCIÓN! El nombre de usuario no puede estar vacío.")
            continue
        if any(u['usuario'] == usuario for u in usuarios):
            print("El nombre de usuario ya está en uso.")
            #usamos un continue antes del break, por si tenemos problemas con el usuario, tambien chequeamos que no exista
            # el mismo nombre de usuario
            continue
        break
         
    while True:
        #aca pedias usuario nuevamente, necesitariamos el campo email
        email = input("Ingrese su correo: ").strip().lower()
        if not email:
            print("El correo no puede estar vacio")
            continue
        if "@" not in email or "." not in email: 
            print("El correo debe tener @ y un dominio válido")
            continue
        if any(e['email'] == email for e in usuarios):
            print("Error: El correo utilizado ya se encuentra registrado.")
            continue
        break
    
    while True: 
        contraseña = input("Ingrese una contraseña: ").strip()
        if not contraseña:
            print("La contraseña no puede estar vacía.")
            continue
        if len(contraseña) < 6: 
            print("La contraseña es demasiado corta. Debe contener más de 6 caracteres. ")
            continue
        confirmar = input("Confirme su contraseña: ").strip()
        if contraseña != confirmar:
            print("Las contraseñas no coinciden.")
            continue
        break
    
    
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
