# =================================================
# Clases RELACIONADAS CON USUARIOS
class Usuario:
    def __init__(self, id, username, contra, nombre_completo, correo, id_rol, id_departamento):
        #self.id_usuario = id_usuario
        self.id = id
        self.username = username
        self.contra = contra
        self.nombre_completo = nombre_completo
        self.correo = correo
        self.id_rol = id_rol
        self.id_departamento = id_departamento

class Rol:
    def __init__(self, id_rol, nombre, descripcion):
        self.id_rol = id_rol
        self.nombre = nombre
        self.descripcion = descripcion

class Departamento:
    def __init__(self, id_departamento, nombre, descripcion):
        self.id_departamento = id_departamento
        self.nombre = nombre
        self.descripcion = descripcion


# =================================================
# Clases RELACIONADAS CON PRODUCTOS
class Producto:
    def __init__(self, id, nombre, descripcion, cantidad, precio_unitario, id_proveedor, id_categoria):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario
        self.id_proveedor = id_proveedor
        self.id_categoria = id_categoria

class Proveedor:
    def __init__(self, id, nombre, direccion, telefono, correo):
        self.id_rol = id
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo


class Categoria:
    def __init__(self, id, nombre, descripcion):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        

# =================================================
# Clases de datos para manejo de inventarios
class Inventario:
    def __init__(self, id, id_producto, movimiento, id_ubicacion, cantidad, saldo, fecha):
        self.id = id
        self.id_producto = id_producto
        self.movimiento = movimiento
        self.id_ubicacion = id_ubicacion
        self.cantidad = cantidad
        self.saldo = saldo
        self.fecha = fecha


class Ubicacion:
    def __init__(self, id, nombre, descripcion):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
