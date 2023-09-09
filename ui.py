from tkinter import *
from tkinter import ttk
from tkinter.messagebox import askokcancel, WARNING

import database as db

class CenterWidgetMixin:
    def center(self):
        self.update()
        w = self.winfo_width()
        h = self.winfo_height()
        ws = self.winfo_screenwidth()
        hs = self.winfo_screenheight()
        x = int(ws/2 - w/2)
        y = int(hs/2 - h/2)

        self.geometry(f"{w}x{h}+{x}+{y}")

class CreateClientWindow(Toplevel, CenterWidgetMixin):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Crear Cliente")
        self.build()
        self.center()
        self.transient(parent)
        self.grab_set()
    
    def build(self):
        frame = Frame(self)
        frame.pack(padx=20, pady=10)

        Label(frame, text="DNI (2 ints y 1 upper char)").grid(row=0, column=0)
        Label(frame, text="Nombre (de 2 a 30 chars)").grid(row=0, column=1)
        Label(frame, text="Apellidos (de 2 60 chars)").grid(row=0, column=2)

        dni = Entry(frame)
        dni.grid(row=1, column=0)

        nombre = Entry(frame)
        nombre.grid(row=1, column=1)

        apellidos = Entry(frame)
        apellidos.grid(row=1, column=2)

        frame = Frame(self)
        frame.pack(pady=10)

        crear = Button(frame, text='Crear', command=self.create_client)
        crear.configure(state=DISABLED)
        crear.grid(row=0, column=0)

        Button(frame, text='Cerrar', command=self.close).grid(row=0, column=1)


    def create_client(self):
        pass

    def close(self):
        self.destroy()
        self.update()


class MainWindow(Tk, CenterWidgetMixin):
    def __init__(self):
        super().__init__()
        self.title("Gestor de Clientes")
        self.build()
        self.center()

    def build(self):
        frame = Frame(self)
        frame.pack()

        treeView = ttk.Treeview(frame)
        treeView['columns'] = ('DNI', 'Nombre', 'Apellidos')

        treeView.column('#0', width=0, stretch=NO) 
        treeView.column('DNI', anchor=CENTER) 
        treeView.column('Nombre', anchor=CENTER) 
        treeView.column('Apellidos', anchor=CENTER) 

        treeView.heading('DNI', text='DNI', anchor=CENTER)
        treeView.heading('Nombre', text='Nombre', anchor=CENTER)
        treeView.heading('Apellidos', text='Apellidos', anchor=CENTER)

        scrollbar = Scrollbar(frame)
        scrollbar.pack(side=RIGHT, fill=Y)

        treeView['yscrollcommand'] = scrollbar.set

        for cliente in db.Clientes.lista:
            treeView.insert(
                parent='', index='end', iid=cliente.dni,
                values=(cliente.dni, cliente.nombre, cliente.apellidos)
            )

        treeView.pack() 

        frame = Frame(self)
        frame.pack(pady=20)

        Button(frame, text='Crear', command=self.create).grid(row=0, column=0)
        Button(frame, text='Modificar', command=None).grid(row=0, column=1)
        Button(frame, text='Borrar', command=self.delete).grid(row=0, column=2)

        self.treeView = treeView
    
    def delete(self):
        cliente = self.treeView.focus()
        if cliente:
            campos = self.treeView.item(cliente, "values")
            confirmar = askokcancel(
                title = "Confirmar Borrado",
                message = f"¿Borrar {campos[1]} {campos[2]}?",
                icon = WARNING)
            if confirmar:
                self.treeView.delete(cliente)

    def create(self):
        CreateClientWindow(self)

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()