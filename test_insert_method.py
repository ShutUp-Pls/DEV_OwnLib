import own
import random
import string

from datetime import datetime, timedelta

def generate_random_tuples(count: int) -> list[tuple]: #(Nombre, Número, Fecha, Genero, Código)
    return [
        (
            "".join(random.choices(string.ascii_letters, k=random.randint(3, 8))),
            f"{random.randint(1000000, 28000000)}-{random.choice(list(map(str, range(10))) + ['k'])}",
            (date := datetime.today() - timedelta(days=random.randint(0, 365 * 100))).strftime("%d/%m/%Y"),
            random.choice(["F", "M"]),
            "".join(random.choices(string.ascii_letters + string.digits, k=8))
        )
        for _ in range(count)
    ]

def generate_type_dict(tuple_list): #{col:tuple}
    if not tuple_list: return {}
    return {i: row for i, row in enumerate(tuple_list)}

# Crear ventana principal
root = own.tk.Tk()
root.title("Ejemplo de ttk.Treeview con estructura de datos")

crono = own.Crono(verbose=False)

# Datos de ejemplo
print("\nGenerando tuplas 1...")
crono.checkpoint()
datos_tuplas = generate_random_tuples(1000000)
crono.checkpoint(verbose=True)
print(f"Cantidad de tuplas generadas: {len(datos_tuplas)}")

print("\nGenerando Diccionario 1...")
crono.checkpoint()
datos_diccionario = generate_type_dict(datos_tuplas)
crono.checkpoint(verbose=True)
print(f"Largo Diccionario de tuplas generado: {len(datos_diccionario)}")

# Crear Treeview
columnas = ["Nombre", "Número", "Fecha", "Genero", "Código"]  # Obtiene la primera tupla
print(f"\nTotal de columnas: {len(columnas)}")
tree = own.ttk.Treeview(root, columns=columnas, show="headings")

# Configurar encabezados de columnas
print("\nPosicionando columnas...")
crono.checkpoint()
for col in columnas:
    tree.heading(col, text=f"Columna {col}")
    tree.column(col, width=100)
crono.checkpoint(verbose=True)

# Insertar datos en el Treeview
print("\nPoniendo filas al Treeview antes del Pack...")
crono.checkpoint()
for iid, valores in datos_diccionario.items(): tree.insert("", "end", iid=iid, values=valores)
crono.checkpoint(verbose=True)

tree.pack(padx=10, pady=10, expand=True, fill="both")

def function_after():
    # Datos de ejemplo
    print("\nGenerando tuplas 2...")
    crono.checkpoint()
    datos_tuplas = generate_random_tuples(1000000)
    crono.checkpoint(verbose=True)
    print(f"Cantidad de tuplas generadas: {len(datos_tuplas)}")

    print("\nGenerando Diccionario 2...")
    crono.checkpoint()
    datos_diccionario = generate_type_dict(datos_tuplas)
    crono.checkpoint(verbose=True)
    print(f"Largo Diccionario de tuplas generado: {len(datos_diccionario)}")

    print("\nBorrando filas actuales del Treeview...")
    crono.checkpoint()    
    tree.delete(*tree.get_children())
    crono.checkpoint(verbose=True)

    # Insertar datos en el Treeview
    print("\nPoniendo filas al Treeview despúes del Pack...")
    crono.checkpoint()
    for iid, valores in datos_diccionario.items(): tree.insert("", "end", iid=iid, values=valores)
    crono.checkpoint(verbose=True)

root.after(1000, function_after)

# Iniciar loop de la interfaz
root.mainloop()