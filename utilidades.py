#Este codigo lo que hace es ir limpiando la terminal, es para que sea mas legible al usarla!!!!
import os

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')
