import tkinter as tk
from tkinter import messagebox

# IMPORTA LA CLASE para manejo de Cuentas
from ClaseCuenta import *


# para consultar la informacion de la cuenta 
def consultar_saldo():
    numero_cuenta = entry_cuenta.get()
    cuenta = buscar_cuenta(numero_cuenta)
    if cuenta:
        saldo = cuenta.consultar_saldo()
        messagebox.showinfo("Saldo", f"El saldo actual de la cuenta {numero_cuenta} es: ${saldo}")
    else:
        messagebox.showerror("Error", "Cuenta no encontrada.")
        

#Para deposito 
def ingresar_efectivo():
    numero_cuenta = entry_cuenta.get()
    cuenta = buscar_cuenta(numero_cuenta)
    if cuenta:
        monto = float(entry_monto.get())
        cuenta.ingresar_efectivo(monto)
        messagebox.showinfo("Operación Exitosa", f"Se han ingresado ${monto} a la cuenta {numero_cuenta}.")
    else:
        messagebox.showerror("Error", "Cuenta no encontrada.")

# Para retiro 
def retirar_efectivo():
    numero_cuenta = entry_cuenta.get()
    cuenta = buscar_cuenta(numero_cuenta)
    if cuenta:
        monto = float(entry_monto.get())
        resp = cuenta.retirar_efectivo(monto)
        if resp == True:
            messagebox.showinfo("Operación Exitosa", f"Se han retirado ${monto} de la cuenta {numero_cuenta}.")
        else:
            messagebox.showerror("Error", f"Fondos insuficientes en la cuenta {numero_cuenta}.")
    else:
        messagebox.showerror("Error", "Cuenta no encontrada.")


# Para transferir a otra cuenta 
def transferir():
    numero_cuenta_origen = entry_cuenta_origen.get()
    numero_cuenta_destino = entry_cuenta_destino.get()
    monto = float(entry_monto_transferencia.get())
    cuenta_origen = buscar_cuenta(numero_cuenta_origen)
    cuenta_destino = buscar_cuenta(numero_cuenta_destino)
    if cuenta_origen and cuenta_destino:
        resp = cuenta_origen.transferir(cuenta_destino, monto)
        if resp == True:
            messagebox.showinfo("Tranferencia exitosa.", "Se tranfirieron fondos a la cuenta destino")    
        else:
            messagebox.showerror("Error", "Fondos insuficientes en la cuenta de origen.")    
        ventana_transferencia.destroy()
    else:
        messagebox.showerror("Error", "Una o ambas cuentas no fueron encontradas.")


# Metodo para busqueda de una cuenta 
def buscar_cuenta(numero_cuenta):
    for cuenta in listaCuentas:
        if cuenta.numero_cuenta == numero_cuenta:
            return cuenta
    return None


# menu 
def abrir_ventana_transferencia():
    global ventana_transferencia
    ventana_transferencia = tk.Toplevel(root)
    ventana_transferencia.title("Transferir")
    label_cuenta_origen = tk.Label(ventana_transferencia, text="Cuenta Origen:")
    label_cuenta_origen.grid(row=0, column=0, padx=5, pady=5)
    global entry_cuenta_origen
    entry_cuenta_origen = tk.Entry(ventana_transferencia)
    entry_cuenta_origen.grid(row=0, column=1, padx=5, pady=5)
    label_cuenta_destino = tk.Label(ventana_transferencia, text="Cuenta Destino:")
    label_cuenta_destino.grid(row=1, column=0, padx=5, pady=5)
    global entry_cuenta_destino
    entry_cuenta_destino = tk.Entry(ventana_transferencia)
    entry_cuenta_destino.grid(row=1, column=1, padx=5, pady=5)
    label_monto_transferencia = tk.Label(ventana_transferencia, text="Monto:")
    label_monto_transferencia.grid(row=2, column=0, padx=5, pady=5)
    global entry_monto_transferencia
    entry_monto_transferencia = tk.Entry(ventana_transferencia)
    entry_monto_transferencia.grid(row=2, column=1, padx=5, pady=5)
    button_transferir = tk.Button(ventana_transferencia, text="Transferir", command=transferir)
    button_transferir.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="WE")


# ejemplos de cuenta 
listaCuentas = [
    Cuenta("001", "Juan Pérez", 30, 1000),
    Cuenta("002", "María García", 25, 1500),
    Cuenta("003", "Juan Vazquez", 50, 500),
    Cuenta("004", "Pedro Rodriguez", 35, 2500),
    Cuenta("005", "Guadalupe Rosas", 75, 4500),
]

# Ventana principal
root = tk.Tk()
root.title("Operaciones CAJA POPULAR")
frame_consultas = tk.Frame(root)
frame_consultas.pack(padx=10, pady=10)
label_cuenta = tk.Label(frame_consultas, text="Número de Cuenta:")
label_cuenta.grid(row=0, column=0, padx=10, pady=5)
entry_cuenta = tk.Entry(frame_consultas)
entry_cuenta.grid(row=0, column=1, padx=10, pady=5)
button_consultar_saldo = tk.Button(frame_consultas, text="Consultar Saldo", command=consultar_saldo)
button_consultar_saldo.grid(row=1, column=0, columnspan=2, padx=10, pady=5, sticky="WE")
frame_operaciones = tk.Frame(root)
frame_operaciones.pack(padx=10, pady=10)
label_monto = tk.Label(frame_operaciones, text="Monto:")
label_monto.grid(row=0, column=0, padx=5, pady=5)
entry_monto = tk.Entry(frame_operaciones)
entry_monto.grid(row=0, column=1, padx=5, pady=5)
button_ingresar_efectivo = tk.Button(frame_operaciones, text="Ingresar Efectivo", command=ingresar_efectivo)
button_ingresar_efectivo.grid(row=1, column=0, padx=5, pady=5, sticky="WE")
button_retirar_efectivo = tk.Button(frame_operaciones, text="Retirar Efectivo", command=retirar_efectivo)
button_retirar_efectivo.grid(row=1, column=1, padx=5, pady=5, sticky="WE")
button_abrir_transferencia = tk.Button(frame_operaciones, text="Transferir", command=abrir_ventana_transferencia)
button_abrir_transferencia.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="WE")
root.mainloop()
