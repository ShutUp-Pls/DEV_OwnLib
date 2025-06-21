'''Clase envoltura y personalizada de la librería 'tkinter'.'''
import tkinter as tk
import psycopg2

from typing import Callable
from tkinter import filedialog, messagebox, ttk
from psycopg2.extensions import cursor, connection

from .tk_tk import Tk
from .tk_entry import Entry
from .tk_frame import Frame
from .tk_label import Label
from .tk_button import Button
from .tk_cascade import Cascade
from .tk_treeview import Treeview
from .tk_textframe import TextFrame
from .tk_menubutton import Menubutton
from .tk_labeledframe import FrameLabel
from .tk_frameautogrid import FrameAutoGrid
from .tk_scrollableframe import ScrollableFrame

from .tools_tk import Tools
from .pg_connect import PgConnect

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

DEF_HOST = "localhost"
DEF_PORT = "5432"
DEF_DBNAME = ""