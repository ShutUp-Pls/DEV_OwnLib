import tkinter as tk
from typing import Callable

class LabelProps:
    def __init__(self, master=None, **kwargs):
        self._texto: tk.StringVar = tk.StringVar()
        self._exe_al_escribir: Callable = None
        
        kwargs['textvariable'] = self._texto
        super().__init__(master, **kwargs)

    @property
    def texto(self) -> str:
        return self._texto.get()
    
    @texto.setter
    def texto(self, txt: str):
        if not isinstance(txt, str): 
            raise ValueError("El valor asignado al 'own.Label.texto' debe ser una cadena de texto 'str'.")
        if self._exe_al_escribir: 
            self._exe_al_escribir()
        self._texto.set(txt)

    @property
    def exe_escritura(self) -> Callable:
        return self._exe_al_escribir
    
    @exe_escritura.setter
    def exe_escritura(self, exe: Callable):
        if not isinstance(exe, Callable): 
            raise ValueError("El valor asignado al 'own.Label.exe_escritura' debe ser una función 'Callable'.")
        self._exe_al_escribir = exe