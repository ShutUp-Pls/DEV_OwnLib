'''Clase envoltura y personalizada de la librería 'tkinter'.'''
from .tk_tk import Tk
from .tk_entry import Entry
from .tk_frame import Frame
from .tk_label import Label
from .tk_button import Button
from .tk_cascade import Cascade
from .tk_notebook import Notebook
from .tk_treeview import Treeview
from .tk_textframe import TextFrame
from .tk_menubutton import Menubutton
from .tk_labeledframe import FrameLabel
from .tk_frameautogrid import FrameAutoGrid
from .tk_scrollableframe import ScrollableFrame

__all__ = [
    "Tk",
    "Entry",
    "Frame",
    "Label",
    "Button",
    "Cascade",
    "Notebook",
    "Treeview",
    "TestFrame",
    "TextFrame",
    "Menubutton",
    "FrameLabel",
    "FrameAutoGrid",
    "ScrollableFrame",
]

W = "w"
S = "s"
E = "e"
N = "n"
NE = "ne"
EW = "ew"
NS = "ns"
END = "end"
NSEW = "nsew"

WORD = "word"
NORMAL = "normal"
CENTER = "center"
DISABLED = "disabled"