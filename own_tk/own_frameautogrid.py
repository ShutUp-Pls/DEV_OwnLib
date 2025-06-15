from . import Callable, Frame, Tk, Widget

class FrameAutoGrid(Frame):

    def __init__(self, master:Tk|Frame = None, posiciones:dict[Widget,list[tuple[int,int]]] = None, **kwargs):
        if not posiciones or not isinstance(posiciones, dict): raise ValueError("El parámetro 'posiciones' debe ser un diccionario no vacío.")

        self.__widgets:dict[tuple[int,int],Widget] = {}

        super().__init__(master, **kwargs)

        for wdg, pos_list in posiciones.items():
            for row, col in pos_list:
                widget = wdg(self)
                widget.grid(row=row, column=col)
                self.__widgets[(row, col)] = widget

    @property
    def widgets(self):
        return self.__widgets