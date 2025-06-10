### CONSTRUCTOR DEL MODULO ###

### IMPORTACIONES DE LIBRERIAS USADAS POR EL MODULO
import psycopg2

import tkinter as tk

from tkinter import filedialog, messagebox
from typing import Callable, Literal

from .psy_conection import

# Puntos Cardinales
W = tk.W
S = tk.S
E = tk.E
N = tk.N
NE = tk.NE
EW = tk.EW
NS = tk.NS
END = tk.END
NSEW = tk.NSEW

# Etiquetas, flags, cadenas
WORD = tk.WORD
NORMAL = tk.NORMAL
CENTER = tk.CENTER
DISABLED = tk.DISABLED