class TrackedDict(dict):
    def __setitem__(self, key, value):
        print(f"🔹 SET: {key} -> {value}")
        super().__setitem__(key, value)

    def __getitem__(self, key):
        value = super().__getitem__(key)
        print(f"🔸 GET: {key} -> {value}")
        return value

    def __delitem__(self, key):
        print(f"❌ DELETE: {key}")
        super().__delitem__(key)

# Prueba
# Instancia de TrackedDict
d = TrackedDict()

# Insertando diferentes tipos de valores
d["nombre"] = "Marco"       # 🔹 SET: nombre -> Marco
d[42] = "Número"            # 🔹 SET: 42 -> Número
d[("x", "y")] = [1, 2, 3]   # 🔹 SET: ('x', 'y') -> [1, 2, 3]
d[3.14] = {"pi": 3.14}      # 🔹 SET: 3.14 -> {'pi': 3.14}

# Accediendo a los valores
print(d["nombre"])   # 🔸 GET: nombre -> Marco
print(d[42])         # 🔸 GET: 42 -> Número
print(d[("x", "y")]) # 🔸 GET: ('x', 'y') -> [1, 2, 3]
print(d[3.14])       # 🔸 GET: 3.14 -> {'pi': 3.14}

# Modificando valores existentes
d["nombre"] = "Carlos"       # 🔹 SET: nombre -> Carlos
d[42] = "Otro número"        # 🔹 SET: 42 -> Otro número
d[("x", "y")].append(4)      # 🔸 GET: ('x', 'y') -> [1, 2, 3] (antes de modificar)
print(d[("x", "y")])         # 🔸 GET: ('x', 'y') -> [1, 2, 3, 4] (después de modificar)

print("Diccionario previo eliminar:", d)

# Eliminando algunos elementos
del d[42]         # ❌ DELETE: 42
del d[3.14]       # ❌ DELETE: 3.14

# Ver el diccionario final
print("Diccionario final:", d)
