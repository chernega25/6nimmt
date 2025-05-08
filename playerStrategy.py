import tkinter as tk

from strategy import Strategy

class PlayerStrategy(Strategy):
    def __init__(self, root, hand, board, queue, discard, tactical = False, proffecional = False, player_number = 5):
        self.root = root
        self.card_play = tk.IntVar(value=-1)
        self.row_choice = tk.IntVar(value=-1)
        super().__init__(hand, board, queue, discard, tactical, proffecional, player_number)

    def play(self):
        self.card_play.set(-1)
        self.root.wait_variable(self.card_play)
        return self.card_play.get()
    
    def chooseRow(self):
        self.row_choice.set(-1)
        self.root.wait_variable(self.row_choice)
        return self.row_choice.get()