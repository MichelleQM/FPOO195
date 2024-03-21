from tkinter import *
from tkinter import ttk
import tkinter as tk 

ventana = Tk()
ventana.title("CRUD Usuarios")
ventana.geometry("500x300")

#2. 
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


ventana.mainloop()
