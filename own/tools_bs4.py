from . import requests, BeautifulSoup

def obtener_titulo(url:str, def_response:str = "Sin título"):
    respuesta = requests.get(url)
    soup = BeautifulSoup(respuesta.text, 'html.parser')
    return soup.title.string.strip() if soup.title else def_response