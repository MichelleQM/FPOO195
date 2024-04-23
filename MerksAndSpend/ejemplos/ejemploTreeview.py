import tkinter as tk
from tkinter import ttk

root = tk.Tk()

# Crear el Treeview
tree = ttk.Treeview(root)
tree["columns"] = ("1", "2", "3")
tree.column("#0", width=50)  # Establecer el ancho de la columna principal
tree.heading("#0", text="Name")
tree.column("1", width=100)
tree.heading("1", text="Column 1")
tree.column("2", width=100)
tree.heading("2", text="Column 2")
tree.column("3", width=100)
tree.heading("3", text="Column 3")

# Insertar datos de ejemplo
for i in range(10):
    tree.insert("", "end", text=f"{i}", values=(f"value {i}", f"value {i}", f"value {i}"))

tree.pack()

# Ejecutar la aplicación
root.mainloop()
