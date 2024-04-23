# ++++++++++++++++++++++++++++++++++++++++++++++++++
# VENTANAS DE ADMINISTRACION DE PRODUCTOS O ARTICULOS

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from clasesDatos import *
from claseDatabase import *
from general import *

objDatabase = claseDatabase()
resp = objDatabase.ConectarDB()
if resp == False:
    print ("ERROR FATAL: no se pudo conectar a la base de datos")
    exit()
lstProveedores, lstNombresProveedores = objDatabase.ObtieneProveedores()
lstCategorias, lstNombresCate = objDatabase.ObtieneCategorias()


# Ventana principal de productos, se muestran en una tabla 
class VentanaProductos(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        CentraVentana(self, 1400, 470)        
        self.title("Ventana de Edicion de PRODUCTOS")
        self.productos = self.LoadProductos()
        self.tabla = ttk.Treeview(self)
        self.tabla["columns"]=("id", "Nombre", "Descripcion", "Cantidad", "precio_unitario", "id_proveedor", "id_categoria")
        self.tabla.column("#0", width=40) 
        self.tabla.heading("id", text="ID")
        self.tabla.column("id", width=100) 
        self.tabla.heading("Nombre", text="Nombre")
        self.tabla.column("Nombre", width=200)         
        self.tabla.heading("Descripcion", text="Descripcion")
        self.tabla.column("Descripcion", width=200)                 
        self.tabla.heading("Cantidad", text="Cantidad")
        self.tabla.column("Cantidad", width=300)                         
        self.tabla.heading("precio_unitario", text="precio_unitario")
        self.tabla.column("precio_unitario", width=150)                         
        self.tabla.heading("id_proveedor", text="id_proveedor")
        self.tabla.column("id_proveedor", width=150)                                 
        self.tabla.heading("id_categoria", text="id_categoria")
        self.tabla.column("id_categoria", width=150)  

        self.actualizar_tabla()
        self.tabla.grid(row=0, column=0, columnspan=3, padx=5, pady=5)
        btn_editar = tk.Button(self, text="Editar", command=self.editar_producto)
        btn_editar.grid(row=1, column=0, padx=5, pady=5)
        btn_borrar = tk.Button(self, text="Borrar", command=self.borrar_producto)
        btn_borrar.grid(row=1, column=1, padx=5, pady=5)
        btn_agregar = tk.Button(self, text="Agregar", command=self.agregar_producto)
        btn_agregar.grid(row=1, column=2, padx=5, pady=5)


    # Funcion para actualizar tabla de productos en pantalla
    def actualizar_tabla(self):
        for i in self.tabla.get_children():
            self.tabla.delete(i)
        for idx, producto in enumerate(self.productos, start=1):
            self.tabla.insert("", "end", text=idx, values=(producto.id, producto.nombre, producto.descripcion, producto.cantidad, producto.precio_unitario, producto.id_proveedor,producto.id_categoria))


    # Funcion para editar un usuario,se abre una ventana de edicion
    def editar_producto(self):
        seleccion = self.tabla.selection()
        if seleccion:
            idx = int(self.tabla.item(seleccion[0], "text")) - 1
            producto = self.productos[idx]
            VentanaEdicionProductos(self, producto)
            self.actualizar_tabla()


    # Funcion para eliminar usuario, se elimina de la tabla y de la DB
    def borrar_producto(self):
        seleccion = self.tabla.selection()
        if seleccion:
            idx = int(self.tabla.item(seleccion[0], "text")) - 1
            del self.productos[idx]
            item = self.tabla.selection()[0]  
            valores = self.tabla.item(item, "values") 
            idProducto = int(valores[0])
            resp = objDatabase.BorrarProducto(idProducto)
            if resp == True:
                print("Se elimino producto con id = ", idProducto)
            else: 
                print ("No se pudo eliminar el producto ",idProducto)                
            self.actualizar_tabla()


    # Se abre ventana de edicion para agregar un producto
    def agregar_producto(self):
        VentanaEdicionProductos(self)

    # Obtiene desde la base de datos la lista de productos
    def LoadProductos(self):
        lstProductos = objDatabase.ConsultaProductos()
        return lstProductos
    
# ====================================================================
# Ventana secundaria para editar/agregar un producto
class VentanaEdicionProductos(tk.Toplevel):
    def __init__(self, master, producto=None):
        super().__init__(master)
        CentraVentana(self, 350, 250)    
        self.producto = producto
        if self.producto:
            self.title("Editar Producto")
        else:
            self.title("Agregar Producto")
        self.nombre = tk.StringVar()
        self.descripcion = tk.StringVar()
        self.cantidad = tk.StringVar()
        self.precio_unitario = tk.StringVar()
        self.id_proveedor = tk.StringVar()
        self.id_categoria = tk.StringVar()

        # Si el producto es dado se trata de editarlo
        if self.producto: # 
            self.nombre.set(self.producto.nombre)
            self.descripcion.set(self.producto.descripcion)
            self.cantidad.set(self.producto.cantidad)
            self.precio_unitario.set(self.producto.precio_unitario)
            self.id_proveedor.set(self.producto.id_proveedor)
            self.id_categoria.set(self.producto.id_categoria)
        # Si es agregar nuevo producto, se establece primera opcion en los combobox
        else: 
            self.id_proveedor.set(1)
            self.id_categoria.set(1)

        lbl_nombre = tk.Label(self, text="Nombre:")
        lbl_nombre.grid(row=0, column=0, padx=5, pady=5)
        entry_nombre = tk.Entry(self, textvariable=self.nombre)
        entry_nombre.grid(row=0, column=1, padx=5, pady=5)

        lbl_decripcion = tk.Label(self, text="Descripcion:")
        lbl_decripcion.grid(row=1, column=0, padx=5, pady=5)
        entry_descripcion = tk.Entry(self, textvariable=self.descripcion)
        entry_descripcion.grid(row=1, column=1, padx=5, pady=5)

        lbl_cantidad = tk.Label(self, text="Cantidad:")
        lbl_cantidad.grid(row=2, column=0, padx=5, pady=5)
        entry_cantidad = tk.Entry(self, textvariable=self.cantidad)
        entry_cantidad.grid(row=2, column=1, padx=5, pady=5)

        lbl_precio_unitario = tk.Label(self, text="Precio_unitario:")
        lbl_precio_unitario.grid(row=3, column=0, padx=5, pady=5)
        entry_precio_unitario = tk.Entry(self, textvariable=self.precio_unitario)
        entry_precio_unitario.grid(row=3, column=1, padx=5, pady=5)

        lbl_proveedor = tk.Label(self, text="PROVEEDOR:")
        lbl_proveedor.grid(row=4, column=0, padx=5, pady=5)
        entry_proveedor = ttk.Combobox(self, textvariable=self.id_proveedor, values=lstNombresProveedores)
        entry_proveedor.grid(row=4, column=1, padx=5, pady=5)
        idProveedor = int(self.id_proveedor.get()) - 1
        entry_proveedor.current(idProveedor)

        lbl_categoria = tk.Label(self, text="Categoria:")
        lbl_categoria.grid(row=5, column=0, padx=5, pady=5)
        entry_categoria = ttk.Combobox(self, textvariable=self.id_categoria, values=lstNombresCate)
        entry_categoria.grid(row=5, column=1, padx=5, pady=5)
        idCategoria = int(self.id_categoria.get()) - 1
        entry_categoria.current(idCategoria)

        btn_text = "Guardar" if self.id_proveedor else "Agregar"
        btn_guardar = tk.Button(self, text=btn_text, command=self.guardar_producto)
        btn_guardar.grid(row=6, column=0, columnspan=2, padx=5, pady=5)


    # Funcion para guardar producto en la ventana y en la base de datos
    def guardar_producto(self):
        nombre = self.nombre.get()
        descripcion = self.descripcion.get()
        cantidad = self.cantidad.get()
        precio_unitario = self.precio_unitario.get()
        proveedor = self.id_proveedor.get()
        proveedor = self.ObtieneID(lstProveedores, proveedor)
        categoria = self.id_categoria.get()        
        categoria = self.ObtieneID(lstCategorias, categoria)

        if self.producto:
            self.producto.nombre = nombre
            self.producto.descripcion = descripcion
            self.producto.cantidad = cantidad
            self.producto.precio_unitario = precio_unitario
            self.producto.id_proveedor = proveedor
            self.producto.id_categoria = categoria
            resp = objDatabase.ModificarProducto(self.producto)
            if resp == True:
                print (" Se modifico el producto id = ", self.producto.id)
        else:
            producto = Producto(0, nombre, descripcion, cantidad, precio_unitario, proveedor, categoria)
            id = objDatabase.AgregarProducto(producto)  
            producto = Producto(id, nombre, descripcion, cantidad, precio_unitario, proveedor, categoria)
            self.master.productos.append(producto)
        self.master.actualizar_tabla()
        self.destroy()


    # Dada la lista de registros de proveedores o categorias obtiene el ID en 
    # base a su nombre
    def ObtieneID(self, lstRegistros, nombre):
        for registro in lstRegistros:
            strNombre = registro[1]
            if strNombre == nombre:
                return registro[0]
        return '0'
