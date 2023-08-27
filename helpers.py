import os
import platform
import re

def limpiar_pantalla():
    os.system("cls") if platform.system == "Windows" else os.system("clear")

def leer_texto(longitud_min=0, longitud_max=100, mensaje=None):
    print(mensaje) if mensaje else None
    while True:
        texto = input("> ")
        if len(texto) >= longitud_min and len(texto) <= longitud_max:
            return texto

def validarDni(dni, lista):
    if not re.match('[0-9]{2}[A-Z]$', dni):
        print('Formato de DNI incorrecto')
        return False
    for cliente in lista:
        if cliente.dni == dni:
            print('DNI usado por otro cliente')
            return False
    return True
