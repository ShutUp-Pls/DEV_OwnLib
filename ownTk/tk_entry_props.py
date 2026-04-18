from typing import Callable

class EntryProps:

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self._limite_caracteres: int = -1
        self._caracteres_prohibidos: str|list|set|tuple|dict = ""
        
        self._placeholder: str = ""
        self._placeholder_color_normal: str = self.cget("foreground")
        self._placeholder_color: str = "gray"
        self._usando_placeholder: bool = False

        self._exe_al_escribir: Callable = None
        self._exe_focus_out: Callable = None
        self._exe_focus_in: Callable = None
    
    @property
    def texto(self) -> str:
        if self._usando_placeholder: return ""
        else: return self._texto.get()
    
    @texto.setter
    def texto(self, txt: str):
        self._texto.set(txt)

    @property
    def limite_caracteres(self) -> int:
        return self._limite_caracteres
    
    @limite_caracteres.setter
    def limite_caracteres(self, limite: int):
        self._limite_caracteres = limite

    @property
    def caracteres_prohibidos(self) -> str|list|set|tuple|dict:
        return self._caracteres_prohibidos
    
    @caracteres_prohibidos.setter
    def caracteres_prohibidos(self, nueva_coleccion: str|list|set|tuple|dict):
        self._caracteres_prohibidos = nueva_coleccion

    @property
    def placeholder(self) -> str:
        return self._placeholder
    
    @placeholder.setter
    def placeholder(self, texto: str):
        self._placeholder = texto

    @property
    def exe_al_escribir(self) -> Callable:
        return self._exe_al_escribir
    
    @exe_al_escribir.setter
    def exe_al_escribir(self, exe: Callable):
        self._exe_al_escribir = exe

    @property
    def exe_focus_out(self) -> Callable:
        return self._exe_focus_out
    
    @exe_focus_out.setter
    def exe_focus_out(self, exe: Callable):
        self._exe_focus_out = exe

    @property
    def exe_focus_in(self) -> Callable:
        return self._exe_focus_in
    
    @exe_focus_in.setter
    def exe_focus_in(self, exe: Callable):
        self._exe_focus_in = exe

    @property
    def usando_placeholder(self) -> bool:
        return self._usando_placeholder