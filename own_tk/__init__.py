### CONSTRUCTOR DEL MODULO ###

### IMPORTACIONES DE LIBRERIAS USADAS POR EL MODULO
import tkinter as tk

from tkinter import filedialog
from typing import Callable

from .tools_tk import Tools
from .tk_button import Button
from .tk_entry import Entry
from .tk_frame import Frame
from .tk_scrollableframe import ScrollableFrame
from .tk_textframe import TextFrame
from .tk_tk import Tk

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