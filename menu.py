import os
import helpers
import database as db

def iniciar():
    while True:
        
        helpers.limpiar_pantalla()

        print("========================")
        print("  Bienvenido al Gestor  ")
        print("========================")
        print("[1] Listar los Clientes ")
        print("[2] Buscar un Cliente   ")
        print("[3] Crear un Cliente    ")
        print("[4] Modificar un Cliente")
        print("[5] Borrar un Cliente   ")
        print("[6] Cerrar el Gestor    ")
        print("========================")

        opcion = input("> ")
        helpers.limpiar_pantalla()

        if(opcion == '1'):
            print("Listando los Clientes...\n")
            for cliente in db.Clientes.lista:
                print(cliente)

        elif(opcion == '2'):
            print("Buscar un Cliente...\n")
            dni = helpers.leer_texto(3, 3, "DNI(2 números y una letra). ").upper()
            cliente = db.Clientes.buscar(dni)
            print(cliente) if cliente else print("Cliente no encontrado.")

        elif(opcion == '3'):
            print("Crear un Cliente...\n")
            dni = None
            while True:
                dni = helpers.leer_texto(3, 3, "DNI(2 números y una letra) ").upper()
                if(helpers.validarDni(dni, db.Clientes.lista)):
                    break

            nombre = helpers.leer_texto(2, 30, "Nombre(de 2 hasta 30 caracteres) ")
            apellidos = helpers.leer_texto(2, 70, "Apellidos(de 2 hasta 70 caracteres) ")
            db.Clientes.crear(dni, nombre, apellidos)
            print("Cliente añadido correctamente.")

        elif(opcion == '4'):
            print("Modificar un Cliente...\n")
            dni = helpers.leer_texto(3, 3, "DNI(2 números y una letra). ").upper()
            cliente = db.Clientes.buscar(dni)
            if cliente:
                nombre = helpers.leer_texto(
                    2, 30, f"Nombre(de 2 hasta 30 caracteres) [{cliente.nombre}]")
                apellidos = helpers.leer_texto(
                    2, 70, f"Apellidos(de 2 hasta 70 caracteres) [{cliente.apellidos}]")
                db.Clientes.modificar(cliente.dni, nombre, apellidos)
                print("Cliente modificado correctamente.")
            else:
                print("Cliente no encontrado.")

        elif(opcion == '5'):
            print("Borrar un Cliente...\n")
            dni = helpers.leer_texto(3, 3, "DNI(2 números y una letra). ").upper()
            print("Cliente borrado correctamente") if db.Clientes.borrar(dni) else print("Cliente no encontrado")

        elif(opcion == '6'):
            print("Saliendo...\n")
            break

        input("\n Presiona ENTER para continuar...")
