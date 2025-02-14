from . import MutableMapping, ttk, tk

class OwnTreeview(MutableMapping):
    def __init__(self, master, **kwargs):
        self.__tree = ttk.Treeview(master=master, **kwargs)
        self.__columns = ()
        self.__data = {}

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

        valid_len = (lens[0] == len(self.__columns))
        if not valid_len: raise ValueError(f"El largo de las filas no coincide con el requerido.\n[Tamaños de Fila]: {lens}\n[Tamaño de Fila Requerido]: {len(self.__columns)}")

        valid_keys = all(isinstance(k, str) for k in data_dict)
        if not valid_keys: raise ValueError(f"Hay identificadores que no son cadenas de texto.")

        ### DEFINICION
        # Si se cumplen todas las validaciones.
        self.__data = data_dict
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
        self.__data[key] = value
        self.__tree.insert("", "end", iid=key, values=value)

    def __delitem__(self, key):
        if key in self.__data:
            del self.__data[key]
            self.__tree.delete(key)

    def __iter__(self):
        return iter(self.__data)

    def __len__(self):
        return (len(self.__data), len(self.__columns))

    def __str__(self):
        return self.__data