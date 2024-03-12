import tkinter as tk
from tkinter import messagebox
from math import gcd

class Fraccion:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador if denominador != 0 else 1

    def simplificar(self):
        divisor_comun = gcd(self.numerador, self.denominador)
        self.numerador //= divisor_comun
        self.denominador //= divisor_comun

    def sumar(self, otra):
        nuevo_numerador = self.numerador * otra.denominador + self.denominador * otra.numerador
        nuevo_denominador = self.denominador * otra.denominador
        resultado = Fraccion(nuevo_numerador, nuevo_denominador)
        resultado.simplificar()
        return resultado

    def restar(self, otra):
        nuevo_numerador = self.numerador * otra.denominador - self.denominador * otra.numerador
        nuevo_denominador = self.denominador * otra.denominador
        resultado = Fraccion(nuevo_numerador, nuevo_denominador)
        resultado.simplificar()
        return resultado

    def multiplicar(self, otra):
        nuevo_numerador = self.numerador * otra.numerador
        nuevo_denominador = self.denominador * otra.denominador
        resultado = Fraccion(nuevo_numerador, nuevo_denominador)
        resultado.simplificar()
        return resultado

    def dividir(self, otra):
        nuevo_numerador = self.numerador * otra.denominador
        nuevo_denominador = self.denominador * otra.numerador
        resultado = Fraccion(nuevo_numerador, nuevo_denominador)
        resultado.simplificar()
        return resultado

    def _str_(self):
        return f"{self.numerador}/{self.denominador}"

class FraccionApp:
    def _init_(self, master):
        self.master = master
        master.title("Operaciones con Fracciones")

        # Inputs para la primera fracción
        self.num1_label = tk.Label(master, text="Numerador 1:")
        self.num1_entry = tk.Entry(master)
        self.den1_label = tk.Label(master, text="Denominador 1:")
        self.den1_entry = tk.Entry(master)

        # Inputs para la segunda fracción
        self.num2_label = tk.Label(master, text="Numerador 2:")
        self.num2_entry = tk.Entry(master)
        self.den2_label = tk.Label(master, text="Denominador 2:")
        self.den2_entry = tk.Entry(master)

        # Botones para las operaciones
        self.sumar_btn = tk.Button(master, text="Sumar", command=self.sumar)
        self.restar_btn = tk.Button(master, text="Restar", command=self.restar)
        self.multiplicar_btn = tk.Button(master, text="Multiplicar", command=self.multiplicar)
        self.dividir_btn = tk.Button(master, text="Dividir", command=self.dividir)

        # Organizar los widgets en la ventana
        self.num1_label.grid(row=0, column=0)
        self.num1_entry.grid(row=0, column=1)
        self.den1_label.grid(row=1, column=0)
        self.den1_entry.grid(row=1, column=1)
        self.num2_label.grid(row=2, column=0)
        self.num2_entry.grid(row=2, column=1)
        self.den2_label.grid(row=3, column=0)
        self.den2_entry.grid(row=3, column=1)

        self.sumar_btn.grid(row=4, column=0)
        self.restar_btn.grid(row=4, column=1)
        self.multiplicar_btn.grid(row=4, column=2)
        self.dividir_btn.grid(row=4, column=3)

    def crear_fraccion_desde_entrada(self, num_entry, den_entry):
        try:
            numerador = int(num_entry.get())
            denominador = int(den_entry.get())
            if denominador == 0:
                messagebox.showerror("Error", "El denominador no puede ser cero.")
                return None
            return Fraccion(numerador, denominador)
        except ValueError:
            messagebox.showerror("Error", "Por favor, introduce solo números enteros.")
            return None

    def operacion(self, operador):
        fraccion1 = self.crear_fraccion_desde_entrada(self.num1_entry, self.den1_entry)
        fraccion2 = self.crear_fraccion_desde_entrada(self.num2_entry, self.den2_entry)

        if fraccion1 and fraccion2:
            resultado = operador(fraccion1, fraccion2)
            messagebox.showinfo("Resultado", str(resultado))

    def sumar(self):
        self.operacion(Fraccion.sumar)

    def restar(self):
        self.operacion(Fraccion.restar)

    def multiplicar(self):
        self.operacion(Fraccion.multiplicar)

    def dividir(self):
        self.operacion(Fraccion.dividir)

if __name__ == "_main_":
    root = tk.Tk()
    app = FraccionApp(root)
    root.mainloop()