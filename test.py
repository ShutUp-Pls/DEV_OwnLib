import tkinter as tk

root = tk.Tk()
root.title("MenuButton dinámico")

# Variable para el texto del botón
opcion_actual = tk.StringVar(value="Selecciona una opción")

# Crear el MenuButton con texto dinámico
menu_button = tk.Menubutton(root, textvariable=opcion_actual, relief=tk.RAISED)
menu_button.grid(padx=20, pady=20)

# Crear el menú
menu = tk.Menu(menu_button, tearoff=0)

# Función para actualizar la opción
def seleccionar(opcion):
    opcion_actual.set(opcion)
    print(f"Elegiste: {opcion}")

# Agregar opciones
menu.add_command(label="Opción 1", command=lambda: seleccionar("Opción 1"))
menu.add_command(label="Opción 2", command=lambda: seleccionar("Opción 2"))
menu.add_separator()
menu.add_command(label="Salir", command=root.quit)

# Asociar menú al botón
menu_button.config(menu=menu)

root.mainloop()
