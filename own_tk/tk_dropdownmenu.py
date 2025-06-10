from . import Callable, tk

class DropdownMenu(tk.Menubutton):
    def __init__(self,master, default:tuple[str,Callable]=("- Vacío -", None), opciones:dict[str,Callable|None]={},**kwargs):
        self.__default = default
        self.__opciones = opciones

        self.__exe_opcion:Callable = None
        self.__opcion = tk.StringVar(value=self.__default[0])
        
        super().__init__(master, textvariable=self.__opcion, **kwargs)

        self.__menu = tk.Menu(self, tearoff=0)
        self.configure(menu=self.__menu)

        self.opciones = opciones

    @property
    def default(self):
        return self.__default

    @default.setter
    def default(self, valor:tuple[str,Callable]):
        self.__default = valor

    @property
    def opciones(self):
        return self.__opciones

    @opciones.setter
    def opciones(self, opc:dict[str,Callable|None]):
        self.__opciones = opc

        self.__menu.delete(0, tk.END)
        for tag, func in opc.items():
            self.__menu.add_command(label=tag, command=lambda t=tag,  f=func:self.__exe_al_seleccionar(t, f))

        if not opc: self.configure(state="disabled")
        else: self.configure(state="normal")

        claves = list(opc.keys())
        sel_actual = self.__opcion.get()

        if not claves or self.__default[0] in claves: self.opcion = self.__default[0]

        elif sel_actual in claves: self.opcion = sel_actual

        else: self.opcion = claves[0]

    @property
    def opcion(self):
        return self.__opcion.get()

    @opcion.setter
    def opcion(self, opc:str):
        self.__opcion.set(opc)

    @property
    def exe_opcion(self):
        return self.__exe_opcion
    
    @exe_opcion.setter
    def exe_opcion(self, exe:Callable):
        if not isinstance(exe, Callable): raise ValueError("El ejecutable de la opción debe ser una función 'Callable'.")

        self.__exe_opcion = exe

    def __exe_al_seleccionar(self, tag:str, func:Callable|None):
        self.__opcion.set(tag)

        if func: func()
        if self.__exe_opcion: self.__exe_opcion()