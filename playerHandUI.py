import tkinter as tk

from cardUI import CardUI
from strategies import Card
from strategies import PlayerStrategy

class PlayerHandUI(tk.Frame):
    def __init__(self, master, player:PlayerStrategy, hand:list[Card], **kwargs):
        super().__init__(master, bd=2, relief="raised", **kwargs)
        self.hand = hand
        self.player = player
        self._create_widgets()
        
    def _create_widgets(self):
        for col in range(10):
            self.grid_columnconfigure(col, weight=1)

        self.grid_rowconfigure(0, weight=1)

        self.widgets = []
        for j in range(10):
            self.widgets.append(tk.Frame(self, width=50, height=60, bd=2, relief="raised"))
            self.widgets[j].grid(row=0, column=j, padx=2, pady=2)
        for j, card in enumerate(self.hand):
            self.widgets[j] = CardUI(self, card, command=self.cardChoice(j))
            self.widgets[j].grid(row=0, column=j, padx=2, pady=2)

    def cardChoice(self, x):
        def func():
            self.player.card_play.set(x)
        return func