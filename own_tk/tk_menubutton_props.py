import tkinter as tk
from typing import Callable

class MenubuttonProps:
    def __init__(self, master=None, **kwargs):
        self._default: tuple[str, Callable|None] = ("- Vacío -", None)
        self._opciones: dict[str, Callable|None] = {}
        self._exe_select: Callable = None
        self._opcion: tk.StringVar = tk.StringVar()

        # Inyectamos el textvariable para Tkinter
        kwargs['textvariable'] = self._opcion
        super().__init__(master, **kwargs)

        # Ahora que el widget base existe, le adjuntamos el menú
        self._menu = tk.Menu(self, tearoff=0)
        self.configure(menu=self._menu)

    @property
    def default(self) -> tuple[str, Callable|None]:
        '''Define la opción por defecto si el atributo 'self.opciones' está vacío.'''
        return self._default

    @default.setter
    def default(self, valor: tuple[str, Callable|None]):
        self._default = valor

    @property
    def opciones(self) -> dict[str, Callable|None]:
        '''Diccionario que da forma a las opciones del tk.Menubutton.'''
        return self._opciones

    @opciones.setter
    def opciones(self, opc: dict[str, Callable|None]):
        if not isinstance(opc, dict): 
            raise ValueError("Las opciones deben ser un diccionario no vacío.")
        self._opciones = opc

        # Reconstruimos el menú internamente
        self._menu.delete(0, tk.END)
        for tag, func in self._opciones.items():
            self._menu.add_command(label=tag, command=lambda t=tag, f=func: self._exe_al_seleccionar(t, f))

        if not self._opciones: 
            self.configure(state="disabled")
        else: 
            self.configure(state="normal")

        claves = list(self._opciones.keys())
        sel_actual = self._opcion.get()

        if not claves or self._default[0] in claves: 
            self.opcion = self._default[0]
        elif sel_actual in claves: 
            self.opcion = sel_actual
        else: 
            self.opcion = claves[0]

    @property
    def opcion(self) -> str:
        '''Opcion escrita en el tk.Stringvar asignado como textvariable al tk.Menubutton.'''
        return self._opcion.get()

    @opcion.setter
    def opcion(self, opc: str):
        self._opcion.set(opc)

    @property
    def exe_opcion(self) -> Callable:
        '''Función que se ejecutará cada vez que se seleccione una opción independiente de cual esta sea.'''
        return self._exe_select
    
    @exe_opcion.setter
    def exe_opcion(self, exe: Callable):
        if not isinstance(exe, Callable): 
            raise ValueError("El ejecutable de la opción debe ser una función 'Callable'.")
        self._exe_select = exe