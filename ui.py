from tkinter import *
from tkinter import ttk

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

        Button(frame, text='Crear', command=None).grid(row=0, column=0)
        Button(frame, text='Modificar', command=None).grid(row=0, column=1)
        Button(frame, text='Borrar', command=None).grid(row=0, column=2)

        self.treeView = treeView

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()