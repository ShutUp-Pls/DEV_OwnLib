from . import time

class Crono:
    def __init__(self, verbose:bool=True):
        self.__verbose = True
        self.verbose = verbose

        self.__checkpoints = []
        self.checkpoints = time.time()

        if self.verbose:
            print(f"[Checkpoint 0 -> {self.checkpoints[0]}] (Total Registrados: {len(self.checkpoints)})")
            print(f"Total_time: {0:.6f}, Checkpoint_0.0_time: {0:.6f}")

    @property
    def checkpoints(self):
        return self.__checkpoints
    
    @checkpoints.setter
    def checkpoints(self, value:float|int):
        if not isinstance(value, (float,int)): raise ValueError(f"Valor ingresado '{value}' no es un número. Se esperaba un número (int o float) para 'checkpoints'.")
        self.__checkpoints.append(value)

    @property
    def verbose(self):
        return self.__verbose

    @verbose.setter
    def verbose(self, value: bool):
        if not isinstance(value, bool): raise ValueError("'verbose' debe ser un valor booleano True|False")
        self.__verbose = value

    def checkpoint(self, from_checkpoint:int=None, verbose:bool=None):
        if self.checkpoints: num_checkpoints = len(self.checkpoints)
        else: raise AttributeError("El atributo 'checkpoints' no ha sido definido")

        if from_checkpoint is None: from_checkpoint = num_checkpoints-1
        elif not isinstance(from_checkpoint, int): raise ValueError("'from_checkpoint' debe ser un valor Entero")

        if verbose is None: verbose = self.verbose
        elif not isinstance(verbose, bool): raise ValueError("'verbose' debe ser un valor booleano True|False")

        current_time = time.time()

        total_time = current_time - self.checkpoints[0]
        partial_time = current_time - self.checkpoints[from_checkpoint]
        self.checkpoints = current_time

        if verbose:
            print(f"[Checkpoint {num_checkpoints} -> {current_time}] (Total Registrados: {len(self.checkpoints)})")
            print(f"Total_time: {total_time:.6f}, Checkpoint_{from_checkpoint}.{num_checkpoints}_time: {partial_time:.6f}")

    def sleep(self, seconds):
        time.sleep(seconds)
