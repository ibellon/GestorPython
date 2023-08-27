import csv
import config

class Cliente:
    def __init__(self, dni, nombre, apellidos) -> None:
        self.dni = dni
        self.nombre = nombre
        self.apellidos = apellidos

    def __str__(self) -> str:
        return f"{self.dni} {self.nombre} {self.apellidos}"
    
class Clientes:
    lista = []
    with open(config.DATABASE_PATH, newline='\n', ) as fichero:
        reader = csv.reader(fichero, delimiter=';')
        for dni, nombre, apellidos in reader:
            cliente = Cliente(dni, nombre, apellidos)
            lista.append(cliente)

    @staticmethod
    def buscar(dni):
        for cliente in Clientes.lista:
            if cliente.dni == dni:
                return cliente
    
    @staticmethod
    def crear(dni, nombre, apellidos):
        cliente = Cliente(dni, nombre, apellidos)
        Clientes.lista.append(cliente)
        Clientes.guardar()
        return cliente
    
    @staticmethod
    def modificar(dni, nombre, apellidos):
        for indice, cliente in enumerate(Clientes.lista):
            if(cliente.dni == dni):
                Clientes.lista[indice].nombre = nombre
                Clientes.lista[indice].apellidos = apellidos
                Clientes.guardar()
                return Clientes.lista[indice]
            
    @staticmethod
    def borrar(dni):
        for indice, cliente in enumerate(Clientes.lista):
            if(cliente.dni == dni):
                cliente = Clientes.lista.pop(indice)
                Clientes.guardar()
                return cliente
            
    @staticmethod
    def guardar():
        with open(config.DATABASE_PATH, 'w', newline='\n') as fichero:
            writer = csv.writer(fichero, delimiter=";")
            for cliente in Clientes.lista:
                writer.writerow([cliente.dni, cliente.nombre, cliente.apellidos])