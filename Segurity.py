import tkinter as tk
from constants import colors
from screens.Home import Home


class Segurity(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background = colors.BACKGROUND)
        self.controller = controller
        #   Última función a llamar
        self.currentQuestion = tk.StringVar(self, value = "Iniciando")
        self.fichero = None
        self.init_widgets()
        
    def updateQuestion(self):
        self.mode = self.controller.mode
        if  (self.fichero == None) or (self.controller.mode.lower() not in self.fichero.name.lower()):
            self.fichero = open(f'./questions/{self.mode}.txt','r', encoding='utf-8')
        tmp = self.fichero.readline()
        if  tmp != "":
            self.currentQuestion.set(tmp)
        else:
            self.currentQuestion.set("recorrimos las opciones, ¿reanudar el funcionamiento?")
            self.fichero.close()
            self.fichero = open(f'./questions/{self.mode}.txt','r', encoding='utf-8')

    def init_widgets(self):

        tk.Label(
            self,
            text = "Ejecutando:",
            justify = tk.CENTER,
            **colors.STYLE
        ).pack(
            side = tk.TOP,
            fill = tk.BOTH,
            expand = True,
            padx = 22,
            pady = 11
        )

        tk.Label(
            self,
            text = "initializing...",
            textvar = self.currentQuestion,
            justify = tk.CENTER,
            **colors.STYLE
        ).pack(
            side = tk.TOP,
            fill = tk.BOTH,
            expand = True,
            padx = 22,
            pady = 11
        )

        tk.Button(
            self, 
            text = "Presiona para iniciar/detener/reiniciar",
            command = self.updateQuestion,
            **colors.STYLE,
            relief = tk.FLAT,
            activebackground = colors.BACKGROUND,
            activeforeground = colors.TEXT,
            ).pack(
            side = tk.TOP,
            fill = tk.BOTH,
            expand = True,
            padx = 22,
            pady = 11
        )

        tk.Button(
            self, 
            text = "<- HOME",
            command = lambda: self.controller.show_frame(self.controller.home),
            **colors.STYLE,
            relief = tk.FLAT,
            activebackground = colors.BACKGROUND,
            activeforeground = colors.TEXT,
            ).pack(
            side = tk.TOP,
            fill = tk.BOTH,
            expand = True,
            padx = 22,
            pady = 11
        )
