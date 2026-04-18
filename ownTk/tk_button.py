import tkinter as tk
from .tk_button_props import ButtonProps

class Button(ButtonProps, tk.Button):

    def __init__(self, master: tk.Tk|tk.Toplevel|tk.Frame|tk.Canvas=None, **kwargs):
        kwargs['command'] = self._click_boton
        super().__init__(master, **kwargs)

    def _click_boton(self, *_):
        if self._exe_boton: self._exe_boton()