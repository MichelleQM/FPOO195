import sqlite3
from clasesDatos import *

class claseDatabase:
    # Constructor de objeto, se ejecuta cuando se crea un objeto
    def __init__(self):
        print ("Se creo  objeto para manejar base de datos ...")
        self.NombreDB = 'MeskrNSpendBD.db'
        self.connDB = None
        self.cursorDB = None

    # Conectarse a la base de datos
    def ConectarDB(self):
        print ("Conectando DB ", self.NombreDB)
        try:
            self.connDB = sqlite3.connect(self.NombreDB)
            self.cursorDB = self.connDB.cursor()
            print (" Conexion exitosa a la DB")
            return True
        except:
            print (" Falla al conectarse a la base de datos")
            return False


    # ===============================================================
    # FUNCIONES RELACIONADAS CON USUARIOS
    # Obtiene lista de usuarios dados de alta
    def ConsultaUsuarios(self):
        lstUsuarios = []        
        try: 
            consulta = "SELECT * FROM tbUsuarios"
            self.cursorDB.execute(consulta)
            usuarios = self.cursorDB.fetchall()
            for usuario in usuarios:
                lstUsuarios.append(Usuario(usuario[0],usuario[1], usuario[2], usuario[3], usuario[4], usuario[5], usuario[6]))
            return lstUsuarios
        except Exception as e:
            print (" Error en la consulta ", e)
            return lstUsuarios
        

    # Agrega un usuario con los datos dados
    def AgregarUsuario(self, usuario):
        try:
            self.cursorDB.execute("INSERT INTO tbUsuarios (nombre_usuario,contra,nombre_completo,correo,id_rol,id_departamento) VALUES (?, ?, ?, ?,?,?)",
            (usuario.username,usuario.contra,usuario.nombre_completo,usuario.correo,usuario.id_rol,usuario.id_departamento))                
            self.connDB.commit()
            print (" Se agrego usuario: ", usuario.username)
            idRec = self.cursorDB.lastrowid
            return idRec
        except Exception as e:
            print (" No se pudo agregar el usuario ", e, usuario.username)
            return 0


    # Elimina un usuario cuyo id es dado
    def BorrarUsuario(self, idUsuario):
        if isinstance(idUsuario, int):
            idUsuario = str(idUsuario)
        try:
            self.cursorDB.execute("DELETE FROM tbUsuarios WHERE id = ?", (idUsuario))
            self.connDB.commit()
            return True
        except Exception as e:
            return False


    # Modifica datos del usuario con el id y con los datos dados
    def ModificarUsuario(self, usuario):
        idUsuario = usuario.id
        """
        if isinstance(idUsuario, int):
            idUsuario = str(idUsuario)
        """
        try:
            self.cursorDB.execute("UPDATE tbUsuarios SET id_rol=?, id_departamento=? WHERE id=?",
                (usuario.id_rol, usuario.id_departamento, idUsuario))
            self.cursorDB.execute("UPDATE tbUsuarios SET nombre_usuario=?,contra=?,nombre_completo=?,correo=? WHERE id=?",
                (usuario.username, usuario.contra, usuario.nombre_completo, usuario.correo, idUsuario))
            self.connDB.commit()
            return True
        except Exception as e:
            print (" No se pudo modificar el usuario ", e, usuario.id)
            return False


    # Checa usuario y contrasena en tbUsuarios
    def ChecaUsuario(self, nombre, contra):
        print (" password = ", contra)
        self.cursorDB.execute("SELECT * FROM tbUsuarios WHERE nombre_usuario = ? AND contra = ?", (nombre, contra))
        resultado = self.cursorDB.fetchone()
        resp = False
        if resultado:
            resp = True
        return resp


    # Obtiene la lista de departamentos
    def ObtieneDepartamentos(self):
        try: 
            consulta = "SELECT * FROM tbDepartamentos"
            self.cursorDB.execute(consulta)
            departamentos = self.cursorDB.fetchall()
            lstNombres = []
            for depa in departamentos:
                lstNombres.append(depa[1])
            return departamentos, lstNombres
        except Exception as e:
            print (" Error en la consulta ", e)
            return [], []


    # Obtiene la lista de roles
    def ObtieneRoles(self):
        try: 
            consulta = "SELECT * FROM tbRoles"
            self.cursorDB.execute(consulta)
            lstRoles = self.cursorDB.fetchall()
            lstNombres = []
            for rol in lstRoles:
                lstNombres.append(rol[1])            
            return lstRoles, lstNombres
        except Exception as e:
            print (" Error en la consulta ", e)
            return [], []



    # ===============================================================
    # FUNCIONES RELACIONADAS CON PRODUCTOS
    # Obtiene lista de PRODUCTOS dados de alta
    def ConsultaProductos(self):
        lstProductos = []        
        try: 
            consulta = "SELECT * FROM tbProductos"
            self.cursorDB.execute(consulta)
            productos = self.cursorDB.fetchall()
            for producto in productos:
                lstProductos.append(Producto(producto[0],producto[1], producto[2], producto[3], producto[4], producto[5], producto[6]))
            return lstProductos
        except Exception as e:
            print (" Error en la consulta ", e)
            return lstProductos

    # Agrega un producto con los datos dados
    def AgregarProducto(self, producto):
        try:
            self.cursorDB.execute("INSERT INTO tbProductos (nombre,descripcion,cantidad,precio_unitario,id_proveedor,id_categoria) VALUES (?, ?, ?, ?,?,?)",
            (producto.nombre,producto.descripcion,producto.cantidad,producto.precio_unitario,producto.id_proveedor,producto.id_categoria))                
            self.connDB.commit()
            print (" Se agrego producto: ", producto.nombre)
            idRec = self.cursorDB.lastrowid
            return idRec
        except Exception as e:
            print (" No se pudo agregar el producto ", e, producto.nombre)
            return 0
        
    # Elimina un producto cuyo id es dado
    def BorrarProducto(self, idProducto):
        if isinstance(idProducto, int):
            idProducto = str(idProducto)
        try:
            self.cursorDB.execute("DELETE FROM tbProductos WHERE id = ?", (idProducto))
            self.connDB.commit()
            return True
        except Exception as e:
            return False

    # Modifica datos del producto dado
    def ModificarProducto(self, producto):
        idProducto = producto.id
        try:
            self.cursorDB.execute("UPDATE tbProductos SET id=?, nombre=?, id_categoria=? WHERE id=?",
                (producto.id, producto.nombre, producto.id_categoria, idProducto))
            self.cursorDB.execute("UPDATE tbProductos SET descripcion=?,cantidad=?,precio_unitario=?,id_proveedor=? WHERE id=?",
                (producto.descripcion, producto.cantidad, producto.precio_unitario, producto.id_proveedor, idProducto))
            self.connDB.commit()
            return True
        except Exception as e:
            print (" No se pudo modificar el producto ", e, idProducto.id)
            return False
        

    # Obtiene la lista de proveedores
    def ObtieneProveedores(self):
        try: 
            consulta = "SELECT * FROM tbProveedores"
            self.cursorDB.execute(consulta)
            proveedores = self.cursorDB.fetchall()
            lstNombres = []
            for prove in proveedores:
                lstNombres.append(prove[1])
            return proveedores, lstNombres
        except Exception as e:
            print (" Error en la consulta ", e)
            return [], []


    # Obtiene la lista de categorias
    def ObtieneCategorias(self):
        try: 
            consulta = "SELECT * FROM tbCategorias"
            self.cursorDB.execute(consulta)
            lstCategorias = self.cursorDB.fetchall()
            lstNombres = []
            for cate in lstCategorias:
                lstNombres.append(cate[1])            
            return lstCategorias, lstNombres
        except Exception as e:
            print (" Error en la consulta ", e)
            return [], []
    

    # ========================================================================
    # CONSULTAS RELACIONADAS CON INVENTARIOS

    def ConsultaInventario(self):
        lstInventarios= []        
        try: 
            consulta = "SELECT * FROM tbInventario"
            self.cursorDB.execute(consulta)
            inventarios = self.cursorDB.fetchall()
            for inventario in inventarios:
                lstInventarios.append(Inventario(inventario[0],inventario[1], inventario[2], inventario[3], inventario[4], inventario[5], inventario[6]))
            return lstInventarios
        except Exception as e:
            print (" Error en la consulta ", e)
            return lstInventarios

    # Agrega un producto con los datos dados
    def AgregarInventario(self, inventario):
        try:
            self.cursorDB.execute("INSERT INTO tbInventario (id_producto,movimiento,id_ubicacion,cantidad,saldo,fecha) VALUES (?, ?, ?, ?,?,?)",
            (inventario.id_producto, inventario.movimiento, inventario.id_ubicacion,inventario.cantidad,inventario.saldo,inventario.fecha))                
            self.connDB.commit()
            print (" Se agrego inventario: ", inventario.movimiento)
            idRec = self.cursorDB.lastrowid
            return idRec
        except Exception as e:
            print (" No se pudo agregar el inventario ", e, inventario.movimiento)
            return 0


    # Elimina un inventario cuyo id es dado
    def BorrarInventario(self, idInventario):
        if isinstance(idInventario, int):
            idInventario = str(idInventario)
        try:
            self.cursorDB.execute("DELETE FROM tbInventario WHERE id = ?", (idInventario))
            self.connDB.commit()
            return True
        except Exception as e:
            return False

    # Modifica datos del inventario dado
    def ModificarInventario(self, inventario):
        idInventario = inventario.id
        try:
            self.cursorDB.execute("UPDATE tbInventario SET id_producto=?, movimiento=? WHERE id=?",
                (inventario.id_producto, inventario.movimiento, idInventario))
            self.cursorDB.execute("UPDATE tbInventario SET id_ubicacion=?,cantidad=?,saldo=?,fecha=? WHERE id=?",
                (inventario.id_ubicacion, inventario.cantidad, inventario.saldo, inventario.fecha, idInventario))
            self.connDB.commit()
            return True
        except Exception as e:
            print (" No se pudo modificar el inventario ", e, inventario.id)
            return False
        

    # Obtiene la lista de productos
    def ObtieneListaProductos(self):
        try: 
            consulta = "SELECT * FROM tbProductos"
            self.cursorDB.execute(consulta)
            lstProductos = self.cursorDB.fetchall()
            lstNombres = []
            print ("LISTA PRODUCTOS ", lstProductos)
            for producto in lstProductos:
                nombre = producto[1]                
                print (" nombre = ", nombre)
                lstNombres.append(nombre)
            return lstProductos, lstNombres
        except Exception as e:
            print (" Error en la consulta ", e)
            return [], []


    # Obtiene la lista de categorias
    def ObtieneUbicaciones(self):
        try: 
            consulta = "SELECT * FROM tbUbicaciones"
            self.cursorDB.execute(consulta)
            lstUbicaciones = self.cursorDB.fetchall()
            lstNombres = []
            for cate in lstUbicaciones:
                lstNombres.append(cate[1])            
            return lstUbicaciones, lstNombres
        except Exception as e:
            print (" Error en la consulta ", e)
            return [], []
        

    # Obtiene cantidad de un producto con idProducto
    def ObtieneaCantidad(self, idProducto):
        try: 
            self.cursorDB.execute("SELECT * FROM tbProductos")
            lstProductos = self.cursorDB.fetchall()
            print (" lista de cantidades ", lstProductos)
            if lstProductos:
                for producto in lstProductos:
                    if producto[0] == idProducto:
                        return producto[3]
                return 0
        except Exception as e:
            print (" Error en la consulta ", e)
            return 0
        
    def ModificaCantidad(self, idProducto, cantidadMov):
        try:
            cantidad = self.ObtieneaCantidad(idProducto)
            cantidad = cantidad + cantidadMov
            self.cursorDB.execute("UPDATE tbProductos SET cantidad=? WHERE id=?", (cantidad, idProducto))
            self.connDB.commit()
            return True
        except Exception as e:
            print (" No se pudo modificar el inventario ", e, idProducto.id)
            return False

    # ----------------------------------------------------------


    # Cierra conexion a la base de datos
    def CerrarSesionDB(self):
        try:
            print ("Cerrando conexion a DB ", self.NombreDB)
            self.connDB.close
        except Exception as e:
            print ("ERROR al cerrar sesion con DB ", e, self.NombreDB)


if __name__== '__main__':
    objManejadorDB = claseDatabase()
    objManejadorDB.ConectarDB()
    if objManejadorDB.connDB != None:
        """
        user1 = Usuario(0, "Luis", "123", "Luis Romo", "lr@gmail.com",'1','1')
        user2 = Usuario(0, "Pedro", "123", "Pedro Garcia", "pg@gmail.com",'1','1')
        user3 = Usuario(0, "Lola", "123", "Lola Perez ", "lp@gmail.com",'1','1')
        objManejadorDB.AgregarUsuario(user1)
        objManejadorDB.AgregarUsuario(user2)
        objManejadorDB.AgregarUsuario(user3)
        userM = Usuario(2, "Socorro", "q12345", "Socorro Fuentes V.", "luisgj@gmail.com",'1','5')
        resp = objManejadorDB.ModificarUsuario(userM)
        if resp == True:
            print (" se modifico el usuario ", userM.username)
        filas = objManejadorDB.ConsultaUsuarios()        
        lista = objManejadorDB.ObtieneDepartamentos()
        print (" Lista de departamentos = ", lista)                    
        objManejadorDB.BorrarUsuario(6)
        filas = objManejadorDB.ConsultaUsuarios()        
        print ("Usuarios encontrados = ", filas)
        lstRec, lstNom = objManejadorDB.ObtieneProveedores()
        print (" Lista proveedores", lstRec, lstNom)
        lstRec, lstNom = objManejadorDB.ObtieneCategorias()
        print (" Lista categorias", lstRec, lstNom)        
        objManejadorDB.CerrarSesionDB()
        """
        cantidad = objManejadorDB.ObtieneaCantidad(3)
        objManejadorDB.ModificaCantidad(3, 30)

        

    


