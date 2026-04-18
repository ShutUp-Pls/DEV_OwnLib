class ConexionProps:

    def __init__(self, *args, **kwargs):
        self._cursor = None
        self._conexion = None
        self._verbose: tuple[bool, bool] = (True, False)
        self._databases: list[str] = []
        self._database: str = ""
        self._tablas: list[str] = []

        super().__init__(*args, **kwargs)

    @property
    def verbose(self):
        return self._verbose
    
    @verbose.setter
    def verbose(self, verb: tuple[bool, bool]):
        if len(verb) != 2: 
            raise ValueError("La tupla debe identificar (consola, gui) donde consola:bool y gui:bool")
        if not isinstance(verb[0], bool) or not isinstance(verb[1], bool): 
            raise ValueError("La tupla debe identificar (consola, gui) donde consola:bool y gui:bool")
        
        self._verbose = verb

    @property
    def conexion(self):
        return self._conexion
    
    @conexion.setter
    def conexion(self, con: dict[str, str]):
        self.conectarse(**con)  # Este método será provisto por la clase principal
    
    @property
    def cursor(self):
        return self._cursor
    
    @property
    def databases(self):
        return self._databases
    
    @property
    def database(self):
        return self._database
    
    @database.setter
    def database(self, db: str):
        if not self._databases: 
            raise Exception("No hay bases de datos disponibles.")
        if db not in self._databases: 
            raise Exception(f"Base de datos no disponible\nBase de datos seleccionada:{db}\nBases de datos disponibles:{self._databases}")

        self._database = db
        self.refrescar_tablas()  # Este método será provisto por la clase principal

    @property
    def tablas(self):
        return self._tablas