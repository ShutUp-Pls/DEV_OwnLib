### CONSTRUCTOR DEL MODULO ###

### IMPORTACIONES DE LIBRERIAS USADAS POR EL MODULO
# Estan marcados con un comentario los modulos que estan siendo llamados
# Y dentro e los comentarios posibles importaciones futuras

import os, json, time, shutil
import queue
import decimal
import traceback
import threading
import requests
import tkinter as tk

from itertools import zip_longest
from PIL import ImageFont, ImageDraw        #, Image, ImageTk
from tkinter import ttk, font               #, Text, filedialog, messagebox
from collections.abc import MutableMapping
from bs4 import BeautifulSoup

from types import GeneratorType
from typing import Any, Literal, Callable
from tkinter import filedialog

### IMPORTACIÓN DE CLASES PROPIAS
# Corresponde a clases del modulo ya listas para usar por el usuario
from .tools_crono import Crono
from .tools_dict import DictTools
from .tools_format import FormatTools
from .tools_json import JsonTools
from .tools_list import ListTools
from .tools_os import OsTools
from .tools_pillow import PillowTools
from .tools_str import StrTools
from .tools_tk import Tools

# from .tk_treeview import OwnTreeview
from .tk_tk import Tk
from .tk_button import Button
from .tk_frame import Frame
from .tk_entry import Entry

# Scrollables
from .tk_scrollableframe import ScrollableFrame
from .tk_textframe import TextFrame

BASE_DIR = os.path.dirname(__file__)

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