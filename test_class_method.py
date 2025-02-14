class Usuario:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __repr__(self):
        """Representación para debugging y desarrollo"""
        return f"Usuario(nombre={repr(self.nombre)}, edad={self.edad})"

    def __str__(self):
        """Representación amigable para usuarios"""
        return f"{self.nombre}, {self.edad} años"

# Creamos una instancia
usuario = Usuario("Marco", 25)

# Usamos print (invoca __str__)
print(usuario)  
# Salida: Marco, 25 años

# Usamos repr() directamente (invoca __repr__)
print(repr(usuario))  
# Salida: Usuario(nombre='Marco', edad=25)

# Mostramos en una lista (repr se usa por defecto en colecciones)
usuarios = [Usuario("Ana", 30), Usuario("Luis", 22)]
print(usuarios)
# Salida: [Usuario(nombre='Ana', edad=30), Usuario(nombre='Luis', edad=22)]
