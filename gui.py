import tkinter as tk

from game import Game


class Gui:
    def __init__(self, game: Game) -> None:
        self.root = tk.Tk()


    def run(self):
        self.root.mainloop()


        