import own_tk as own
import own_psycopg as own_pg

from own_tk.own_frameautogrid import FrameAutoGrid

BTN_CONECT = "Conectarse"
BTN_DESCON = "Desconectarse"

class GUIpsql(own.Tk):

    def __init__(self, *args, **kwargs):
        self.__conexion = own_pg.PgConnect()
        self.__conexion.verbose = (False, True)

        super().__init__(*args, **kwargs)
        own.Tools.configurar_pesos(self, [1, 1], [1, 0])

        self.visualizacion = own.ScrollableFrame(self)
        self.visualizacion.grid(row=0, column=0, sticky=own.NSEW, rowspan=2)

        self.inicio_sesion = own.FrameLabel(self)
        own.Tools.configurar_pesos(self.inicio_sesion, [0, 0], {1})
        self.inicio_sesion.texto = "Conectarse a PostgresSQL:"
        self.inicio_sesion.grid(row=0, column=1, sticky=own.NSEW)

        self.datos_conexion = FrameAutoGrid(self.inicio_sesion, {
            own.Label:[(0,0),(1,0),(2,0),(3,0),(4,0)],
            own.Entry:[(0,1),(1,1),(2,1),(3,1),(4,1)],
        })
        
        for i, etiqueta in enumerate(["Usuario:", "Constraseña:", "Host:", "Puerto:", "Base de Datos:"]):
            self.datos_conexion.widgets[(i,0)].texto = etiqueta
            self.datos_conexion.widgets[(i,0)].grid_configure(sticky=own.E)

        self.datos_conexion.widgets[(2,1)].texto = own_pg.DEF_HOST if own_pg.DEF_HOST else ""
        self.datos_conexion.widgets[(3,1)].texto = own_pg.DEF_PORT if own_pg.DEF_PORT else ""
        self.datos_conexion.widgets[(4,1)].texto = own_pg.DEF_DBNAME if own_pg.DEF_DBNAME else ""

        self.datos_conexion.grid(row=0, column=0, sticky=own.NSEW)

        self.boton_conexion = own.Button(self.inicio_sesion)
        self.boton_conexion.texto = BTN_CONECT
        self.boton_conexion.exe_boton = self.__exe_conectar
        self.boton_conexion.grid(row=1, column=0, sticky=own.NSEW)

        self.seleccionar_frame = own.FrameLabel(self)
        own.Tools.configurar_pesos(self.seleccionar_frame, [0, 0], [1])
        self.seleccionar_frame.texto = "Seleccionar:"
        self.seleccionar_frame.grid(row=1, column=1, sticky=own.NSEW)

        self.seleccionar_database = own.DropdownMenu(self.seleccionar_frame, default=("No hay Bases de Datos.", None))
        self.seleccionar_database.grid(row=0, column=0, sticky=own.EW)

        self.seleccionar_tabla = own.DropdownMenu(self.seleccionar_frame, default=("No hay Tablas disponibles.", None))
        self.seleccionar_tabla.grid(row=1, column=0, sticky=own.EW)

    @property
    def conexion(self):
        return self.__conexion
    
    @conexion.setter
    def conexion(self, con:dict[str,str]):
        self.__conexion.conexion = con

        if self.__conexion.conexion: pass

    def __estado_desconectado(self):
        for _, widget in self.datos_conexion.widgets.items():
            if isinstance(widget, own.Entry): widget.config(state=own.NORMAL)

        self.boton_conexion.texto = BTN_CONECT
        self.boton_conexion.exe_boton = self.__exe_conectar

        self.seleccionar_database.opciones = {}
        self.seleccionar_tabla.opciones = {}

    def __estado_conectado(self):
        for _, widget in self.datos_conexion.widgets.items():
            if isinstance(widget, own.Entry): widget.config(state=own.DISABLED)

        self.boton_conexion.texto = BTN_DESCON
        self.boton_conexion.exe_boton = self.__exe_deconectar

        dbs = self.__conexion.databases
        self.seleccionar_database.opciones = {tag:None for tag in dbs}

        print("flag 1")
        self.__conexion.database = self.seleccionar_database.opcion
        print("flag 2")
        tbs = self.__conexion.tablas
        print("sexo",tbs)
        self.seleccionar_tabla.opciones = {tag:None for tag in tbs}

        # self.__conexion.tabla = self.seleccionar_tabla.opcion

    def __exe_conectar(self, *_):
        host = self.datos_conexion.widgets[(2,1)].texto
        port = self.datos_conexion.widgets[(3,1)].texto
        dbname = self.datos_conexion.widgets[(4,1)].texto

        conectado = self.__conexion.conectarse(
            user = self.datos_conexion.widgets[(0,1)].texto,
            password = self.datos_conexion.widgets[(1,1)].texto,
            host = host if host else own_pg.DEF_HOST,
            port = port if port else own_pg.DEF_PORT,
            dbname = dbname if dbname else own_pg.DEF_DBNAME
        )

        if conectado:
            
            self.__estado_conectado()
        else: self.__estado_desconectado()

    def __exe_deconectar(self, *_):
        self.__conexion.desconectarse()
        self.__estado_desconectado()


programa = GUIpsql()
programa.title("CRUD (Solo Gráficos)")
own.Tools.configurar_pesos(programa, [1], [1])

programa.mainloop()