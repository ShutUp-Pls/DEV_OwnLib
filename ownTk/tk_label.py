import tkinter as tk
from .tk_label_props import LabelProps

class Label(LabelProps, tk.Label):

    def __init__(self, master: tk.Tk|tk.Toplevel|tk.Frame|tk.Canvas, **kwargs):
        super().__init__(master, **kwargs)