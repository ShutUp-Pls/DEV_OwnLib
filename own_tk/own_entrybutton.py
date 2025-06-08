from . import Callable, Entry, Button, Frame, Tk, NSEW, Tools

class EntryButton(Frame):

    def __init__(self, master:Tk|Frame=None, **kwargs):
        self.__exe_boton:Callable = None

        super().__init__(master, **kwargs)
        Tools.configurar_pesos(self, [1], [1, 1])

        self.entrada = Entry(self)
        self.entrada.grid(row=0, column=0, sticky=NSEW)

        self.boton = Button(self)
        self.boton.exe_boton = self.__exe_boton_f
        self.boton.grid(row=0, column=1, sticky=NSEW)

    @property
    def exe_boton(self):
        return self.__exe_boton
    
    @exe_boton.setter
    def exe_boton(self, exe:Callable):
        self.__exe_boton = exe
    
    def __exe_boton_f(self, *_):
        if self.__exe_boton: self.__exe_boton()