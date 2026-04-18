# ownTK

---

## Descripción
Esta librería es una colección de componentes personalizados para el framework Tkinter, diseñados bajo el principio de reutilización de código y herencia de clases. El objetivo principal es estandarizar la interfaz de usuario en múltiples proyectos, encapsulando comportamientos comunes y extendiendo las capacidades de los widgets nativos de Python.

## Características Técnicas
* **Arquitectura basada en Clases:** Todos los widgets heredan de `tk.Frame` o widgets específicos, permitiendo una integración transparente como componentes independientes.
* **Encapsulamiento:** Lógica de eventos y estilos configurada internamente para mantener el código del proyecto principal limpio.
* **Extensibilidad:** Los componentes aceptan `*args` y `**kwargs` para mantener compatibilidad total con las opciones estándar de Tkinter.

## Estructura del Proyecto
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

## Instalación

Para utilizar esta librería en sus proyectos de desarrollo, puede instalarla directamente desde este repositorio de GitHub utilizando `pip`:

```bash
pip install git+https://github.com/ShutUp-Pls/DEV_OwnLib
```

## Ejemplo de Uso

A continuación se muestra cómo integrar un widget de esta librería en una aplicación estándar de Tkinter:

```python
import ownTk as own

class Aplicacion(tk.Tk):
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
## Autor
* **Marco Delgado**