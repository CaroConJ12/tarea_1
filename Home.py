import tkinter as tk
from constants import colors


class Home(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background = colors.BACKGROUND)
        self.controller = controller
        self.segurityMode = tk.StringVar(self, value="IniciarMaquina")
        #   Última función a llamar
        self.init_widgets()
        
    def move_to_segurity(self):
        self.controller.mode = self.segurityMode.get()
        self.controller.show_frame(self.controller.segurity)

    def init_widgets(self):
        tk.Label(
            self,
            text = "¿Que haremos hoy?",
            justify = tk.CENTER,
            **colors.STYLE
        ).pack(
            side = tk.TOP,
            fill = tk.BOTH,
            expand = True,
            padx = 22,
            pady = 11
        )
        optionsFrame = tk.Frame(self)
        optionsFrame.configure(background = colors.COMPONENT)
        optionsFrame.pack(
            side = tk.TOP,
            fill = tk.BOTH,
            expand = True,
            padx = 22,
            pady = 11
        )
        tk.Label(
            optionsFrame,
            text = "Elige una opcion",
            justify = tk.CENTER,
            **colors.STYLE
        ).pack(
            side = tk.TOP,
            fill = tk.X,
            padx = 22,
            pady = 11
        )
        for (key, value) in colors.MODES.items():
            tk.Radiobutton(
                optionsFrame, 
                text = key + ("⚙️" if key == "INICIAR CORTINA" else ""), 
                variable = self.segurityMode,
                value = value,
                activebackground = colors.BACKGROUND,
                activeforeground = colors.TEXT,
                **colors.STYLE).pack(
                    side = tk.LEFT,
                    fill = tk.BOTH,
                    expand = True,
                    padx = 5,
                    pady = 5
                )
        tk.Button(
            self, 
            text = "EMPEZAR!",
            command = self.move_to_segurity,
            **colors.STYLE,
            relief = tk.FLAT,
            activebackground = colors.BACKGROUND,
            activeforeground = colors.TEXT,
            ).pack(
            side = tk.TOP,
            fill = tk.X,
            padx = 22,
            pady = 11
        )