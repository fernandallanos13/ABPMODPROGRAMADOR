dispositivos = []
contador_id=0 

def listar_dispositivos ():
    """lista de los dispositivos"""

    if not dispositivos:
        print("no hay dispositivos registrados")
        return
    print("\n__Dispositivos registrados__")
    for dispositivo in dispositivos:
        print(f"ID: {dispositivo ['id']}| Tipo: {dispositivo['tipo']}| Estado: {dispositivo['estado']}")


def buscar_dispositivo(identificador):
    """Busca un dispositivo por su ID."""
    for dispositivo in dispositivos:
        if dispositivo['id'] == identificador:
            return dispositivo
    return None


def agregar_dispositivo():
    """Agrega un nuevo dispositivo."""
    global contador_id
    print("\n__ Agregar Nuevo Dispositivo __")
    while True:
        nombre = input("Ingrese un nombre para el dispositivo:").lower()
        tipo = input("Ingrese el tipo de dispositivo (luz, cámara, electrodoméstico, etc.): ").lower()
        estado = input("Ingrese el estado inicial (encendido/apagado): ").lower()
        if estado in["encendido", "apagado"]:
            break
        else:
            print("Estado inválido. Escriba 'encendido' o 'apagado'")
            estado = input("Ingrese el estado inicial (encendido/apagado): ").lower()
            break
                      
    contador_id += 1 
    nuevo_id = str(contador_id)

    nuevo_dispositivo = {
        'id': nuevo_id,
        'nombre': nombre, 
        'tipo': tipo,
        'estado': estado
    }

    dispositivos.append(nuevo_dispositivo)
    print(f"Dispositivo '{nuevo_id}' agregado exitosamente.")


def eliminar_dispositivo(identificador):
    """Elimina un dispositivo por su ID."""
    dispositivo_encontrado = buscar_dispositivo(identificador)
    if dispositivo_encontrado:
        dispositivos.remove(dispositivo_encontrado)
        print(f"Dispositivo con ID '{identificador}' eliminado.")
    else:
        print(f"No se encontró ningún dispositivo con ID '{identificador}'.")



def modificar_estado_dispositivo(identificador, nuevo_estado):
    """Modifica el estado de un dispositivo."""
    dispositivo = buscar_dispositivo(identificador)
    if dispositivo:
        dispositivo['estado'] = nuevo_estado.lower()
        print(f"Estado del dispositivo '{identificador}' modificado a '{nuevo_estado}'.")
    else:
        print(f"No se encontró ningún dispositivo con ID '{identificador}'.")

def automatizacion_modo_noche():
    print("\n__Automatización: Modo Noche __")
    for dispositivo in dispositivos: 
        if dispositivo ['tipo'] == 'luz' and dispositivo ['estado'] == 'apagado':
            dispositivo ['estado'] = 'encendido'
            print(f"La luz con ID {dispositivo ['id']}, {dispositivo ['nombre']}, fue encendida automáticamente")
            print(f"{dispositivo['id']}, {dispositivo['nombre']}, {dispositivo['estado']}")

