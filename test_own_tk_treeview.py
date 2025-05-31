import own

# DEMO: Uso de la clase OwnTreeview
def demo():
    root = own.tk.Tk()
    root.title("Demo OwnTreeview")
    root.geometry("500x400")

    frame = own.tk.Frame(root)
    frame.pack(pady=10, padx=10, fill="both", expand=True)

    # Crear instancia de OwnTreeview
    tree = own.OwnTreeview(frame, show="headings")
    tree.pack(pady=10, padx=10, fill="both", expand=True)
    tree.columns = ("ID", "Nombre", "Edad")

    # Datos iniciales
    tree.data = {
        "1": ("1", "Alice", 25),
        "2": ("2", "Bob", 30),
        "3": ("3", "Charlie", 22),
    }

    # Funciones para botones
    def agregar_fila():
        row_len = len(tree)
        id_nuevo = str(row_len + 1)
        tree[id_nuevo] = (id_nuevo, f"Persona {id_nuevo}", 20 + row_len)

    def eliminar_fila():
        tree.selection_del()

    # Botones
    btn_frame = own.tk.Frame(root)
    btn_frame.pack(expand=True, fill=own.tk.BOTH)

    btn_add = own.tk.Button(btn_frame, text="Agregar Fila", command=agregar_fila)
    btn_add.pack(padx=5)

    btn_del = own.tk.Button(btn_frame, text="Eliminar Seleccionado", command=eliminar_fila)
    btn_del.pack(padx=5)

    root.mainloop()


if __name__ == "__main__":
    demo()