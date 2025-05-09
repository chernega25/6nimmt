import tkinter as tk

from board import Board
from cardUI import CardUI
from strategies import PlayerStrategy

class rowButton(tk.Button):
    def __init__(self, master = None, points: int = 0, command=None, **kwargs):
        super().__init__(master, text="<< "+str(points), font=("Helvetica", 10),
                         width=8, height=1, 
                         bd=2, relief="raised", command=command, **kwargs)

class BoardUI(tk.Frame):
    def __init__(self, master, board:Board, **kwargs):
        super().__init__(master, bd=2, relief="raised", **kwargs)
        self.board = board.board
        self.player = None

        self.configure(bg="white")
        self._create_widgets()

    def _create_widgets(self):
        for col in range(6):
            self.grid_columnconfigure(col, weight=1)

        for row in range(4):
            self.grid_rowconfigure(row, weight=1)

        self.widgets = [[], [], [], []]
        for i in range(4):
            for j in range(5):
                self.widgets[i].append(tk.Frame(self, width=50, height=60, bd=2, relief="raised"))
                self.widgets[i][j].grid(row=i, column=j, padx=2, pady=2)
            for j, card in enumerate(self.board[i]):
                self.widgets[i][j] = CardUI(self, card)
                self.widgets[i][j].grid(row=i, column=j, padx=2, pady=2)

        self.buttons = [rowButton(self, sum(self.board[i]), self.getCommand(i)) for i in range(4)]
        for i, button in enumerate(self.buttons):
            button.grid(row=i, column=6, padx=2, pady=2)

    def setPlayer(self, player: PlayerStrategy):
        self.player = player

    def getCommand(self, x):
        def command():
            if self.player:
                self.player.row_choice.set(x) 
        return command
