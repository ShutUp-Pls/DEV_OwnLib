### CONSTRUCTOR DEL MODULO ###

### IMPORTACIONES DE LIBRERIAS USADAS POR EL MODULO
# Estan marcados con un comentario los modulos que estan siendo llamados
# Y dentro e los comentarios posibles importaciones futuras

import os, json, time, shutil               #
import queue
import decimal
import traceback
import threading

import tkinter as tk                        #

from itertools import zip_longest           #
from PIL import ImageFont, ImageDraw        #, Image, ImageTk
from tkinter import ttk, font               #, Text, filedialog, messagebox
from collections.abc import MutableMapping  #

from types import GeneratorType
from typing import Any, Literal

### IMPORTACIÓN DE CLASES PROPIAS
# Corresponde a clases del modulo ya listas para usar por el usuario

from .own_utils import TkTools, StrTools, ListTools, DictTools, OsTools, PillowTools, FormatTools, JsonTools, Crono

BASE_DIR = os.path.dirname(__file__)