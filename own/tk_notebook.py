from . import ttk, tk

class Notebook(ttk.Notebook):

    def __init__(self, master:tk.Tk|tk.Toplevel|tk.Frame|tk.Canvas=None, **kwargs):
        

        super().__init__(master, **kwargs)