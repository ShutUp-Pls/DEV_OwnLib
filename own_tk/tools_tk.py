from . import tk, Callable

class Tools:

    def __init__(self): pass

    @staticmethod
    def configurar_pesos(widget:tk.Widget, pesos_filas:list[int], pesos_columnas:list[int]):
        '''Asigna pesos a las filas y columnas "grid" de un widget.'''
        for fila, peso in enumerate(pesos_filas): widget.rowconfigure(fila, weight=peso)
        for columna, peso in enumerate(pesos_columnas): widget.columnconfigure(columna, weight=peso)

    @staticmethod
    def esta_empaquetado_con_grid(widget:tk.Widget):
        return bool(widget.grid_info())