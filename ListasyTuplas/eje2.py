import tkinter as tk
from tkinter import messagebox, simpledialog

class Serie:
    def __init__(self, titulo, genero="", calificacion=0):
        self.__titulo = titulo
        self.__horas_estimadas = 10
        self.__status = "Sin reproducir"
        self.__genero = genero
        self.__calificacion = calificacion

    def reproducir(self):
        self.__status = "Reproduciendo"
        messagebox.showinfo("Reproducir", f"Reproduciendo {self.__titulo}")

    def agregar_a_mi_lista(self):
        messagebox.showinfo("Agregar a mi lista", f"{self.__titulo} agregado a mi lista")

    def marcar_como_completada(self):
        self.__status = "Completada"
        messagebox.showinfo("Completada", f"{self.__titulo} marcada como completada")

    def calificar(self):
        nueva_calificacion = simpledialog.askinteger("Calificar", "Introduce una calificación (0-10):", minvalue=0, maxvalue=10)
        if nueva_calificacion is not None:
            self.__calificacion = nueva_calificacion
            messagebox.showinfo("Calificación", f"Calificación de {self.__titulo} actualizada a {nueva_calificacion}")

    def _str_(self):
        return f"Título: {self._titulo}, Horas Estimadas: {self.horas_estimadas}, Status: {self.status}, Género: {self.genero}, Calificación: {self._calificacion}"

class SerieApp:
    def _init_(self, master):
        self.master = master
        master.title("Gestor de Series")

        # Input para el título y género de la serie
        self.titulo_label = tk.Label(master, text="Título:")
        self.titulo_entry = tk.Entry(master)
        self.genero_label = tk.Label(master, text="Género:")
        self.genero_entry = tk.Entry(master)

        # Botones para las acciones
        self.crear_btn = tk.Button(master, text="Crear Serie", command=self.crear_serie)
        self.reproducir_btn = tk.Button(master, text="Reproducir", command=self.reproducir, state=tk.DISABLED)
        self.agregar_btn = tk.Button(master, text="Agregar a mi lista", command=self.agregar_a_mi_lista, state=tk.DISABLED)
        self.completar_btn = tk.Button(master, text="Marcar como Completada", command=self.marcar_como_completada, state=tk.DISABLED)
        self.calificar_btn = tk.Button(master, text="Calificar", command=self.calificar, state=tk.DISABLED)

        # Organizar los widgets
        self.titulo_label.grid(row=0, column=0)
        self.titulo_entry.grid(row=0, column=1)
        self.genero_label.grid(row=1, column=0)
        self.genero_entry.grid(row=1, column=1)

        self.crear_btn.grid(row=2, column=0, columnspan=2)
        self.reproducir_btn.grid(row=3, column=0)
        self.agregar_btn.grid(row=3, column=1)
        self.completar_btn.grid(row=4, column=0)
        self.calificar_btn.grid(row=4, column=1)

    def crear_serie(self):
        titulo = self.titulo_entry.get()
        genero = self.genero_entry.get()
        self.serie = Serie(titulo, genero)
        messagebox.showinfo("Serie creada", f"Se ha creado la serie: {titulo}")
        self.reproducir_btn['state'] = tk.NORMAL
        self.agregar_btn['state'] = tk.NORMAL
        self.completar_btn['state'] = tk.NORMAL
        self.calificar_btn['state'] = tk.NORMAL

    def reproducir(self):
        self.serie.reproducir()

    def agregar_a_mi_lista(self):
        self.serie.agregar_a_mi_lista()

    def marcar_como_completada(self):
        self.serie.marcar_como_completada()

    def calificar(self):
        self.serie.calificar()

if __name__ == "_main_":
    root = tk.Tk()
    app = SerieApp(root)
    root.mainloop()