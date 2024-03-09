from tkinter import Tk, Frame, messagebox, Button, Entry, usuario, contra

#Metodo login 
class login:
    def __init__(self):
        self.__usuarios = {"usuario": "contra"}

    def __validacion(self, usuario, contra):
        if usuario in self.__usuarios and self.__usa[usuario] == contra:
            return True
        return False

    def login(self, user, password):
        if self.__validacion(user, password):
            print(messagebox.showinfo('Bienvenido'))
        else:
            print(messagebox.showerror('Revisa tus credenciales'))
            


ventanalogin = Tk()
ventanalogin.title("Ventana login")
ventanalogin.geometry("600x400")

secclogin = Frame(ventanalogin, bg="white smoke")
self.__Entry=(text="Usuario", bg="gray", fg="black")
self. __Entry=(text="Contraseña", bg="gray", fg="black")
Entry.pack()
secclogin.pack(expand=True, fill='both')

seccboton = Frame(ventanalogin, bg="white smoke")
seccboton.pack(expand=True, fill='both')


botonValidar = Button(seccboton, text="Ingresar", bg="blue", fg="white", command=login)
botonValidar.configure(height=2, width=10)
botonValidar.pack()

ventanalogin.mainloop()


