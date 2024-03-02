class Usuarios:
    def __init__(self, nom, cor, cont, i, apep, apem):
        self.__nombre = nom
        self.__correo = cor
        self.__contra = cont
        self.__id = 1
        self.__apellidoP = apep
        self.__apellidoM = apem

    def getNombre(self):
        return self.__nombre

    def setNombre(self, nx):
        self.__nombre = nx

    def getCorreo(self):
        return self.__correo

    def setCorreo(self, cr):
        self.__correo = cr

    def getContra(self):
        return self.__contra

    def setContra(self, cn):
        self.__contra = cn

    def getId(self):
        return self.__id

    def setId(self, d):
        self.__id = d

    def getApellidoP(self):
        return self.__apellidoP

    def setApellidoP(self, app):
        self.__apellidoP = app

    def getApellidoM(self):
        return self.__apellidoM

    def setApellidoM(self, apm):
        self.__apellidoM = apm


class ManejoUsuarios:
    usuarios = []

    def crearUsuario(cls):
        nombre = input("Ingresa el nombre de tu usuario: ")
        apellidoP = input("Ingresa el apellido paterno: ")
        apellidoM = input("Ingresa el apellido materno: ")
        correo = input("Ingresa el correo: ")
        contra = input("Ingresa tu contrasena: ")
        nuevo_usuario = Usuarios(nombre, correo, contra, 1, apellidoP, apellidoM)
        cls.usuarios.append(nuevo_usuario)
        print("Usuario registrado con éxito.")

    def eliminarUsuario(cls, elim):
        for usuario in cls.usuarios:
            if usuario.getNombre() == elim:
                cls.usuarios.remove(usuario)
                print(f"El usuario {elim} ha sido eliminado")
                return
        print(f"El usuario {elim} no existe")

    def editarUsuario(cls, nwNom, nwApp, nwApm, nwcor):
        for usuario in cls.usuarios:
            if usuario.getNombre() == nwNom:
                usuario.setNombre(nwNom)
                usuario.setApellidoP(nwApp)
                usuario.setApellidoM(nwApm)
                usuario.setCorreo(nwcor)
                print("Usuario editado correctamente.")
                return
        print("Usuario no encontrado.")

    def consultarUsuarios(cls):
        for usuario in cls.usuarios:
            print(f"Nombre: {usuario.getNombre()}, Correo: {usuario.getCorreo()}, ID: {usuario.getId()}")
