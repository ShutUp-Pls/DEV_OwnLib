from . import json

class JsonTools:

    @staticmethod
    def load_json(path):
        with open(path, 'r', encoding='utf-8') as archivo: datos = json.load(archivo)
        return datos if datos else None

    @staticmethod
    def save_as_json(diccionario, ruta):  
        with open(ruta, 'w', encoding='utf-8') as archivo:
            json.dump(diccionario, archivo, indent=4, ensure_ascii=False)

    @staticmethod
    def update_json(path, new_data_dict):
        data = JsonTools.load_json(path) or {}
        data.update(new_data_dict)
        JsonTools.save_as_json(data, path)