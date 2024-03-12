import tkinter as tk
from tkinter import messagebox
from matricula import *

class winGeneradorMatricula:
    def __init__(self, ventana):
        self.ventana = ventana
        ventana.title("Generador de Matriculas")

        self.nombre_label = tk.Label(ventana, text="Ingresa el Nombre:")
        self.nombre_label.pack()

        self.intLongitud_entry = tk.Entry(ventana)
        self.intLongitud_entry.pack()
        
        self.intLongitud2_label = tk.Label(ventana, text="Ingresa el Apellido Paterno:")
        self.intLongitud2_label.pack()

        self.intLongitud2_entry = tk.Entry(ventana)
        self.intLongitud2_entry.pack()
        
        self.intLongitud_label = tk.Label(ventana, text="Ingresa el Apellido Materno:")
        self.intLongitud3_label.pack()

        self.intLongitud3_entry = tk.Entry(ventana)
        self.intLongitud3_entry.pack()
        
        self.intLongitud4_label = tk.Label(ventana, text="Ingresa el Año de nacimiento:")
        self.intLongitud4_label.pack()

        self.intLongitud4_entry = tk.Entry(ventana)
        self.intLongitud4_entry.pack()
        
        self.intLongitud5_label = tk.Label(ventana, text="Ingresa la carrera:")
        self.intLongitud5_label.pack()

        self.intLongitud5_entry = tk.Entry(ventana)
        self.intLongitud5_entry.pack()
        
        self.generate_button = tk.Button(ventana, text="Generar Matricula")
        self.generate_button.pack()
        
    def matriculaGenerada(self):
        objdatosMatricula=matricula()
        messagebox.showinfo("Matricula", "Tu matricula generada es: ",matricula)
        
ventana = tk.Tk()
ventana.geometry("600x400")
app = winGeneradorMatricula(ventana)
ventana.mainloop()