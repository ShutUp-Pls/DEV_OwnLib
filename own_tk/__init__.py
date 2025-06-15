'''Clase envoltura y personalizada de la librería 'tkinter'.'''
import tkinter as tk

from typing import Callable, Union
from tkinter import filedialog, messagebox

from .tk_tk import Tk
from .tools_tk import Tools
from .tk_entry import Entry
from .tk_frame import Frame
from .tk_label import Label
from .tk_button import Button
from .tk_cascade import Cascade
from .tk_textframe import TextFrame
from .tk_dropdownmenu import DropdownMenu
from .tk_labeledframe import FrameLabel
from .tk_scrollableframe import ScrollableFrame

Widget = Union[Button, Cascade, Frame, Entry, Label, TextFrame, ScrollableFrame, DropdownMenu, FrameLabel]

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