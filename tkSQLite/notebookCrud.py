from tkinter import *
from tkinter import ttk
import tkinter as tk 
from Controlador import *

#7. Se crea un objeto de la clase controlador para acceder a todos los metodos y atributos de la misma 
objControlador=Controlador()

#8. Funcion para los inserts en donde se instancia las funciones de la clase controlador
#desde esta funcion se mandan llamar los datos con un get con los que se declararon los inputs 
def ejecutaInsert():
    objControlador.insertUsuario(var1.get(),var2.get(),var3.get())

#9. se crea una funcion para el boton de busqueda de usuario, y este mismo se declara en una variable de nombre usuarioBD
def buscarUsuario():
    usuarioBD=objControlador.buscarUsuario(varBus.get())
    print(usuarioBD)

#1. Definimos ventana y sus dimenciones 
ventana = Tk()
ventana.title("CRUD Usuarios")
ventana.geometry("500x300")

#2. se crea un panel para la ventana 
panel=ttk.Notebook(ventana)
panel.pack(fill='both', expand='yes')

#3. Definir las pestanas de notebook
pestana1=ttk.Frame(ventana)
pestana2=ttk.Frame(ventana)
pestana3=ttk.Frame(ventana)
pestana4=ttk.Frame(ventana)
pestana5=ttk.Frame(ventana)

#4. Agregamos las pestanas 
panel.add(pestana1, text='Crear Usuario')
panel.add(pestana2, text='Buscar usuario')
panel.add(pestana3, text='Consultar usuarios')
panel.add(pestana4, text='Editar usuario')
panel.add(pestana5, text='Eliminar usuario')


#5. Pestana 1: formulario de insert 
Label(pestana1, text='Registro de Usuarios',fg='blue', font=('modern',18)).pack()

#6. Se asocioan los imput en una variable para que todo aquello que entre ahi se guarde
var1=tk.StringVar()
Label(pestana1,text='Nombre: ').pack()
Entry(pestana1,textvariable=var1).pack()

var2=tk.StringVar()
Label(pestana1,text='Correo: ').pack()
Entry(pestana1,textvariable=var2).pack()

var3=tk.StringVar()
Label(pestana1,text='Contraseña: ').pack()
Entry(pestana1,textvariable=var3).pack()

boton= Button(pestana1,text='Registrar',command=ejecutaInsert)
boton.pack()

#6. Pestana 2: Buscar usuario 
Label(pestana2, text='Buscar Usuario',fg='blue', font=('modern',18)).pack()

varBus=tk.StringVar()
Label(pestana2,text='ID: ').pack()
Entry(pestana2,textvariable=varBus).pack()

boton= Button(pestana2,text='Buscar', command=buscarUsuario)
boton.pack()

Label(pestana2, text='Usuario Registrado',fg='black', font=('modern',14)).pack()
tk.Text(pestana2, height=5, width=52).pack()


ventana.mainloop()
