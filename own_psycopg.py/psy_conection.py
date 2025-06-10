from . import psycopg2, messagebox

DEF_HOST = "localhost"
DEF_PORT = "5432"

class Conexion:

    def __init__(self, *args, **kwargs):
        self.__verbose:tuple[bool,bool] = (False, False)
        super().__init__(*args, **kwargs)

    def conectar(self, dbname:str, user:str, password:str, host:str=DEF_HOST, port:str=DEF_PORT):
        try:
            conn = psycopg2.connect(
                dbname=dbname,
                user=user,
                password=password,
                host=host,
                port=port,
            )
            if self.__verbose[0]: print("Se estableció la conexión con la base de datos correctamente.")
            if self.__verbose[1]: messagebox.showinfo("Conexión exitosa", "Se estableció la conexión con la base de datos correctamente.")

        except Exception as e:
            conn = None
            if self.__verbose[0]: print(f"No se pudo conectar a la base de datos:\n{e}")
            if self.__verbose[1]: messagebox.showerror("Error de conexión", f"No se pudo conectar a la base de datos:\n{e}")

        finally: self.conexion = conn

    @property
    def verbose(self):
        return self.__verbose
    
    @verbose.setter
    def verbose(self, verb:tuple[bool, bool]):
        if len(verb) != 2: raise ValueError("La tupla debe identificar (consola, gui) donde consola:bool y gui:bool")
        if not isinstance(verb[0], bool) or not isinstance(verb[1], bool): raise ValueError("La tupla debe identificar (consola, gui) donde consola:bool y gui:bool")
        
        self.__verbose = verb