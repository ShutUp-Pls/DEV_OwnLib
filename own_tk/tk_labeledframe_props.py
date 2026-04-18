import tkinter as tk
from typing import Callable

class FrameLabelProps:
    def __init__(self, master=None, **kwargs):
        self._exe_al_escribir: Callable = None
        super().__init__(master, **kwargs)

    @property
    def texto(self) -> str:
        return self['text']
    
    @texto.setter
    def texto(self, txt: str):
        if not isinstance(txt, str): 
            raise ValueError("texto debe ser una cadena de texto")
        if self._exe_al_escribir: 
            self._exe_al_escribir()
        self.config(text=txt)

    @property
    def exe_escritura(self) -> Callable:
        return self._exe_al_escribir
    
    @exe_escritura.setter
    def exe_escritura(self, exe: Callable):
        if not isinstance(exe, Callable): 
            raise ValueError("El valor asignado al 'own.Label.exe_escritura' debe ser una función 'Callable'.")
        self._exe_al_escribir = exe