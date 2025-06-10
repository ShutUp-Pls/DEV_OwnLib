from . import psycopg2, messagebox

from psycopg2.extensions import cursor, connection

OBTENER_DBS = "SELECT datname FROM pg_database WHERE datistemplate = false;"
OBTENER_TBS = "SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname = 'public';"

class Conexion:

    def __init__(self, *args, **kwargs):
        self.__cursor:cursor = None
        self.__conexion:connection = None
        self.__verbose:tuple[bool,bool] = (True, False)
        self.__databases:list[str] = []
        self.__database:str = ""
        self.__tablas:list[str] = []

        super().__init__(*args, **kwargs)

    @property
    def verbose(self):
        return self.__verbose
    
    @verbose.setter
    def verbose(self, verb:tuple[bool, bool]):
        if len(verb) != 2: raise ValueError("La tupla debe identificar (consola, gui) donde consola:bool y gui:bool")
        if not isinstance(verb[0], bool) or not isinstance(verb[1], bool): raise ValueError("La tupla debe identificar (consola, gui) donde consola:bool y gui:bool")
        
        self.__verbose = verb

    @property
    def conexion(self):
        return self.__conexion
    
    @conexion.setter
    def conexion(self, con:dict[str,str]):
        self.conectarse(**con)
    
    @property
    def cursor(self):
        return self.__cursor
    
    @property
    def databases(self):
        return self.__databases
    
    @property
    def database(self):
        return self.__database
    
    @database.setter
    def database(self, db:str):
        if not self.__databases: raise Exception("No hay bases de datos dispobibles.")
        if not db in self.__databases: raise Exception(f"Base de datos no disponible\nBase de datos seleccionada:{db}\nBases de datos disponibles:{self.__databases}")

        self.__database = db
        self.refrescar_tablas()

    @property
    def tablas(self):
        return self.__tablas
    
    def conectarse(self, **kwargs):
        try:
            conn = psycopg2.connect(**kwargs)

            self.desconectarse()

            if self.__verbose[0]: print("Se estableció la conexión con la base de datos correctamente.")
            if self.__verbose[1]: messagebox.showinfo("Conexión exitosa", "Se estableció la conexión con la base de datos correctamente.")

            return True

        except Exception as e:
            conn = None
            if self.__verbose[0]: print(f"No se pudo conectar a la base de datos:\n{e}")
            if self.__verbose[1]: messagebox.showerror("Error de conexión", f"No se pudo conectar a la base de datos:\n{e}")

            return False

        finally:
            self.__conexion = conn
            if self.__conexion: self.refrescar_databases()
    
    def desconectarse(self):
        if self.__cursor is not None:
            try: self.__cursor.close()

            except Exception as e:
                if self.__verbose[0]: print(f"Error al cerrar cursor:\n{e}")
                if self.__verbose[1]: messagebox.showinfo("Cursor Error", f"Error al cerrar cursor:\n{e}")

        if self.__conexion is not None:
            try: self.__conexion.close()

            except Exception as e:
                if self.__verbose[0]: print(f"Error al desconectar:\n{e}")
                if self.__verbose[1]: messagebox.showinfo("Desconexión", f"Error al desconectar:\n{e}")

        self.__cursor     = None
        self.__conexion   = None
        self.__verbose    = (True, False)
        self.__databases  = []
        self.__database   = ""
        self.__tablas     = []

        if self.__verbose[0]: print("Desconectado y estado interno restablecido.")
        if self.__verbose[1]: messagebox.showinfo("Desconexión", "Se ha cerrado la conexión y se restableció el estado.")
    
    def refrescar_cursor(self):
        if not self.__conexion: raise Exception("No hay conexión para extraer cursor.")

        self.__cursor = self.__conexion.cursor()

    def refrescar_databases(self):
        if not self.__conexion: raise Exception("No hay conexión para extraer databases.")

        self.refrescar_cursor()
        self.cursor.execute(OBTENER_DBS)
        databases:list[str] = [db for db in self.cursor.fetchall()]
        self.refrescar_cursor()

        self.__databases = databases
        return self.__databases
    
    def refrescar_tablas(self):
        if not self.__conexion: raise Exception("No hay conexión para extraer databases.")
        if not self.__database: raise Exception("No hay base de datos seleccionada.")

        self.refrescar_cursor()
        self.cursor.execute(OBTENER_TBS)
        tablas:list[str] = [tb for tb in self.cursor.fetchall()]
        print("sexo: ", tablas)
        self.refrescar_cursor()

        self.__tablas = tablas
        return self.__tablas