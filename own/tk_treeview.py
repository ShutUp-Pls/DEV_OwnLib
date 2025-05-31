from . import MutableMapping, ttk

class OwnTreeview(MutableMapping):
    def __init__(self, master, **kwargs):
        self.__tree = ttk.Treeview(master=master, **kwargs)
        self.__columns = ()
        self.__data = {}
        self.__allow_overwrite = False

        self.def_tag = "Col"

    @property
    def allow_overwrite(self):
        return self.__allow_overwrite
    
    @allow_overwrite.setter
    def allow_overwrite(self, value:bool):
        if not isinstance(value, bool): raise ValueError(f"Permitir el sobre escribir nuevos valores debe ser booleano.\n[Valor Intentado]: {value}\n[Valor Tipo]: {type(value)}")

        self.__allow_overwrite = value

    @property
    def columns(self):
        return self.__columns

    @columns.setter
    def columns(self, value:tuple|int):
        ### VALIDACIONES
        # Si se quiere setear un diccionario completo se han de cumplir ciertas condiciones.
        if not isinstance(value, (int,tuple)): raise ValueError(f"Columnas deben ser Tupla o Entero.\n[Valor Intentado]: {value}\n[Valor Tipo]: {type(value)}")

        ### DEFINICION
        # Si se cumplen todas las validaciones.
        self.__columns = value if isinstance(value, tuple) else tuple(f"{self.def_tag}_{i}" for i in range(1, value + 1))
        self.__data = {}

        self.__tree["columns"] = self.__columns
        self.__tree.delete(*self.__tree.get_children())
        for col in self.__columns:
            self.__tree.heading(col, text=col)
            self.__tree.column(col, width=100)        

    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, data_dict:dict):
        ### VALIDACIONES
        # Si se quiere setear un diccionario completo se han de cumplir ciertas condiciones.
        lens = {len(v) for v in data_dict.values()}
        valid_len = (len(lens) == 1)
        if not valid_len: raise ValueError(f"Hay filas que difieren en tamaño.\n[Tamaños de Fila]: {lens}")

        lens = next(iter(lens))
        valid_len = (lens == len(self.__columns))
        if not valid_len: raise ValueError(f"El largo de las filas no coincide con el requerido.\n[Tamaños de Fila]: {lens}\n[Tamaño de Fila Requerido]: {len(self.__columns)}")

        for k in data_dict:
            if not isinstance(k, str): raise ValueError(f"Un iid no es una entrada valida.\n[iid value]: {k}\n[iid tipo]: {type(k)}")

        ### DEFINICION
        # Si se cumplen todas las validaciones.
        self.__data = data_dict
        self.__tree.delete(*self.__tree.get_children())
        for iid, values in data_dict.items(): self.__tree.insert("", "end", iid=iid, values=values)

    def __getitem__(self, key:str):
        return self.__data[key]

    def __setitem__(self, key:str, value:tuple):
        ### VALIDACIONES
        # Si se quiere agregar una fila esta debe cumplir con ciertas cosas.
        if not isinstance(key, str): raise ValueError(f"El 'iid' solo puede ser una cadena de texto.\n[iid]: {key}\n[iid Type]: {type(key)}")
        if not isinstance(value, tuple): raise ValueError(f"La fila del 'iid' deben estar definidas en tupla.\n[Fila]: {value}\n[Fila Type]: {type(value)}")
        if len(value) != len(self.__columns): raise ValueError(f"La fila ingresada no cumple el N°columnas requeridas.\n[Fila]: {value}\n[Columnas Requeridas]: {len(self.__columns)}") 

        ### DEFINICION
        # Si se cumplen todas las validaciones.
        key_in_data = (key in self.__data)
        if key_in_data :
            if self.__allow_overwrite:
                self.__data[key] = value
                self.__tree.delete(key)
                self.__tree.insert("", "end", iid=key, values=value)
        else:
            self.__data[key] = value
            self.__tree.insert("", "end", iid=key, values=value)
        
        self.__tree.update_idletasks()

    def __delitem__(self, key):
        if key in self.__data:
            del self.__data[key]
            self.__tree.delete(key)
            self.__tree.update_idletasks()

    def __iter__(self):
        return iter(self.__data)

    def __len__(self):
        return len(self.__data)

    def __repr__(self):
        return self.__data
    
    def __str__(self):
        return self.__data
    
    ### MÉTODOS COMÚNES
    # Métodos que afectan al Treeview y sus estructuras de datos.
    def selection_del(self, **kwargs):
        selected_iids = self.__tree.selection(**kwargs)
        if selected_iids:
            for iid in selected_iids: self.__delitem__(iid)
    
    ### MÉTODOS OVERLOAD
    # Métodos Treeview
    def selection(self, **kwargs):
        return self.__tree.selection(**kwargs)
    
    def pack(self,**kwargs):
        self.__tree.pack(**kwargs)

    ### MÉTODOS OVERLOAD
    # Métodos de las estructuras