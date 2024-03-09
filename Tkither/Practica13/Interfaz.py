import tkinter as tk
from tkinter import Tk, messagebox, Button

def mostrarMensajes():
    print(messagebox.askquestion(message="Deseas incluir Mayusculas en tu contrasena?", title="Mayusculas"))

Ventana=Tk()
Ventana.title("Generador de Contraseñas")
Ventana.geometry("600x400")

longitudEtiqueta = tk.Label(Ventana, text="Longitud:")
longitudEtiqueta.pack()

logitud = tk.Entry(Ventana)
logitud.insert(0, "8")
logitud.pack()

botonGenerar=tk.Button(logitud,text="Generar Contraseña" command=mostrarMensajes)
botonGenerar.pack()

contra_entry = tk.Entry(Ventana, show="*")
contra_entry.pack()

Ventana.mainloop()