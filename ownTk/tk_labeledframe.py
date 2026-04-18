import tkinter as tk
from .tk_labeledframe_props import FrameLabelProps

class FrameLabel(FrameLabelProps, tk.LabelFrame):

    def __init__(self, master: tk.Tk|tk.Toplevel|tk.Frame|tk.Canvas=None, **kwargs):
        '''tk.LabelFrame - Widget funciona como Frame pero enmarcado y con texto de titulo.'''
        super().__init__(master, **kwargs)