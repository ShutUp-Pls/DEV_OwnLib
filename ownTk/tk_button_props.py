import tkinter as tk
from typing import Callable

class ButtonProps:
    def __init__(self, master=None, **kwargs):
        self._texto: tk.StringVar = tk.StringVar()
        self._exe_boton: Callable = None
        
        kwargs['textvariable'] = self._texto

        super().__init__(master, **kwargs)

    @property
    def texto(self) -> str:
        return self._texto.get()
    
    @texto.setter
    def texto(self, txt: str):
        self._texto.set(txt)

    @property
    def exe_boton(self) -> Callable:
        return self._exe_boton
    
    @exe_boton.setter
    def exe_boton(self, exe: Callable):
        self._exe_boton = exe