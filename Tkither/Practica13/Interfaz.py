import tkinter as tk
from tkinter import messagebox
from clase import *

    #Se crea una clase con los widgets para la creacion de la intefaz usando Tkinter 
class winGeneradorContrasena:
    def __init__(self, ventana):
        print (" Se ha creado un objeto de la clase winGeneradorContrasena")
        self.ventana = ventana
        ventana.title("Generador de Contraseñas")

        self.intLongitud_label = tk.Label(ventana, text="Longitud de la Contraseña:")
        self.intLongitud_label.pack()

        self.intLongitud_entry = tk.Entry(ventana)
        self.intLongitud_entry.pack()

        self.generate_button = tk.Button(ventana, text="Generar Contraseña", command=self.cmdGeneraPassword)
        self.generate_button.pack()

        self.passEntry = tk.Entry(ventana, text="")
        self.passEntry.pack()


    def cmdGeneraPassword(self):
        objGenerador = clase()
        respuesta = messagebox.askquestion("Pregunta", "¿Quieres incluir mayusculas?")
        if respuesta == "yes":
            blnIncluyeMayusculas = True
        else:
            blnIncluyeMayusculas = False            
        respuesta = messagebox.askquestion("Pregunta", "¿Quieres incluir caracteres especiales?")
        if respuesta == "yes":
            blnIncluyeCaracteresEspeciales = True
        else:
            blnIncluyeCaracteresEspeciales = False            

        try:
            #aqui se optiene la longitud designada por el usuario en donde si la contrasena es menor a 8 el programa arroja un mensaje de error 
            intLongitud = int(self.intLongitud_entry.get())
            if intLongitud <= 7:
                raise ValueError("La longitud debe ser un número positivo mayor que ocho")

            #se crea un objeto de tipo password con los atributos seleccionados por el usuario en donde si selecciona mayusculas y caracter especial 
            password = objGenerador.GeneraContrasena(intLongitud, blnIncluyeMayusculas, blnIncluyeCaracteresEspeciales)

            # Aqui se muestra la contra generada en un cuadro de texto para que pueda ser copiada por el usuario 
            self.passEntry.delete(0, tk.END)
            self.passEntry.insert(0, password)
            strFortaleza = objGenerador.VerificaFortalezaContrasena(password)
            messagebox.showinfo ("Fortaleza del password generado", strFortaleza)
        except ValueError as e:
            messagebox.showerror("Error", str(e))


ventana = tk.Tk()
ventana.geometry("350x150")
app = winGeneradorContrasena(ventana)
ventana.mainloop()
