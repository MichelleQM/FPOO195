import sys

from Persona import *

objectPeople= Persona()

while True:
    print("===Menu===")
    print("1. Insertar Persona: ")
    print("2. Consultar todos: ")
    print("3. Buscar una persona: ")
    print("4. Eliminar una persona: ")
    print("5. Editar una persona: ")
    print("6. Salir")
    opcion = input("Elige una opcion: ")
    
    if opcion == "1":
        print("==Ingresar los datos del usuario==")
        id= input("Escribe el Id: ")
        nom= input("Escribe el Nombre: ")
        eda=input("Escribe la edad: ")
        
        objectPeople.Insertar(id,nom,eda)
        print("::Persona Agregada correctamente::")
    elif opcion == "2":
        print(":: Estos son las Personas guardadas ::")
        objectPeople.consultarTodo()
        
    elif opcion == "3":
        print(":: Introduce Id de la persona::")
        id= input("Id: ")
        objectPeople.buscarUsuario(id)
        
    elif opcion == "4":
        print(":: Introduce Id de la persona a eliminar::")
        id= input("Id: ")
        objectPeople.eliminar(id)
        
    elif opcion == "5":
        print (":: Introduce Id de la persona a editar ::")
        id= input("Id: ")
        nm= input("Nombre: ")
        ed= input("Edad: ")
        objectPeople.editar(id,nm,ed)
        
    elif opcion == "6":
        print("Hasta luego!")
        sys.exit()
    else:
        print("Opcion no valida. Intentalo de nuevo.")