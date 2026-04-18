import tkinter as tk
from .tk_entry_props import EntryProps

class Entry(EntryProps, tk.Entry):
    
    def __init__(self, master: tk.Tk|tk.Toplevel|tk.Frame|tk.Canvas, **kwargs):
        self._texto: tk.StringVar = tk.StringVar()
        super().__init__(master, textvariable=self._texto, **kwargs)

        self._texto.trace_add('write', self._exe_al_escribir_f)
        self.configure(validate='key', validatecommand=(self.register(self._validar_entrada_f), '%P'))
        self.bind("<FocusOut>", self._exe_focus_out_f)
        self.bind("<FocusIn>", self._exe_focus_in_f)

        self._exe_focus_out_f()


    def _exe_al_escribir_f(self, *_):
        if self._exe_al_escribir: self._exe_al_escribir()

    def _exe_focus_out_f(self, *_):
        if not self._texto.get() and self._placeholder:
            self._usando_placeholder = True
            self._texto.set(self._placeholder)
            self.config(foreground=self._placeholder_color)

        if self._exe_focus_out: self._exe_focus_out()

    def _exe_focus_in_f(self, *_):
        if self._usando_placeholder and self._texto.get() == self._placeholder:
            self._texto.set("")
            self._usando_placeholder = False
            self.config(foreground=self._placeholder_color_normal)

        if self._exe_focus_in: self._exe_focus_in()

    def _validar_entrada_f(self, entrada: str):
        if self._usando_placeholder: return True

        if any(c in entrada for c in self._caracteres_prohibidos): return False
        if len(entrada) > self._limite_caracteres > -1: return False

        return True