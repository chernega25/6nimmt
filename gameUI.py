import tkinter as tk

from game import Game
from boardUI import BoardUI
from queueUI import QueueUI
from scoreUI import ScoreUI
from playerHandUI import PlayerHandUI

class GameUI(tk.Frame):
    def __init__(self, master, strategies, command, **kwargs):
        super().__init__(master,
                         width=800, height=400,
                         bd=2, relief="raised", **kwargs)
        
        self.game = Game(self.playerStrategySync(), strategies)
        self.step = self.game.steps()
        self.command = command
        self.root = master
        self.player = None
        self.hand = None

        self.configure(bg="white")
        self._create_widgets()
        self.nextButton = tk.Button(self, text="Next", font=("Helvetica", 20), 
                                    width=4, height=1, bd=2, relief="raised", 
                                    command=self.nextCommand(), **kwargs)
        self.nextButton.place(x=720, y=360, anchor="se")

    def _create_widgets(self):
        self.board = BoardUI(self, self.game.board)
        self.board.place(x=10, y=390, anchor="sw")

        self.queue = QueueUI(self, self.game.board)
        self.queue.place(x=720, y=280, anchor="se")

        self.score = ScoreUI(self, self.game.player_points)
        self.score.place(x=720, y=200, anchor="se")

        if self.player:
            self.createPlayerHand()
            self.board.setPlayer(self.player)

    def updateGame(self):
        self.board.destroy()
        self.queue.destroy()
        self.score.destroy()
        if self.hand: self.hand.destroy()
        self._create_widgets()

    def nextCommand(self):
        def nextStep():
            try:
                next(self.step)
                self.updateGame()
            except StopIteration:
                self.command(self.game.player_points)
        return nextStep

    def playerStrategySync(self):
        def func():
            self.player = self.game.players[0]
            self.player.setRoot(self.root)
            self.board.setPlayer(self.player)
            self.createPlayerHand()
        return func
    
    def createPlayerHand(self):
        self.hand = PlayerHandUI(self, self.player, self.game.board.player_hands[0])
        self.hand.place(x=10, y=10, anchor="nw")

