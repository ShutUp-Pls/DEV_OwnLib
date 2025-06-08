import own, requests

from own.own_entrybutton import EntryButton

class GUIScrapHTML(own.Tk):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        own.Tools.configurar_pesos(self, [1], [1])

        self.scraping = EntryButton(self)
        self.scraping.boton.texto = "Scrap HTML"
        self.scraping.boton.exe_boton = self.do_scrap
        self.scraping.grid(row=0, column=0, sticky=own.NSEW)

    def do_scrap(self):
        response = requests.get(self.scraping.entrada.texto)
        with open('pagina.html', 'w', encoding='utf-8') as f: f.write(response.text)

programa = GUIScrapHTML()
programa.title("Scrappable V1.0 - Beta")
own.Tools.configurar_pesos(programa, [1], [1])

programa.mainloop()