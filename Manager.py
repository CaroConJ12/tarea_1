import tkinter as tk
from constants import colors
from screens.Segurity import Segurity
from screens.Home import Home


class Manager(tk.Tk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Cortinas de Seguridad")
        self.mode = "Iniciar Máquina"
        self.segurity = Segurity
        self.home = Home

        container = tk.Frame(self)
        container.pack(
            side = tk.TOP, 
            fill = tk.BOTH, 
            expand = True
            )
        container.configure(background = colors.BACKGROUND)
        #   Índice de la fila/columna y lo que ocupa respecto
        #   a las demás. Una columna con weight 2 es el doble 
        #   de ancha que una con weight 1. 
        container.grid_columnconfigure(0, weight = 1)
        container.grid_rowconfigure(0, weight = 1)

        self.frames = {}
        for F in (Segurity, Home):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky = tk.NSEW)
        self.show_frame(Home)

    def show_frame(self, container):
        frame = self.frames[container]
        #   Manda el frame al frente de todo
        frame.tkraise()

        
        