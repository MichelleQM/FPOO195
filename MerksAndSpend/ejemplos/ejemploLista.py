
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class VentanaControlAcceso(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Control de Acceso")

        self.label_usuario = tk.Label(self, text="Usuario:")
        self.label_usuario.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.entry_usuario = tk.Entry(self)
        self.entry_usuario.grid(row=0, column=1, padx=5, pady=5)

        self.label_contrasena = tk.Label(self, text="Contraseña:")
        self.label_contrasena.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.entry_contrasena = tk.Entry(self, show="*")
        self.entry_contrasena.grid(row=1, column=1, padx=5, pady=5)

        self.boton_ingresar = tk.Button(self, text="Ingresar", command=self.ingresar)
        self.boton_ingresar.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

    def ingresar(self):
        usuario = self.entry_usuario.get()
        contrasena = self.entry_contrasena.get()
        # Verificar las credenciales del usuario
        if usuario == "admin" and contrasena == "123":
            self.destroy()
            self.master.mostrar_ventana_principal()
        else:
            tk.messagebox.showerror("Error", "Credenciales incorrectas.")

class VentanaAgregarUsuario(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Agregar Usuario")

        self.label_nombre = tk.Label(self, text="Nombre:")
        self.label_nombre.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.entry_nombre = tk.Entry(self)
        self.entry_nombre.grid(row=0, column=1, padx=5, pady=5)

        self.label_apellido = tk.Label(self, text="Apellido:")
        self.label_apellido.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.entry_apellido = tk.Entry(self)
        self.entry_apellido.grid(row=1, column=1, padx=5, pady=5)

        self.boton_agregar = tk.Button(self, text="Agregar", command=self.agregar_usuario)
        self.boton_agregar.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

    def agregar_usuario(self):
        nombre = self.entry_nombre.get()
        apellido = self.entry_apellido.get()
        if nombre and apellido:
            self.master.agregar_usuario_treeview(nombre, apellido)
            self.destroy()
        else:
            tk.messagebox.showerror("Error", "Por favor, ingresa nombre y apellido del usuario.")

class VentanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tabla de Usuarios")
        self.geometry("400x300")

        self.treeview = ttk.Treeview(self, columns=("Nombre", "Apellido"))
        self.treeview.heading("#0", text="ID")
        self.treeview.heading("Nombre", text="Nombre")
        self.treeview.heading("Apellido", text="Apellido")
        self.treeview.pack()

        self.boton_agregar_usuario = tk.Button(self, text="Agregar Usuario", command=self.abrir_ventana_agregar_usuario)
        self.boton_agregar_usuario.pack(pady=10)

        # Mostrar ventana de control de acceso
        self.mostrar_ventana_control_acceso()

    def mostrar_ventana_control_acceso(self):
        ventana_control_acceso = VentanaControlAcceso(self)

    def mostrar_ventana_principal(self):
        self.deiconify()

    def abrir_ventana_agregar_usuario(self):
        ventana_agregar_usuario = VentanaAgregarUsuario(self)

    def agregar_usuario_treeview(self, nombre, apellido):
        id_ultimo = int(self.treeview.get_children()[-1]) if self.treeview.get_children() else 0
        self.treeview.insert("", "end", text=id_ultimo + 1, values=(nombre, apellido))

# Crear la ventana principal
app_principal = VentanaPrincipal()
app_principal.mainloop()
