import tkinter as tk
from tkinter import ttk

from scoreUI import ScoreUI
from strategies import STRATEGY_NAME

class MainScreenUI(tk.Frame):
    def __init__(self, master, command, scores = [], **kwargs):
        super().__init__(master, **kwargs)

        if scores:
            self.scores = ScoreUI(self, scores)
            self.scores.pack(pady=10)

        self.command = command
        self.combo_frame = None
        self.player_combo = ttk.Combobox(self, values=[5, 6], state="readonly")
        self.player_combo.current(0)  # по умолчанию выбран первый
        self.player_combo.bind("<<ComboboxSelected>>", self.onPlayerNumberChange())
        self.player_combo.pack(pady=10)

        self.button = tk.Button(self, text="New Game", font=("Helvetica", 20), 
                                width=8, height=1, bd=2, relief="raised", 
                                command=self.startGame(), **kwargs)
        self.button.pack(pady=10)

        self.reloadStrategyBox()

    def onPlayerNumberChange(self):
        def func(event):
            self.reloadStrategyBox()
        return func
    
    def reloadStrategyBox(self):
        n = int(self.player_combo.get())

        if self.combo_frame: 
            self.combo_frame.destroy()

        self.combo_frame = tk.Frame(self)
        self.strategy_combo = []
        for i in range(n):
            self.strategy_combo.append(ttk.Combobox(self.combo_frame, values=STRATEGY_NAME[bool(i):], state="readonly"))
            self.strategy_combo[i].current(not i)
            # self.strategy_combo[i].grid(row=0, column=i, padx=10)
            self.strategy_combo[i].pack(pady=1)

        self.combo_frame.pack(pady=10)

    def startGame(self):
        def func():
            strategies = [combo.current()+1 for combo in self.strategy_combo]
            strategies[0] -= 1
            self.command(strategies)
        return func
            