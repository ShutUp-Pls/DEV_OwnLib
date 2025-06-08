from . import os, shutil

class OsTools:

    @staticmethod
    def is_path(path):
        return os.path.exists(path)

    @staticmethod
    def is_dir(path):
        return os.path.isdir(path)

    @staticmethod
    def clean_dir(path):
        if not os.path.exists(path): raise FileNotFoundError(f"La ruta '{path}' no existe.")
        if not os.path.isdir(path): raise NotADirectoryError(f"La ruta '{path}' no es un directorio.")

        try:
            shutil.rmtree(path)
            os.makedirs(path)
        except:
            list_dir = os.listdir(path)
            for file in list_dir:
                file_path = os.path.join(path, file)
                if os.path.isfile(file_path) or os.path.islink(file_path): os.unlink(file_path)
                elif os.path.isdir(file_path): shutil.rmtree(file_path)
        
    @staticmethod
    def len_files(path):
        if not os.path.exists(path): raise FileNotFoundError(f"La ruta '{path}' no existe.")
        if not os.path.isdir(path): raise NotADirectoryError(f"La ruta '{path}' no es un directorio.")

        list_dir = os.listdir(path)
        files = [f for f in list_dir if os.path.isfile(os.path.join(path, f))]
        return len(files)

    @staticmethod
    def put_directory(path):
        if not os.path.exists(path): os.makedirs(path)
        elif not os.path.isdir(path): raise NotADirectoryError(f"La ruta '{path}' existe pero no es un directorio.")