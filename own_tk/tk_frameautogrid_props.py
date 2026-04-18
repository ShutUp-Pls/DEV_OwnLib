import tkinter as tk

class FrameAutoGridProps:
    def __init__(self, master=None, **kwargs):
        self._widgets: dict[tuple[int,int], tk.Widget] = {}
        super().__init__(master, **kwargs)

    @property
    def widgets(self) -> dict[tuple[int,int], tk.Widget]:
        return self._widgets