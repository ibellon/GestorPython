import unittest
import database as db
import copy

class TestDatabase(unittest.TestCase):

    def setUp(self):
        db.Clientes.lista = [
            db.Cliente('10A', 'Manolo', 'López Maroto'),
            db.Cliente('21B', 'Alicia', 'Pérez García'),
            db.Cliente('31C', 'Rigoberto', 'Sánchez Patón')
        ]
    def test_buscar_cliente(self):
        cliente_existente = db.Clientes.buscar("21B")
        cliente_inexistente = db.Clientes.buscar("11V")
        self.assertIsNotNone(cliente_existente)
        self.assertIsNone(cliente_inexistente)

    def test_crear_cliente(self):
        nuevo_cliente = db.Clientes.crear('99Y', 'Isidro', 'Bellón Cano')
        self.assertEqual(len(db.Clientes.lista), 4)
        self.assertEqual(nuevo_cliente.dni, "99Y")
        self.assertEqual(nuevo_cliente.nombre, "Isidro")
        self.assertEqual(nuevo_cliente.apellidos, "Bellón Cano")

    def test_modificar_cliente(self):
        cliente_modificar = copy.copy(db.Clientes.buscar('21B'))
        cliente_modificaddo = db.Clientes.modificar('21B', 'Paula', 'García Nieto')
        self.assertEqual(cliente_modificar.nombre, "Alicia")
        self.assertEqual(cliente_modificaddo.nombre, "Paula")
    
    def test_borrar_cliente(self):
        cliente_borrado = db.Clientes.borrar('10A')
        cliente_rebuscado = db.Clientes.buscar('10A')
        self.assertEqual(cliente_borrado.dni, "10A")
        self.assertIsNone(cliente_rebuscado)