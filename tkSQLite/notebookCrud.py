from tkinter import *
from tkinter import ttk
import tkinter as tk 
from Controlador import *
from GeneradorPDF import *
import os


#7. Se crea un objeto de la clase controlador para acceder a todos los metodos y atributos de la misma 
objControlador=Controlador()
objPDF=GeneradorPDF()

#8. Funcion para los inserts en donde se instancia las funciones de la clase controlador
#desde esta funcion se mandan llamar los datos con un get con los que se declararon los inputs 
def ejecutaInsert():
    objControlador.insertUsuario(var1.get(),var2.get(),var3.get())

#9. se crea una funcion para el boton de busqueda de usuario, y este mismo se declara en una variable de nombre usuarioBD
#dentro de la funcion para el boton se coloca una validacion la cual indica la infomacion del usuario que se esta buscando en la BD
#Se crea un nueva variable la cual se dara a conocer al widget de text para que la informacion se pueda mostrar ahi, 
#Se usa la funcion de insert la cual se incorpora directo al widget
def buscarUsuario():
    usuarioBD = objControlador.buscarUsuario(varBus.get())
    if txtBuscarUsuario:  
        txtBuscarUsuario.delete('1.0', END)  
        if usuarioBD:
            for usuario in usuarioBD:
                txtBuscarUsuario.insert(END, f"ID: {usuario[0]}, Nombre: {usuario[1]}, Correo: {usuario[2]}\n")
        else:
            txtBuscarUsuario.insert(END, "Usuario no encontrado en Base de datos")
            
#10. Funcion para boton que despliega todos los registros en Base de datos
#El caso fue casi el mismo que para la funcion de busqueda. 
def mostrarRegistros():
    usuariosBD = objControlador.listaUsuariosBD()
    if txtListaUsuarios:
        txtListaUsuarios.delete('1.0', END)
        if usuariosBD:
            for usuario in usuariosBD:
                txtListaUsuarios.insert(END, f"ID: {usuario[0]}, Nombre: {usuario[1]}, Correo: {usuario[2]}, Password:{usuario[3]}\n")
        else:
            txtListaUsuarios.insert(END, "Aun no existen reistros en la Base de datos")
            
def ejecutapdf():
    if varPDF==" ":
        messagebox.showwarning("Importante","Escribe un nombre")
    else:
        objPDF.add_page()
        objPDF.chapter_body()
        objPDF.output(varPDF.get()+".pdf")
        rutaPDF="C:/Users/DEll Gamer G3/Desktop/FPOO195/tkSQLite"+varPDF.get()+".pdf"
        messagebox.showinfo("Archivo Creado","PDF disponible en carpeta")
        os.system(f"start {rutaPDF}")
        
def buscarUsuarioEliminar():
    usuarioBD = objControlador.buscarUsuario(varEli.get())
    if txtElimnarUsuario:
        txtElimnarUsuario.delete('1.0', END)
        if usuarioBD:
            for usuario in usuarioBD:
                txtElimnarUsuario.insert(END, f"ID: {usuario[0]}, Nombre: {usuario[1]}, Correo: {usuario[2]}\n")
        else:
            txtElimnarUsuario.insert(END, "Usuario no encontrado en Base de datos")

def eliminarUsuario():
    objControlador.eliminarUsuario(varEli.get())
    # Limpiar el área de texto después de eliminar el usuario
    txtElimnarUsuario.delete('1.0', END)
    # Opcionalmente, puedes mostrar un mensaje de éxito o realizar otras acciones después de eliminar el usuario

#1. Definimos ventana y sus dimenciones 
ventana = Tk()
ventana.title("CRUD Usuarios")
ventana.geometry("600x400")

#2. se crea un panel para la ventana 
panel=ttk.Notebook(ventana)
panel.pack(fill='both', expand='yes')

#3. Definir las pestanas de notebook
pestana1=ttk.Frame(ventana)
pestana2=ttk.Frame(ventana)
pestana3=ttk.Frame(ventana)
pestana4=ttk.Frame(ventana)
pestana5=ttk.Frame(ventana)
pestana6=ttk.Frame(ventana)

#4. Agregamos las pestanas 
panel.add(pestana1, text='Crear Usuario')
panel.add(pestana2, text='Buscar usuario')
panel.add(pestana3, text='Consultar usuarios')
panel.add(pestana4, text='Editar usuario')
panel.add(pestana5, text='Eliminar usuario')
panel.add(pestana6, text='Reportes en PDF')

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

#7. Pestana 2: Buscar usuario 
Label(pestana2, text='Buscar Usuario',fg='blue', font=('modern',18)).pack()

varBus=tk.StringVar()
Label(pestana2,text='ID: ').pack()
Entry(pestana2,textvariable=varBus).pack()

boton= Button(pestana2,text='Buscar', command=buscarUsuario)
boton.pack()

Label(pestana2, text='Usuario Registrado',fg='black', font=('modern',14)).pack()
txtBuscarUsuario=tk.Text(pestana2, height=5, width=52)
txtBuscarUsuario.pack()

#8. Pestana 3: Listado de usuarios 
Label(pestana3, text='Listado de usuarios', fg='blue', font=('modern', 18)).pack()
boton = Button(pestana3, text='Mostrar usuarios BD', command=mostrarRegistros)
boton.pack()
Label(pestana3, text='Usuarios registrados en Base de Datos', fg='black', font=('modern', 14)).pack()
txtListaUsuarios = tk.Text(pestana3, height=5, width=52)
txtListaUsuarios.pack()

#9. Pestana 4: Editar usuarios 
Label(pestana4, text='Listado de usuarios', fg='blue', font=('modern', 18)).pack()
boton = Button(pestana4, text='Mostrar usuarios BD')
boton.pack()
Label(pestana4, text='Usuarios registrados en Base de Datos', fg='black', font=('modern', 14)).pack()
txtListaUsuarios_editar = tk.Text(pestana4, height=5, width=52)
txtListaUsuarios_editar.pack()

#10. Pestana 5: Eliminar Usuario 
Label(pestana5, text='Busca el usuario a eliminar',fg='blue', font=('modern',18)).pack()

varEli=tk.StringVar()
Label(pestana5,text='ID: ').pack()
Entry(pestana5,textvariable=varEli).pack()  # Corregido el nombre de la variable

botonBuscar = Button(pestana5, text='Buscar', command=buscarUsuarioEliminar)
botonBuscar.pack()

botonEliminar = Button(pestana5, text='Eliminar', command=eliminarUsuario)
botonEliminar.pack()

Label(pestana5, text='Usuario Registrado',fg='black', font=('modern',14)).pack()
txtElimnarUsuario=tk.Text(pestana5, height=5, width=52)
txtElimnarUsuario.pack()  


#11. Pestana 6: Reportes PDF  
Label(pestana6, text='Reportes PDF usuarios', fg='blue', font=('modern', 18)).pack()

varPDF=tk.StringVar()
Label(pestana6,text='Escribe el titulo de tu archivo: ').pack()
Entry(pestana6,textvariable=varPDF).pack()

boton = Button(pestana6, text='Crear PDF', command=ejecutapdf)
boton.pack()


ventana.mainloop()
