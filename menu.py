class Cliente:
    def __init__(self, dni, nombre, apellidos) -> None:
        self.dni = dni
        self.nombre = nombre
        self.apellidos = apellidos

    def __str__(self) -> str:
        return f"{self.dni} {self.nombre} {self.apellidos}"
    
class Clientes:
    lista = []

    @staticmethod
    def buscar(dni):
        for cliente in Clientes.lista:
            if cliente.dni == dni:
                return cliente
    
    @staticmethod
    def crear(dni, nombre, apellidos):
        cliente = Cliente(dni, nombre, apellidos)
        Clientes.lista.append(cliente)
        return cliente
    
    @staticmethod
    def modificar(dni, nombre, apellidos):
        for indice, cliente in enumerate(Clientes.lista):
            if(cliente.dni == dni):
                Clientes.lista[indice].nombre = nombre
                Clientes.lista[indice].apellidos = apellidos
                return Clientes.lista[indice]
            
    @staticmethod
    def borrar(dni):
        for indice, cliente in enumerate(Clientes.lista):
            if(cliente.dni == dni):
                return Clientes.lista.pop(indice)