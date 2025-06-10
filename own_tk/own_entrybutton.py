from . import Callable, Entry, Button, Label, Frame, Tk, Tools, Widget

class EntryLabelButton(Frame):

    def __init__(self, master:Tk|Frame = None, posiciones:dict[str,list[tuple[int,int]]] = None, **kwargs):
        if not posiciones or not isinstance(posiciones, dict): raise ValueError("La lista 'posiciones' no puede estar vacía y debe ser una lista de diccionarios.")
        
        self.__exe_boton: Callable = None
        self.__widgets:dict[tuple[int,int], Label|Button|Entry] = []

        super().__init__(master, **kwargs)

        widgets:dict[tuple[int,int], Label|Button|Entry] = {}
        for wdg, pos in posiciones.items():
            for row, col in pos:
                # Label
                if wdg == "l":
                    lbl = Label(self)
                    lbl.texto = ""
                    lbl.grid(row=row, column=col)
                    widgets[(row, col)] = lbl

                # Entry
                if wdg == "e":
                    ent = Entry(self)
                    ent.grid(row=row, column=col)
                    widgets[(row, col)] = ent

                # Button
                if wdg == "b":
                    btn = Button(self)
                    btn.texto = ""
                    btn.grid(row=row, column=col)
                    widgets[(row, col)] = btn

            self.__widgets = widgets

    @property
    def exe_boton(self):
        return self.__exe_boton

    @exe_boton.setter
    def exe_boton(self, exe: Callable):
        if not isinstance(exe, Callable):
            raise ValueError("exe_boton debe ser: Callable")
        self.__exe_boton = exe

    @property
    def widgets(self):
        return self.__widgets