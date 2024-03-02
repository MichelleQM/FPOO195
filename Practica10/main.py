from Usuarios import *

def mostrar_menu():
    print("1. Registrar usuario")
    print("2. Consultar usuarios")
    print("3. Editar usuario")
    print("4. Eliminar usuario")
    print("5. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            Usuarios.crearUsuario()
        elif opcion == "2":
            Usuarios.consultarUsuarios()
        elif opcion == "3":
            nombre = input("Ingresa el nombre del usuario a editar: ")
            nuevo_nombre = input("Nuevo nombre: ")
            nuevo_apellidoP = input("Nuevo apellido paterno: ")
            nuevo_apellidoM = input("Nuevo apellido materno: ")
            nuevo_correo = input("Nuevo correo: ")
            Usuarios.editarUsuario(nuevo_nombre, nuevo_apellidoP, nuevo_apellidoM, nuevo_correo)
        elif opcion == "4":
            usuario_eliminar = input("Ingrese el nombre del usuario a eliminar: ")
            Usuarios.eliminarUsuario(usuario_eliminar)
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()
