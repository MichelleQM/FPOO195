from tkinter import Tk, Frame, Button, messagebox

#Metodos para mensaje 
def mostrarMensajes():
    print(messagebox.showinfo('showinfo','Information'))
    print(messagebox.showerror('showerror','Error'))
    print(messagebox.showwarning('showwarning','Warning'))
    print(messagebox.askquestion(message="Desea continuar?", title="Soy el titulo"))
    
def addbtn():
    botonVerde.config(text='+')
    botonRosa = Button(seccion3, text="Nuevo", bg="pink", fg="white")
    botonRosa.configure(height=3, width=5)
    botonRosa.pack()

#1. Creamos la ventana
Ventana= Tk() #Uso de POO creando un obj Ventana 
Ventana.title("Ejemplo con 3 Frames")
Ventana.geometry("600x400")

#2. Colocamos Frames de la ventana 
seccion1= Frame(Ventana, bg="blue")
seccion1.pack(expand= True, fill= 'both')

seccion2= Frame(Ventana, bg="gray")
seccion2.pack(expand= True, fill= 'both')

seccion3= Frame(Ventana, bg="green")
seccion3.pack(expand= True, fill= 'both')

#3. Agrgar botones 
#Place
botonAzul = Button(seccion1, text="Azul", bg="black", fg="white")
botonAzul.place(x=60, y=60, width=100, height=30)

#Grid
botonNegro = Button(seccion2, text="Negro", bg="pink", fg="black")
botonNegro.configure(height=2, width=10)
botonNegro.grid(row=0, column=1)

botonAmarillo = Button(seccion2, text="Amarillo", bg="red", fg="green", command=mostrarMensajes)
botonAmarillo.configure(height=2, width=10)
botonAmarillo.grid(row=1, column=2)

#Pack
botonVerde = Button(seccion3, text="Verde", bg="violet", fg="white", command=addbtn)
botonVerde.configure(height=2, width=10)
botonVerde.pack()

botonVerde2 = Button(seccion3, text="Verde", bg="violet", fg="white")
botonVerde2.configure(height=2, width=10)
botonVerde2.pack()


#Ejecuta es un metodo para ejecutar 
Ventana.mainloop()

