import tkinter as tk
from tkinter import ttk

# Crear ventana principal
root = tk.Tk()
root.geometry("400x300")

# Crear Treeview
tree = ttk.Treeview(root, columns=("Nombre", "Edad"), show="headings")
tree.heading("Nombre", text="Nombre")
tree.heading("Edad", text="Edad")
tree.pack(fill="both", expand=True)

# Insertar elementos con un iid específico
tree.insert("", "end", iid="item1", values=("Marco", 25))
tree.insert("", "end", iid="item2", values=("Ana", 30))
tree.insert("", "end", iid="item3", values=("Carlos", 40))

# Función para eliminar un elemento por iid
def eliminar_elemento(iid):
    if iid in tree.get_children():  # Verificar si el iid existe
        tree.delete(iid)

# Eliminar un elemento después de 2 segundos
root.after(2000, lambda: eliminar_elemento("item2"))

root.mainloop()
