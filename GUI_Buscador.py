import own_tk
from own_tk.own_frameautogrid import EntryButton

from bs4 import BeautifulSoup

class GUIBuscador(own_tk.Tk):

    def __init__(self,  **kwargs):
        self.__html_soup:BeautifulSoup = None

        super().__init__(**kwargs)
        own_tk.Tools.configurar_pesos(self, [1], [1])

        self.entry_busqueda = EntryButton(self)
        own_tk.Tools.configurar_pesos(self.entry_busqueda, [1,1], [8,1])
        self.entry_busqueda.entrada.config(justify=own_tk.CENTER)
        self.entry_busqueda.boton.texto = "Buscar etiqueta"
        self.entry_busqueda.boton.exe_boton = self.__buscar_y_resaltar
        self.entry_busqueda.grid(row=0, column=0, sticky=own_tk.NSEW)

        self.text_area = own_tk.TextFrame(self, wrap=own_tk.WORD, font=("Consolas", 10))
        self.text_area.configure(state=own_tk.DISABLED)
        self.text_area.grid(row=1, column=0, sticky=own_tk.NSEW, columnspan=2, padx=5, pady=5)

        self.boton_cargar = own_tk.Button(self)
        self.boton_cargar.texto = "Cargar HTML"
        self.boton_cargar.exe_boton = self.__cargar_pagina
        self.boton_cargar.grid(row=0, column=1, sticky=own_tk.NSEW)

    @property
    def html_soup(self):
        return self.__html_soup
    
    def __cargar_pagina(self, *_):
        html_path = own_tk.filedialog.askopenfilename(title="Selecciona un archivo HTML", filetypes=[("Archivos HTML", "*.html")])

        if html_path:
            with open(html_path, 'r', encoding='utf-8') as f:
                self.__html_soup = BeautifulSoup(f, 'html.parser')
                self.text_area.configure(state=own_tk.NORMAL)
                self.text_area.insert(own_tk.END, self.__html_soup)
                self.text_area.configure(state=own_tk.DISABLED)
        else: pass

    def __buscar_y_resaltar(self, *_):
        self.text_area.tag_remove('highlight', '1.0', own_tk.END)
        tag_name = self.entry_busqueda.entrada.texto
        encontrados = self.__html_soup.find_all(tag_name)
        if not encontrados: return

        for e in [str(e) for e in encontrados]:
            contenido = str(e)
            pos = self.text_area.search(contenido, '1.0', own_tk.END)
            if pos:
                end = f"{pos}+{len(contenido)}c"
                self.text_area.tag_add('highlight', pos, end)

            self.text_area.tag_config('highlight', background='yellow')
    
programa = GUIBuscador()
programa.title("Buscador V1.0 - Beta")
own_tk.Tools.configurar_pesos(programa, [1], [1])

programa.mainloop()