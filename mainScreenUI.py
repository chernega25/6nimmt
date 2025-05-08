import tkinter as tk

from scoreUI import ScoreUI

class MainScreenUI(tk.Frame):
    def __init__(self, master, command, scores = [], **kwargs):
        super().__init__(master, **kwargs)

        if scores:
            self.scores = ScoreUI(self, scores)
            self.scores.pack()

        self.button = tk.Button(self, text="New Game", font=("Helvetica", 20), 
                                width=8, height=1, bd=2, relief="raised", 
                                command=command, **kwargs)
        self.button.pack()