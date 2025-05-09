import tkinter as tk

from config import PLAYER_COLORS

class ScoreUI(tk.Frame):
    def __init__(self, master, scores: list[int], **kwargs):
        super().__init__(master, bd=2, relief="raised", **kwargs)
        self.scores = scores
        self.n = len(scores)
        self.configure(bg="white")
        self._create_widgets()

    def _create_widgets(self):
        for col in range(self.n):
            self.grid_columnconfigure(col, weight=1)

        self.grid_rowconfigure(0, weight=1)

        self.widgets = []
        for j in range(self.n):
            self.widgets.append(tk.Label(self, 
                                         text=str(self.scores[j]), font=("Helvetica", 16, "bold"),
                                         bg=PLAYER_COLORS[j],
                                         width=2, height=1, bd=2, relief="raised"))
            self.widgets[j].grid(row=0, column=j, padx=2, pady=2)