import tkinter as tk
from tkinter import messagebox

class VentanaLista(tk.Toplevel):
    def __init__(self, master, titulo="Lista"):
        super().__init__(master)
        self.title(titulo)
        
        # Títulos de columnas
        self.frame_titulos = tk.Frame(self)
        self.frame_titulos.pack(side="top", fill="x", padx=5, pady=5)
        
        tk.Label(self.frame_titulos, text="Nombre").grid(row=0, column=0)
        tk.Label(self.frame_titulos, text="Dirección").grid(row=0, column=1)
        tk.Label(self.frame_titulos, text="Correo").grid(row=0, column=2)
        
        # Lista de elementos
        self.lista_elementos = tk.Listbox(self)
        self.lista_elementos.pack(side="top", fill="both", expand=True, padx=5, pady=5)
        
        # Botones
        self.frame_botones = tk.Frame(self)
        self.frame_botones.pack(side="bottom", fill="x", padx=5, pady=5)
        
        self.boton_agregar = tk.Button(self.frame_botones, text="Agregar", command=self.agregar_elemento)
        self.boton_agregar.pack(side="left", padx=5, pady=5)
        
        self.boton_borrar = tk.Button(self.frame_botones, text="Borrar", command=self.borrar_elemento)
        self.boton_borrar.pack(side="left", padx=5, pady=5)
        
        self.boton_modificar = tk.Button(self.frame_botones, text="Modificar", command=self.modificar_elemento)
        self.boton_modificar.pack(side="left", padx=5, pady=5)
    
    def agregar_elemento(self):
        self.master.AccesoWinHija()
        
    
    def borrar_elemento(self):
        pass
    
    def modificar_elemento(self):
        pass
    
class VentanaPrincipal(tk.Tk):
    def __init__(self, master=None):
        super().__init__(master)
        CentraVentana(self, 600,200)
        self.title("Ventana Contactos")
        
        # Barra de botones
        self.frame_botones = tk.Frame(self)
        self.frame_botones.pack()
        
        self.boton_usuarios = tk.Button(self.frame_botones, text="Usuarios", command=self.abrir_ventana_usuarios)
        self.boton_usuarios.pack(side="left", padx=5, pady=5)
        
        self.boton_articulos = tk.Button(self.frame_botones, text="Artículos", command=self.abrir_ventana_articulos)
        self.boton_articulos.pack(side="left", padx=5, pady=5)
        
        self.boton_inventario = tk.Button(self.frame_botones, text="Inventario", command=self.abrir_ventana_inventario)
        self.boton_inventario.pack(side="left", padx=5, pady=5)
        
        self.boton_solicitudes = tk.Button(self.frame_botones, text="Solicitudes", command=self.abrir_ventana_solicitudes)
        self.boton_solicitudes.pack(side="left", padx=5, pady=5)
    
    def abrir_ventana_usuarios(self):
        ventana_usuarios = VentanaLista(self, "Usuarios")
        ventana_usuarios.mainloop()
        
    def abrir_ventana_articulos(self):
        ventana_articulos = VentanaLista(self, "Artículos")
        ventana_articulos.mainloop()
        
    def abrir_ventana_inventario(self):
        ventana_inventario = VentanaLista(self, "Inventario")
        ventana_inventario.mainloop()
        
    def abrir_ventana_solicitudes(self):
        ventana_solicitudes = VentanaLista(self, "Solicitudes")
        ventana_solicitudes.mainloop()

    def AccesoWinHija(self):
         messagebox.showinfo("ventana mama", "acceso desde la ventana hija")


class VentanaControlAcceso(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Control de Acceso")
        CentraVentana(self, 250,150)
        
        self.label_usuario = tk.Label(self, text="Usuario:")
        self.entry_usuario = tk.Entry(self)
        self.label_contraseña = tk.Label(self, text="Contraseña:")
        self.entry_contraseña = tk.Entry(self, show="*")
        self.boton_ingresar = tk.Button(self, text="Ingresar", command=self.verificar_credenciales)
        
        self.label_usuario.pack()
        self.entry_usuario.pack()
        self.label_contraseña.pack()
        self.entry_contraseña.pack()
        self.boton_ingresar.pack()
    
    def verificar_credenciales(self):
        usuario = self.entry_usuario.get()
        contraseña = self.entry_contraseña.get()
        
        # Verificar las credenciales (nombre de usuario y contraseña)
        if usuario == "admin" and contraseña == "admin123":
            self.destroy()  # Cerrar la ventana de control de acceso
            app_principal = VentanaPrincipal()
        else:
            messagebox.showerror("Error", "Credenciales incorrectas")

def CentraVentana(ventana, ancho, alto):
    screen_width = ventana.winfo_screenwidth()
    screen_height = ventana.winfo_screenheight()
    x = (screen_width - ancho) // 2
    y = (screen_height - alto) // 2
    ventana.geometry(f'{ancho}x{alto}+{x}+{y}')


# Crear la ventana de control de acceso y mostrarla primero
app_control_acceso = VentanaControlAcceso()
app_control_acceso.mainloop()
