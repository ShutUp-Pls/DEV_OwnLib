import psycopg2
from tkinter import messagebox

from .pg_conexion_props import ConexionProps

OBTENER_DBS = "SELECT datname FROM pg_database WHERE datistemplate = false;"
OBTENER_TBS = "SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname = 'public';"

class Conexion(ConexionProps):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def conectarse(self, **kwargs):
        try:
            conn = psycopg2.connect(**kwargs)

            self.desconectarse()

            if self._verbose[0]: print("Se estableció la conexión con la base de datos correctamente.")
            if self._verbose[1]: messagebox.showinfo("Conexión exitosa", "Se estableció la conexión con la base de datos correctamente.")

            return True

        except Exception as e:
            conn = None
            if self._verbose[0]: print(f"No se pudo conectar a la base de datos:\n{e}")
            if self._verbose[1]: messagebox.showerror("Error de conexión", f"No se pudo conectar a la base de datos:\n{e}")

            return False

        finally:
            self._conexion = conn
            if self._conexion: self.refrescar_databases()
    
    def desconectarse(self):
        if self._cursor is not None:
            try: 
                self._cursor.close()
            except Exception as e:
                if self._verbose[0]: print(f"Error al cerrar cursor:\n{e}")
                if self._verbose[1]: messagebox.showinfo("Cursor Error", f"Error al cerrar cursor:\n{e}")

        if self._conexion is not None:
            try: 
                self._conexion.close()
            except Exception as e:
                if self._verbose[0]: print(f"Error al desconectar:\n{e}")
                if self._verbose[1]: messagebox.showinfo("Desconexión", f"Error al desconectar:\n{e}")

        # Restablecemos las propiedades protegidas
        self._cursor     = None
        self._conexion   = None
        self._verbose    = (True, False)
        self._databases  = []
        self._database   = ""
        self._tablas     = []

        if self._verbose[0]: print("Desconectado y estado interno restablecido.")
        if self._verbose[1]: messagebox.showinfo("Desconexión", "Se ha cerrado la conexión y se restableció el estado.")
    
    def refrescar_cursor(self):
        if not self._conexion: 
            raise Exception("No hay conexión para extraer cursor.")

        self._cursor = self._conexion.cursor()

    def refrescar_databases(self):
        if not self._conexion: 
            raise Exception("No hay conexión para extraer databases.")

        self.refrescar_cursor()
        self.cursor.execute(OBTENER_DBS)
        databases: list[str] = [db for db in self.cursor.fetchall()]
        self.refrescar_cursor()

        self._databases = databases
        return self._databases
    
    def refrescar_tablas(self):
        if not self._conexion: 
            raise Exception("No hay conexión para extraer tablas.")
        if not self._database: 
            raise Exception("No hay base de datos seleccionada.")

        self.refrescar_cursor()
        self.cursor.execute(OBTENER_TBS)
        tablas: list[str] = [tb for tb in self.cursor.fetchall()]
        print("sexo: ", tablas)  # Tu print original de debug intacto jajaja
        self.refrescar_cursor()

        self._tablas = tablas
        return self._tablas