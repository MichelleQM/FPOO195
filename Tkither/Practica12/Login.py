from tkinter import Tk, Frame, Button, Label, messagebox, Entry
import tkinter as tk

class login:
    def crearLogin(self,objPeople):
        
        def ejecutaValidacion():
            status=objPeople.validarUsuario(var1.get(),var2.get())
            if(status):
                print(messagebox.showwarning('Bienvenido','Acceso concedido'))
            else:
                print(messagebox.showerror('Error','Usuario no encontrado'))
            
        Ventana=Tk()
        Ventana.title("Login Persona")
        Ventana.geometry("600x400")
        
        seccion1=Frame(Ventana)
        seccion1.pack(expand=True, fill='both')
        
        Label(seccion1,text='login FPOO',bg='white',font=('mono,18')).pack()
        
        var1=tk.StringVar()
        Label(seccion1,text='Usuario: ',font=('Heletica',14)).pack
        Entry(seccion1,takefocus=True, textvariable=var1).pack
        
        var2=tk.StringVar()
        Label(seccion1,text='Contrasena: ',font=('Heletica',14)).pack
        Entry(seccion1,show='+', textvariable=var2).pack
        
        botonAcceso=Button(seccion1, text='Acceder',command=ejecutaValidacion)
        botonAcceso.pack()
        
        Ventana.mainloop()
