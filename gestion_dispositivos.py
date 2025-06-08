import uuid

dispositivos = []

def listar_dispositivos():
    """lista de los dispositivos"""
    if not dispositivos:
        print("no hay dispositivos registrados")
        return
    print("\n__Dispositivos registrados__")
    for dispositivo in dispositivos:
        print(f"Nombre: {dispositivo['nombre']}")
        print(f"Tipo: {dispositivo['tipo']}")
        print(f"Estado: {dispositivo['estado']}")
        print("-" * 20)

def buscar_dispositivo(identificador):
    """Busca un dispositivo por su Nombre."""
    for dispositivo in dispositivos:
        if dispositivo['nombre'] == identificador:
            return dispositivo
    return None

def agregar_dispositivo():
    """Agrega un nuevo dispositivo."""
    print("\n__ Agregar Nuevo Dispositivo __")
    tipo = input("Ingrese el tipo de dispositivo (luz, camara, electrodomestico, alarma, etc.): ").lower()
    estado = input("Ingrese el estado inicial (encendido/apagado): ").lower()
    nombre = input("Ingrese el nombre del dispositivo: ")

    # Validación de nombre duplicado
    if buscar_dispositivo(nombre):
        print(f"Error: Ya existe un dispositivo con nombre '{nombre}'")
        return

    # Validación de estado
    if estado not in ['encendido', 'apagado']:
        print("Error: El estado debe ser 'encendido' o 'apagado'")
        return

    # Crear un ID único
    dispositivo_id = str(uuid.uuid4())

    nuevo_dispositivo = {
        "id": dispositivo_id,  
        "nombre": nombre,
        "tipo": tipo,
        "estado": estado
    }

    dispositivos.append(nuevo_dispositivo)
    print(f"Dispositivo '{nombre}' agregado exitosamente.")

def eliminar_dispositivo(identificador):
    """Elimina un dispositivo por su nombre."""
    dispositivo_encontrado = buscar_dispositivo(identificador)
    if dispositivo_encontrado:
        dispositivos.remove(dispositivo_encontrado)
        print(f"Dispositivo con nombre '{identificador}' eliminado.")
    else:
        print(f"No se encontró ningún dispositivo con nombre '{identificador}'.")

def modificar_estado_dispositivo(identificador, nuevo_estado):
    """Modifica el estado de un dispositivo."""
    dispositivo = buscar_dispositivo(identificador)
    if dispositivo:
        # Validación de estado aquí también
        if nuevo_estado.lower() not in ['encendido', 'apagado']:
            print("Error: El estado debe ser 'encendido' o 'apagado'")
            return
        dispositivo['estado'] = nuevo_estado.lower()
        print(f"Estado del dispositivo '{identificador}' modificado a '{nuevo_estado}'.")
    else:
        print(f"No se encontró ningún dispositivo con nombre '{identificador}'.")