# OwnLin

Librería colección de reutilizaciones para el desarrollo en python.

## 1) ownTk

### Descripción
Este modulo es una colección de componentes personalizados para el framework Tkinter, diseñados bajo el principio de reutilización de código y herencia de clases. El objetivo principal es estandarizar la interfaz de usuario en múltiples proyectos, encapsulando comportamientos comunes y extendiendo las capacidades de los widgets nativos de Python.

### Características Técnicas
* **Arquitectura basada en Clases:** Todos los widgets heredan de `tk.Frame` o widgets específicos, permitiendo una integración transparente como componentes independientes.
* **Encapsulamiento:** Lógica de eventos y estilos configurada internamente para mantener el código del proyecto principal limpio.
* **Extensibilidad:** Los componentes aceptan `*args` y `**kwargs` para mantener compatibilidad total con las opciones estándar de Tkinter.

### Estructura del Proyecto
```text
DEV_OwnLib/
├── ownTk/                 # Paquete principal
│   ├── __init__.py         
│   ├── widget_1.py         # Widget y funcionalidades
│   ├── widget_2.py
│   ├── widget_2_props.py   # Algunos widgets separan sus atributos
│   ├── func_1.py         
│   └── ...
├── pyproject.toml          # Configuración de empaquetado moderno
├── setup.py                # Compatibilidad con instalaciones heredadas
├── requirements.txt        # Librerías Python requeridas
└── README.md
```

### Instalación

Para utilizar esta librería en sus proyectos de desarrollo, puede instalarla directamente desde este repositorio de GitHub utilizando `pip`:

```bash
pip install git+https://github.com/ShutUp-Pls/DEV_OwnLib
```

### Ejemplo de Uso

A continuación se muestra cómo integrar un widget de esta librería en una aplicación estándar de Tkinter:

```python
import ownTk as own

class Aplicacion(own.Tk):
    def __init__(self):
        super().__init__()
        self.title("Proyecto Principal")
        self.geometry("400x300")
        
        # Instanciación del widget personalizado
        self.btn = own.Button(self, text="Acción", command=self.ejecutar)
        self.btn.pack(pady=20)

    def ejecutar(self):
        print("Widget reutilizable funcionando correctamente")

if __name__ == "__main__":
    app = Aplicacion()
    app.mainloop()
```

## 2) ownPg

### Descripción
Al igual que su contraparte visual, este módulo está diseñado para estandarizar y simplificar la interacción con bases de datos PostgreSQL utilizando `psycopg2`. Encapsula la gestión de conexiones, cursores y el manejo de excepciones, permitiendo mantener la lógica de base de datos de tus proyectos limpia, reutilizable y tolerante a fallos.

### Características Técnicas
* **Gestión de Estado Interno:** Administra automáticamente el ciclo de vida del cursor y la conexión, extrayendo metadatos dinámicos como las bases de datos y tablas disponibles al momento de conectarse.
* **Verbosidad Configurable:** Permite derivar las alertas y errores de conexión de forma silenciosa, hacia la consola, o mediante ventanas emergentes (`tkinter.messagebox`), sin necesidad de ensuciar el código principal con bloques `try-except`.
* **Separación de Responsabilidades:** Utiliza el mismo patrón arquitectónico de `ownTk`, separando las propiedades (`Props`) de los métodos de ejecución para una alta legibilidad del código.

### Ejemplo de Uso

A continuación se muestra cómo gestionar una conexión a PostgreSQL usando el objeto estandarizado:

```python
import ownPg as pg

# Instanciamos el administrador de conexión
db = pg.Conexion()

# Configuramos la verbosidad: (imprimir en consola, NO mostrar popup en GUI)
db.verbose = (True, False)

# Establecemos la conexión usando el setter (acepta un diccionario de credenciales)
db.conexion = {
    "host": "localhost",
    "user": "postgres",
    "password": "mi_password_seguro",
    "port": "5432"
}

# Verificamos que la conexión esté activa
if db.conexion:
    print("Bases de datos disponibles:", db.databases)
    
    # Al asignar la base de datos, automáticamente refresca las tablas disponibles
    db.database = "mi_proyecto_db"
    print("Tablas en la BD:", db.tablas)

# Limpieza segura de cursores y cierre de conexión
db.desconectarse()

```

## Autor
* **Marco Delgado**