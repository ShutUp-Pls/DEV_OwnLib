import tkinter as tk
from typing import Callable
from .tk_menubutton_props import MenubuttonProps

class Menubutton(MenubuttonProps, tk.Menubutton):
    
    def __init__(self, master, default: tuple[str, Callable] = ("- Vacío -", None), opciones: dict[str, Callable|None] = None, **kwargs):
        '''tk.Menubutton configurable a través de un diccionario de la forma 'dict[str,Callable|None]'.'''
        if opciones is None: opciones = {}

        super().__init__(master, **kwargs)

        self.default = default
        self.opciones = opciones

    def _exe_al_seleccionar(self, tag: str, func: Callable|None):
        '''Función anclada por defecto a cada opción del tk.Menubutton. Ejecuta una acción por defecto y luego la función externa definidia si es que tiene.'''
        self.opcion = tag
        if func: func()

        if self.exe_opcion: self.exe_opcion()