import tkinter as tk

from gameUI import GameUI
from mainScreenUI import MainScreenUI

# Создаем главное окно
root = tk.Tk()
root.title("6 nimmt")
root.geometry("800x400")

mainScreen = None
game = None

def newGame():
    mainScreen.destroy()
    global game
    game = GameUI(root, endGame)
    game.pack()

def endGame(scores):
    game.destroy()
    global mainScreen
    mainScreen = MainScreenUI(root, newGame, scores)
    mainScreen.pack()

mainScreen = MainScreenUI(root, newGame)
mainScreen.pack()

# Запускаем главный цикл приложения
root.mainloop()