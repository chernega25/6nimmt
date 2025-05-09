import tkinter as tk

from .strategy import Strategy

class PlayerStrategy(Strategy):
    def __init__(self, hand, board, queue, discard, tactical = False, proffecional = False, player_number = 5):
        super().__init__(hand, board, queue, discard, tactical, proffecional, player_number)
        
        self.card_play = tk.IntVar(value=-1)
        self.row_choice = tk.IntVar(value=-1)

    def setRoot(self, root):
        self.root = root
        self.label = tk.Label(root, text="Your Move")

    def play(self):
        self.card_play.set(-1)
        self.label.place(relx=1.0, rely=0.0, anchor="ne")
        self.root.wait_variable(self.card_play)
        self.label.place_forget()
        return self.card_play.get()
    
    def chooseRow(self):
        self.row_choice.set(-1)
        self.label.place(relx=1.0, rely=0.0, anchor="ne")
        self.root.wait_variable(self.row_choice)
        self.label.place_forget()
        return self.row_choice.get()