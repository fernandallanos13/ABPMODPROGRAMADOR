from modelos.gestion_dispositivos import dispositivos

estado_automatizaciones = {
    'Modo Noche': {'estado': 'No ejecutada'},
    'Modo Seguridad': {'estado': 'No ejecutada'}
}

def automatizacion_modo_noche():
    """Automatización: Enciende todas las luces apagadas para el modo noche."""
    print("\n__Automatización: Modo Noche __")
    luces_encendidas = 0
    
    for dispositivo in dispositivos: 
        if dispositivo['tipo'] == 'luz' and dispositivo['estado'] == 'apagado':
            dispositivo['estado'] = 'encendido'
            print(f"La luz '{dispositivo['nombre']}' fue encendida automáticamente")
            luces_encendidas += 1
    
    if luces_encendidas == 0:
        print("No hay luces apagadas para encender o no hay luces registradas.")
    else:
        print(f"Modo noche activado: {luces_encendidas} luces encendidas.")
        estado_automatizaciones['Modo Noche']['estado'] = 'Ejecutado'

def automatizacion_modo_seguridad():
    """Automatización: Enciende todas las cámaras y alarmas para el modo seguridad."""
    print("\n__Automatización: Modo Seguridad __")
    camaras_activadas = 0
    alarmas_activadas = 0
    
    for dispositivo in dispositivos:
        if dispositivo['tipo'] == 'camara' and dispositivo['estado'] == 'apagado':
            dispositivo['estado'] = 'encendido'
            print(f"La cámara '{dispositivo['nombre']}' fue activada automáticamente")
            camaras_activadas += 1
        elif dispositivo['tipo'] == 'alarma' and dispositivo['estado'] == 'apagado':
            dispositivo['estado'] = 'encendido'
            print(f"La alarma '{dispositivo['nombre']}' fue activada automáticamente")
            alarmas_activadas += 1
    
    total_activados = camaras_activadas + alarmas_activadas
    
    if total_activados == 0:
        print("No hay cámaras o alarmas apagadas para activar, o no hay dispositivos de seguridad registrados.")
    else:
        print(f"Modo seguridad activado: {camaras_activadas} cámaras y {alarmas_activadas} alarmas activadas.")
        estado_automatizaciones['Modo Seguridad']['estado'] = 'Ejecutado'

def listar_automatizaciones():
        print("\n__ Automatizaciones Disponibles __")
        for nombre, automatizaciones in estado_automatizaciones.items():
            print(f"- {nombre}:")
            print(f"  Estado: {automatizaciones['estado']}")