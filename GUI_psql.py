import psycopg2

import own_tk as own

from own_tk.own_entrybutton import EntryLabelButton

class GUIpsql(own.Tk):

    def __init__(self, *args, **kwargs):
        self.conexion:psycopg2 = None

        super().__init__(*args, **kwargs)
        own.Tools.configurar_pesos(self, [1], [1, 0])

        self.visualizacion = own.ScrollableFrame(self)
        self.visualizacion.grid(row=0, column=0, sticky=own.NSEW)

        self.inicio_sesion = own.FrameLabel(self)
        own.Tools.configurar_pesos(self.inicio_sesion, [1, 0], {1})
        self.inicio_sesion.texto = "Conectarse a PostgresSQL"
        self.inicio_sesion.grid(row=0, column=1, sticky=own.N)

        self.datos_conexion = EntryLabelButton(self.inicio_sesion, {
            "l":[(0,0),(1,0),(2,0),(3,0),(4,0)],
            "e":[(0,1),(1,1),(2,1),(3,1),(4,1)],
        })
        
        for i, etiqueta in enumerate(["Base de Datos:", "Usuario:", "Constraseña:", "Host:", "Puerto:"]):
            self.datos_conexion.widgets[(i,0)].texto = etiqueta
            self.datos_conexion.widgets[(i,0)].grid_configure(sticky=own.E)

        self.datos_conexion.grid(row=0, column=0, sticky=own.NSEW)

        self.boton_conexion = own.Button(self.inicio_sesion)
        self.boton_conexion.texto = "Conectar"
        self.boton_conexion.exe_boton = self.__intentar_conectar
        self.boton_conexion.grid(row=1, column=0, sticky=own.NSEW)

    def __intentar_conectar(self, *_):
        try:
            conn = psycopg2.connect(
                dbname=self.datos_conexion.widgets[(0,1)].texto,
                user=self.datos_conexion.widgets[(1,1)].texto,
                password=self.datos_conexion.widgets[(2,1)].texto,
                host=self.datos_conexion.widgets[(3,1)].texto,
                port=self.datos_conexion.widgets[(4,1)].texto,
            )
            own.messagebox.showinfo("Conexión exitosa", "Se estableció la conexión con la base de datos correctamente.")

        except Exception as e:
            conn = None
            own.messagebox.showerror("Error de conexión", f"No se pudo conectar a la base de datos:\n{e}")

        finally: self.conexion = conn

programa = GUIpsql()
programa.title("CRUD V1.0 - Alpha (Only Graphics)")
own.Tools.configurar_pesos(programa, [1], [1])

programa.mainloop()