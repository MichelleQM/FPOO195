# ++++++++++++++++++++++++++++++++++++++++++++++++++
# VENTANAS DE ADMINISTRACION DE PRODUCTOS INVENTARIOS

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from clasesDatos import *
from claseDatabase import *
from general import *
from datetime import date

objDatabase = claseDatabase()
resp = objDatabase.ConectarDB()
if resp == False:
    print ("ERROR FATAL: no se pudo conectar a la base de datos")
    exit()
lstProductos, lstNombresProductos = objDatabase.ObtieneListaProductos()
lstUbicaciones, lstNombresUbi = objDatabase.ObtieneUbicaciones()
lstMovimiento = ["Entrada", "Salida"]


# Ventana principal de productos, se muestran en una tabla 
class VentanaInventarios(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        CentraVentana(self, 1400, 470)        
        self.title("Ventana de Edicion de INVENTARIO")
        self.inventarios = self.LoadInventarios()
        self.tabla = ttk.Treeview(self)
        self.tabla["columns"]=("id", "idProducto", "Movimiento", "id_ubicacion", "cantidad", "saldo", "fecha")
        self.tabla.column("#0", width=40) 
        self.tabla.heading("id", text="ID")
        self.tabla.column("id", width=100) 
        self.tabla.heading("idProducto", text="idProducto")
        self.tabla.column("idProducto", width=200)         
        self.tabla.heading("Movimiento", text="Movimiento")
        self.tabla.column("Movimiento", width=200)                 
        self.tabla.heading("id_ubicacion", text="id_ubicacion")
        self.tabla.column("id_ubicacion", width=300)                         
        self.tabla.heading("cantidad", text="cantidad")
        self.tabla.column("cantidad", width=150)                         
        self.tabla.heading("saldo", text="saldo")
        self.tabla.column("saldo", width=150)                                 
        self.tabla.heading("fecha", text="fecha")
        self.tabla.column("fecha", width=150)  

        self.actualizar_tabla()
        self.tabla.grid(row=0, column=0, columnspan=3, padx=5, pady=5)
        btn_editar = tk.Button(self, text="Editar", command=self.editar_inventario)
        btn_editar.grid(row=1, column=0, padx=5, pady=5)
        btn_borrar = tk.Button(self, text="Borrar", command=self.borrar_inventario)
        btn_borrar.grid(row=1, column=1, padx=5, pady=5)
        btn_agregar = tk.Button(self, text="Agregar", command=self.agregar_inventario)
        btn_agregar.grid(row=1, column=2, padx=5, pady=5)

    # Funcion para actualizar tabla de productos en pantalla
    def actualizar_tabla(self):
        for i in self.tabla.get_children():
            self.tabla.delete(i)
        for idx, inventario in enumerate(self.inventarios, start=1):
            self.tabla.insert("", "end", text=idx, values=(inventario.id, inventario.id_producto, inventario.movimiento, inventario.id_ubicacion, inventario.cantidad, inventario.saldo, inventario.fecha))

    # Funcion para editar un inventario,se abre una ventana de edicion
    def editar_inventario(self):
        seleccion = self.tabla.selection()
        if seleccion:
            idx = int(self.tabla.item(seleccion[0], "text")) - 1
            inventario = self.inventarios[idx]
            VentanaEdicionInventarios(self, inventario)
            self.actualizar_tabla()

    # Funcion para eliminar inventario, se elimina de la tabla y de la DB
    def borrar_inventario(self):
        seleccion = self.tabla.selection()
        if seleccion:
            idx = int(self.tabla.item(seleccion[0], "text")) - 1
            del self.inventarios[idx]
            item = self.tabla.selection()[0]  
            valores = self.tabla.item(item, "values") 
            idInventario = int(valores[0])
            resp = objDatabase.BorrarInventario(idInventario)
            if resp == True:
                print("Se elimino inventario con id = ", idInventario)
            else: 
                print ("No se pudo eliminar el inventario ",idInventario)                
            self.actualizar_tabla()


    # Se abre ventana de edicion para agregar un producto
    def agregar_inventario(self):
        VentanaEdicionInventarios(self)

    # Obtiene desde la base de datos la lista de productos
    def LoadInventarios(self):
        lstInventario = objDatabase.ConsultaInventario()
        return lstInventario
    
# ====================================================================
# Ventana secundaria para editar/agregar un inventario
class VentanaEdicionInventarios(tk.Toplevel):
    def __init__(self, master, inventario=None):
        super().__init__(master)
        CentraVentana(self, 350, 250)    
        self.inventario = inventario
        if self.inventario:
            self.title("Editar Inventario")
        else:
            self.title("Agregar Inventario")
        self.id_producto = tk.StringVar()
        self.movimiento = tk.StringVar()
        self.id_ubicacion = tk.StringVar()
        self.cantidad = tk.StringVar()
        self.saldo = tk.StringVar()
        self.fecha = tk.StringVar()
        # Si el inventario es dado se trata de editarlo
        if self.inventario: 
            ixProducto = self.ObtieneIndice(lstProductos, self.id_producto)            
            print (" ix, id = ", ixProducto, inventario.id)
            self.id_producto.set(self.inventario.id_producto)
            self.movimiento.set(self.inventario.movimiento)
            self.id_ubicacion.set(self.inventario.id_ubicacion)
            self.cantidad.set(self.inventario.cantidad)
            self.saldo.set(self.inventario.saldo)
            self.fecha.set(self.inventario.fecha)
        else: 
        # Si es agregar nuevo producto, se establece primera opcion en los combobox            
            self.id_producto.set(1)
            self.id_ubicacion.set(1)
            fechaHoy  = date.today()
            strFecha = fechaHoy.strftime("%Y-%m-%d")
            self.fecha.set(strFecha)
            self.movimiento.set(lstMovimiento[0])

        lbl_producto = tk.Label(self, text="Producto:")
        lbl_producto.grid(row=0, column=0, padx=5, pady=5)
        entry_producto = ttk.Combobox(self, textvariable=self.id_producto, values=lstNombresProductos)
        entry_producto.grid(row=0, column=1, padx=5, pady=5)
        ixProducto = self.ObtieneIndice(lstProductos, self.id_producto)
        entry_producto.current(ixProducto)

        lbl_movimiento = tk.Label(self, text="Movimiento:")
        lbl_movimiento.grid(row=1, column=0, padx=5, pady=5)
        entry_movimiento = ttk.Combobox(self, textvariable=self.movimiento, values=lstMovimiento)
        entry_movimiento.grid(row=1, column=1, padx=5, pady=5)

        lbl_cantidad = tk.Label(self, text="Cantidad:")
        lbl_cantidad.grid(row=2, column=0, padx=5, pady=5)
        entry_cantidad = tk.Entry(self, textvariable=self.cantidad)
        entry_cantidad.grid(row=2, column=1, padx=5, pady=5)

        lbl_saldo = tk.Label(self, text="Saldo:")
        lbl_saldo.grid(row=3, column=0, padx=5, pady=5)
        entry_saldo = tk.Entry(self, textvariable=self.saldo)
        entry_saldo.grid(row=3, column=1, padx=5, pady=5)
        entry_saldo.config(state=tk.DISABLED)

        lbl_fecha = tk.Label(self, text="Fecha:")
        lbl_fecha.grid(row=4, column=0, padx=5, pady=5)
        entry_fecha = tk.Entry(self, textvariable=self.fecha)
        entry_fecha.grid(row=4, column=1, padx=5, pady=5)
        entry_fecha.config(state=tk.DISABLED)        

        lbl_unicacion = tk.Label(self, text="Ubicacion:")
        lbl_unicacion.grid(row=5, column=0, padx=5, pady=5)
        entry_ubicacion = ttk.Combobox(self, textvariable=self.id_ubicacion, values=lstNombresUbi)
        entry_ubicacion.grid(row=5, column=1, padx=5, pady=5)
        idUbicacion = int(self.id_ubicacion.get()) - 1
        entry_ubicacion.current(idUbicacion)

        btn_text = "Guardar" if self.id_producto else "Agregar"
        btn_guardar = tk.Button(self, text=btn_text, command=self.guardar_inventario)
        btn_guardar.grid(row=6, column=0, columnspan=2, padx=5, pady=5)


    # Funcion para guardar inventario en la ventana y en la base de datos
    def guardar_inventario(self):
        movimiento = self.movimiento.get()
        cantidad = self.cantidad.get()
        saldo = self.saldo.get()
        fecha = self.fecha.get()
        producto = self.id_producto.get()
        idProducto = self.ObtieneID(lstProductos, producto)
        ubicacion = self.id_ubicacion.get()        
        idUbicacion = self.ObtieneID(lstUbicaciones, ubicacion)

        if self.inventario:
            self.inventario.id_producto = idProducto
            self.inventario.movimiento = movimiento
            self.inventario.cantidad = cantidad
            self.inventario.saldo = saldo
            self.inventario.id_ubicacion = idUbicacion
            self.inventario.fecha = fecha
            resp = objDatabase.ModificarInventario(self.inventario)
            if resp == True:
                print (" Se modifico el inventario id = ", self.inventario.id)
        else:
            inventario = Inventario(0, idProducto, movimiento, idUbicacion, cantidad, saldo, fecha)
            id = objDatabase.AgregarInventario(inventario)  
            inventario = Inventario(id, idProducto, movimiento, idUbicacion, cantidad, saldo, fecha)
            self.master.inventarios.append(inventario)
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

    # Dada una lista obtiene el IX del elemento con ID dado
    def ObtieneIndice(self, lstRegistros, id):
        ix = 1
        for registro in lstRegistros:
            idX = registro[0]
            if idX == id:
                return ix
            ix = ix + 1
        return 0