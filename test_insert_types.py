import tkinter as tk
from tkinter import ttk

def check_selected_values():
    selected_item = tree.selection()  # Obtener el ID de la fila seleccionada
    if not selected_item:
        print("No hay ninguna fila seleccionada.")
        return
    
    values = tree.item(selected_item)["values"]
    print(f"\nValores de la fila seleccionada: {values}")
    for i, value in enumerate(values): print(f"Columna {i+1}: {value} ({type(value).__name__})")

def check_selected_values_():
    selected_items = tree.selection()  # Obtener IDs de filas seleccionadas
    if not selected_items:
        print("No hay ninguna fila seleccionada.")
        return
    
    for item in selected_items:
        values = tree.item(item)["values"]
        print(f"\nValores de la fila {item}: {values}")
        for i, value in enumerate(values):
            print(f"  Columna {i+1}: {value} ({type(value).__name__})")

def check_selected_values_():
    selected_item = tree.selection()
    if not selected_item:
        print("No hay ninguna fila seleccionada.")
        return
    
    values_dict = tree.set(selected_item)  # Devuelve un diccionario {columna: valor}
    print(f"\nValores de la fila seleccionada (dict): {values_dict}")

    for column, value in values_dict.items():
        print(f"Columna '{column}': {value} ({type(value).__name__})")


# Crear ventana principal
root = tk.Tk()
root.title("Prueba de Treeview con None")

# Crear Treeview
columns = ("Col1", "Col2", "Col3")
tree = ttk.Treeview(root, columns=columns, show="headings")

# Configurar encabezados
for col in columns:
    tree.heading(col, text=col)

tree.insert("", "end", iid="row_objects", values=(True, False, None))
tree.insert("", "end", iid="row_numbers", values=(1/2, 321, 1.23))
tree.insert("", "end", iid="row_incomplete", values=("Dato2", "Dato3", 3.0))
tree.insert("", "end", iid="row_structures_empty", values=([], (), {}))
tree.insert("", "end", iid="row_structures_fill", values=([1,2,3], (1,2,3,4,5), {"id":"valor"}))

# Botón para consultar valores de la fila con None
btn_check = tk.Button(root, text="Comprobar valores None", command=check_selected_values)
btn_check.pack()

# Empaquetar Treeview
tree.pack()

# Ejecutar ventana
root.mainloop()
