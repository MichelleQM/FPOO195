import tkinter as tk
from tkinter import messagebox

class winGeneradorMatricula:
    def __init__(self, ventana):
        self.ventana = ventana
        ventana.title("Generador de Matriculas")

        self.nombre_label = tk.Label(ventana, text="Ingresa el Nombre:")
        self.nombre_label.pack()

        self.nombre_entry = tk.Entry(ventana)
        self.nombre_entry.pack()
        
        self.apellidoP_label = tk.Label(ventana, text="Ingresa el Apellido Paterno:")
        self.apellidoP_label.pack()

        self.apellidoP_entry = tk.Entry(ventana)
        self.apellidoP_entry.pack()
        
        self.apellidoM_label = tk.Label(ventana, text="Ingresa el Apellido Materno:")
        self.apellidoM_label.pack()

        self.apellidoM_entry = tk.Entry(ventana)
        self.apellidoM_entry.pack()
        
        self.nacimiento_label = tk.Label(ventana, text="Ingresa el Año de nacimiento:")
        self.nacimiento_label.pack()

        self.nacimiento_entry = tk.Entry(ventana)
        self.nacimiento_entry.pack()
        
        self.carrera_label = tk.Label(ventana, text="Ingresa la carrera:")
        self.carrera_label.pack()

        self.carrera_entry = tk.Entry(ventana)
        self.carrera_entry.pack()
        
        self.generate_button = tk.Button(ventana, text="Generar Matricula", command=self.matriculaGenerada)
        self.generate_button.pack()
        
    def matriculaGenerada(self):
        #objdatosMatricula=matricula()
        messagebox.showinfo("Matricula", "Tu matricula generada es: ")

ventana = tk.Tk()
ventana.geometry("600x400")
app = winGeneradorMatricula(ventana)
ventana.mainloop()