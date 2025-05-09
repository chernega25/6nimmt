import tkinter as tk

from board import Board
from cardUI import CardUI
from config import PLAYER_COLORS

class QueueUI(tk.Frame):
    def __init__(self, master, board:Board, **kwargs):
        super().__init__(master, bd=2, relief="raised", **kwargs)
        self.queue = board.queue
        self.n = board.player_number
        self.configure(bg="white")
        self._create_widgets()

    def _create_widgets(self):
        for col in range(self.n):
            self.grid_columnconfigure(col, weight=1)

        self.grid_rowconfigure(0, weight=1)

        self.widgets = []
        for j in range(self.n):
            self.widgets.append(tk.Frame(self, width=50, height=60, bd=2, relief="raised"))
            self.widgets[j].grid(row=0, column=j, padx=2, pady=2)
        for j, [card, i] in enumerate(self.queue):
            self.widgets[j] = CardUI(self, card, color=PLAYER_COLORS[i])
            self.widgets[j].grid(row=0, column=j, padx=2, pady=2)