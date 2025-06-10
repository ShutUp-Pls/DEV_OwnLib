### CONSTRUCTOR DEL MODULO ###

### IMPORTACIONES DE LIBRERIAS USADAS POR EL MODULO
import psycopg2

from tkinter import filedialog, messagebox
from typing import Callable

from .psy_conection import Conexion, OBTENER_DBS, OBTENER_TBS

DEF_HOST = "localhost"
DEF_PORT = "5432"
DEF_DBNAME = None