from . import tk, font, Callable

class Tools:

    def __init__(self): pass

    @staticmethod
    def configurar_pesos(widget:tk.Widget, pesos_filas:list[int], pesos_columnas:list[int]):
        '''Asigna pesos a las filas y columnas "grid" de un widget.'''
        for fila, peso in enumerate(pesos_filas): widget.rowconfigure(fila, weight=peso)
        for columna, peso in enumerate(pesos_columnas): widget.columnconfigure(columna, weight=peso)

    @staticmethod
    def siguiente_columna_disponible(fila:int, widget:tk.Widget) -> int:
        '''Retorna el indíce de la siguiente columna 'grid' disponible en un widget sobre una fila especifica y después del último widget empaquetado.'''
        ocupadas = []
        for w in widget.grid_slaves(row=fila):
            info = w.grid_info()
            col = int(info["column"])
            span = int(info.get("columnspan", 1))
            ocupadas.extend(range(col, col + span))
        return 0 if not ocupadas else max(ocupadas) + 1
    
    @staticmethod
    def siguiente_fila_disponible(columna: int, widget: tk.Widget) -> int:
        '''Retorna el índice de la siguiente fila 'grid' disponible en un widget sobre una columna específica y después del último widget empaquetado.'''
        ocupadas = []
        for w in widget.grid_slaves(column=columna):
            info = w.grid_info()
            fila = int(info["row"])
            span = int(info.get("rowspan", 1))
            ocupadas.extend(range(fila, fila + span))
        return 0 if not ocupadas else max(ocupadas) + 1

    @staticmethod
    def calcular_dimensiones(widget_altos:list[tk.Widget], widget_anchos:list[tk.Widget], margen_extra_v:int = 0, margen_extra_h:int = 0):
        '''Calcula el alto total y el ancho total de una lista de widgets más un margen opcional para cada uno.'''
        alto_total = sum(widget.winfo_reqheight() for widget in widget_altos) + margen_extra_v
        ancho_total = sum(widget.winfo_reqwidth() for widget in widget_anchos) + margen_extra_h
        return alto_total, ancho_total
    
    @staticmethod
    def px_to_entry_chars(widget:tk.Widget, px:int):
        """Convierte una medida en píxeles al equivalente en caracteres para un widget de tipo Entry, usando su fuente."""
        widget_font = font.nametofont(widget.cget("font"))
        char_width_px = widget_font.measure("0") or 1  # Evita división por cero
        return px // char_width_px