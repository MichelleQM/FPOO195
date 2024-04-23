import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sys
from clasesDatos import *
from claseDatabase import *
from general import *
from winProductos import *
from winInventario import *

# ====================================================================
# ====================================================================
# Ventana principal de usuarios, se muestran en una tabla 
class VentanaUsuarios(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        CentraVentana(self, 1400, 470)        
        self.title("Ventana de Edicion de USUARIOS")


        self.usuarios = self.LoadUsuarios()
        self.tabla = ttk.Treeview(self)
        self.tabla["columns"]=("id", "Nombre", "Password", "Nombre completo", "Mail", "Rol", "Departamento")
        self.tabla.column("#0", width=40) 
        self.tabla.heading("id", text="ID")
        self.tabla.column("id", width=100) 
        self.tabla.heading("Nombre", text="Nombre")
        self.tabla.column("Nombre", width=200)         
        self.tabla.heading("Password", text="Password")
        self.tabla.column("Password", width=200)                 
        self.tabla.heading("Nombre completo", text="Nombre completo")
        self.tabla.column("Nombre completo", width=300)                         
        self.tabla.heading("Mail", text="Mail")
        self.tabla.column("Mail", width=150)                         
        self.tabla.heading("Rol", text="Rol")
        self.tabla.column("Rol", width=150)                                 
        self.tabla.heading("Departamento", text="Departamento")
        self.tabla.column("Departamento", width=150)                                 

        self.actualizar_tabla()
        self.tabla.grid(row=0, column=0, columnspan=3, padx=5, pady=5)
        btn_editar = tk.Button(self, text="Editar", command=self.editar_usuario)
        btn_editar.grid(row=1, column=0, padx=5, pady=5)
        btn_borrar = tk.Button(self, text="Borrar", command=self.borrar_usuario)
        btn_borrar.grid(row=1, column=1, padx=5, pady=5)
        btn_agregar = tk.Button(self, text="Agregar", command=self.agregar_usuario)
        btn_agregar.grid(row=1, column=2, padx=5, pady=5)


    # Funcion para actualizar tabla de usuarios en pantalla
    def actualizar_tabla(self):
        for i in self.tabla.get_children():
            self.tabla.delete(i)
        for idx, usuario in enumerate(self.usuarios, start=1):
            self.tabla.insert("", "end", text=idx, values=(usuario.id, usuario.username, usuario.contra, usuario.nombre_completo, usuario.correo, usuario.id_rol,usuario.id_departamento))


    # Funcion para editar un usuario,se abre una ventana de edicion
    def editar_usuario(self):
        seleccion = self.tabla.selection()
        if seleccion:
            idx = int(self.tabla.item(seleccion[0], "text")) - 1
            usuario = self.usuarios[idx]
            VentanaEdicionUsuarios(self, usuario)
            self.actualizar_tabla()


    # Funcion para eliminar usuario, se elimina de la tabla y de la DB
    def borrar_usuario(self):
        seleccion = self.tabla.selection()
        if seleccion:
            idx = int(self.tabla.item(seleccion[0], "text")) - 1
            del self.usuarios[idx]
            item = self.tabla.selection()[0]  
            valores = self.tabla.item(item, "values") 
            idUsuario = int(valores[0])
            resp = objDatabase.BorrarUsuario(idUsuario)
            if resp == True:
                print("Se elimino usuario con id = ", idUsuario)
            else: 
                print ("No se pudo eliminar el usuario ",idUsuario)                
            self.actualizar_tabla()


    # Se abre ventana de edicion para agregar un usuario
    def agregar_usuario(self):
        VentanaEdicionUsuarios(self)

    # Obtiene desde la base de datos la lista de usuarios
    def LoadUsuarios(self):
        lstUsuarios = objDatabase.ConsultaUsuarios()
        return lstUsuarios
    
# ====================================================================
# Ventana secundaria para editar/agregar un usuario
class VentanaEdicionUsuarios(tk.Toplevel):
    def __init__(self, master, usuario=None):
        super().__init__(master)
        CentraVentana(self, 350, 250)                
        self.usuario = usuario
        if self.usuario:
            self.title("Editar Usuario")
        else:
            self.title("Agregar Usuario")
        self.username = tk.StringVar()
        self.contra = tk.StringVar()
        self.nombre_completo = tk.StringVar()
        self.correo = tk.StringVar()
        self.id_rol = tk.StringVar()
        self.id_departamento = tk.StringVar()
        # Si el usuario es dado se trata de editarlo
        if self.usuario: # 
            self.username.set(self.usuario.username)
            self.contra.set(self.usuario.contra)
            self.nombre_completo.set(self.usuario.nombre_completo)
            self.correo.set(self.usuario.correo)
            self.id_rol.set(self.usuario.id_rol)
            self.id_departamento.set(self.usuario.id_departamento)
        # Si es agregar nuevo usuario, se establece primera opcion en los combobox
        else: 
            self.id_rol.set(1)
            self.id_departamento.set(1)

        lbl_username = tk.Label(self, text="Nombre:")
        lbl_username.grid(row=0, column=0, padx=5, pady=5)
        entry_username = tk.Entry(self, textvariable=self.username)
        entry_username.grid(row=0, column=1, padx=5, pady=5)

        lbl_contra = tk.Label(self, text="Password:")
        lbl_contra.grid(row=1, column=0, padx=5, pady=5)
        entry_contra = tk.Entry(self, textvariable=self.contra)
        entry_contra.grid(row=1, column=1, padx=5, pady=5)

        lbl_nombre_completo = tk.Label(self, text="Nombre completo:")
        lbl_nombre_completo.grid(row=2, column=0, padx=5, pady=5)
        entry_lbl_nombre_completo = tk.Entry(self, textvariable=self.nombre_completo)
        entry_lbl_nombre_completo.grid(row=2, column=1, padx=5, pady=5)

        lbl_correo = tk.Label(self, text="Correo:")
        lbl_correo.grid(row=3, column=0, padx=5, pady=5)
        entry_correo = tk.Entry(self, textvariable=self.correo)
        entry_correo.grid(row=3, column=1, padx=5, pady=5)

        lbl_rol = tk.Label(self, text="ROL:")
        lbl_rol.grid(row=4, column=0, padx=5, pady=5)
        entry_rol = ttk.Combobox(self, textvariable=self.id_rol, values=lstNombresRol)
        entry_rol.grid(row=4, column=1, padx=5, pady=5)
        idRol = int(self.id_rol.get()) - 1
        entry_rol.current(idRol)

        lbl_departamento = tk.Label(self, text="Departamento:")
        lbl_departamento.grid(row=5, column=0, padx=5, pady=5)
        entry_departamento = ttk.Combobox(self, textvariable=self.id_departamento, values=lstNombresDepa)
        entry_departamento.grid(row=5, column=1, padx=5, pady=5)
        idDepa = int(self.id_departamento.get()) - 1
        entry_departamento.current(idDepa)

        btn_text = "Guardar" if self.usuario else "Agregar"
        btn_guardar = tk.Button(self, text=btn_text, command=self.guardar_usuario)
        btn_guardar.grid(row=6, column=0, columnspan=2, padx=5, pady=5)


    # Funcion para agregar usuario en la ventana y en la base de datos
    def guardar_usuario(self):
        nombre = self.username.get()
        contra = self.contra.get()
        nombre_completo = self.nombre_completo.get()
        correo = self.correo.get()
        if nombre == "" or contra == "" or nombre_completo == "" or correo == "":
            messagebox.showinfo("AVISO", "Llenar todos los campos")            
            return
        rol = self.id_rol.get()
        rol = self.ObtieneID(lstRoles, rol)
        departamento = self.id_departamento.get()        
        departamento = self.ObtieneID(lstDepartamentos, departamento)
        if self.usuario:
            self.usuario.username = nombre
            self.usuario.contra = contra
            self.usuario.nombre_completo = nombre_completo
            self.usuario.correo = correo
            self.usuario.id_rol = rol
            self.usuario.id_departamento = departamento
            resp = objDatabase.ModificarUsuario(self.usuario)
            if resp == True:
                print (" Se modifico el usuario id = ", self.usuario.id)
        else:
            usuario = Usuario(0, nombre, contra, nombre_completo, correo, rol, departamento)
            id = objDatabase.AgregarUsuario(usuario)  
            usuario = Usuario(id, nombre, contra, nombre_completo, correo, rol, departamento)                      
            self.master.usuarios.append(usuario)
        self.master.actualizar_tabla()
        self.destroy()


    # Dada la lista de registros de Roles o Departamentos obtiene el ID en 
    # base a su nombre
    def ObtieneID(self, lstRegistros, nombre):
        for registro in lstRegistros:
            strNombre = registro[1]
            if strNombre == nombre:
                return registro[0]
        return '0'





# ====================================================================
# Ventana inicial de control de acceso
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
        self.boton_ingresar.bind("<Return>", self.verificar_credenciales)
        self.after(0, self.poner_foco)
        self.label_usuario.pack()
        self.entry_usuario.pack()
        self.label_contraseña.pack()
        self.entry_contraseña.pack()
        self.boton_ingresar.pack()
    

    # Cuando se abra la ventana de acceso poner el cursor en el entry de usuario
    def poner_foco(self):
        self.entry_usuario.focus_set()


    # Funcion para verificar acceso de usuario, 
    # El usuario de inicio es admin y su password es 123
    # Cuando ya hay usuarios dados de alta se verifica en DB
    def verificar_credenciales(self):
        usuario = self.entry_usuario.get()
        contraseña = self.entry_contraseña.get()
        if usuario == "" or contraseña == "":
            messagebox.showinfo("AVISO", "Llenar todos los campos")            
            return        
        # Verificar las credenciales (nombre de usuario y contraseña)
        resp = objDatabase.ChecaUsuario(usuario, contraseña)
        if (usuario == "admin" and contraseña == "123") or resp == True:
            self.destroy()  # Cerrar la ventana de control de acceso
            app_principal = VentanaMenu()
        else:
            messagebox.showerror("Error", "Credenciales incorrectas")




# ====================================================================
# Ventana principal de la aplicacion
class VentanaMenu(tk.Tk):
    def __init__(self, master=None):
        super().__init__(master)
        CentraVentana(self, 1410,600)
        self.title("SISTEMA MERKS AND SPEND-MANEJO DE INVENTARIOS")
        
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
        winUsuarios = VentanaUsuarios(self)
        #ventana_usuarios.mainloop()
        
    def abrir_ventana_articulos(self):
        winProductos = VentanaProductos(self)
        
    def abrir_ventana_inventario(self):
        winInventarios = VentanaInventarios(self)

    def abrir_ventana_solicitudes(self):
        messagebox.showinfo("AVISO", "En construccion")



# PROGRAMA PRINCIPAL DE INICIO
# Crear la ventana de control de acceso y mostrarla primero
objDatabase = claseDatabase()
resp = objDatabase.ConectarDB()
if resp == False:
    print ("ERROR FATAL: no se pudo conectar a la base de datos")
    sys.exit()
lstDepartamentos, lstNombresDepa = objDatabase.ObtieneDepartamentos()
lstRoles, lstNombresRol = objDatabase.ObtieneRoles()
app_control_acceso = VentanaControlAcceso()
app_control_acceso.mainloop()
