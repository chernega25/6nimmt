import tkinter as tk

from game import Game

# Создаем главное окно
root = tk.Tk()
root.title("6 nimmt")
root.geometry("600x600")

root.grid_rowconfigure(0, weight=1)  # Первая строка будет растягиваться
root.grid_columnconfigure(0, weight=1)  # Первый столбец будет растягиваться

game = Game()
step = game.steps()

label1 = tk.Label(root, text="hands\n")
label1.grid(row=0, column=0, sticky="nsew")

label2 = tk.Label(root, text="board\n")
label2.grid(row=1, column=0, sticky="nsew")

label3 = tk.Label(root, text="points\n")
label3.grid(row=0, column=1, sticky="nsew")

label4 = tk.Label(root, text="queue\n")
label4.grid(row=1, column=1, sticky="nsew")

label5 = tk.Label(root, text="discard\n")
label5.grid(row=2, column=0, sticky="nsew")

def reloadText():
    label1.config(text="hands\n"+"\n".join(str(i) for i in game.board.player_hands))
    label2.config(text="board\n"+"\n".join(str(i) for i in game.board.board))
    label3.config(text="points\n"+str(game.player_points))
    label4.config(text="queue\n"+str(game.board.queue))
    label5.config(text="discard\n"+str(game.board.discard))

reloadText()
    
# Функция для нажатии кнопки
def next_step():
    # if not next(step):
    #     game.startGame()
    #     step = game.steps()
    #     next(step)
    next(step)
    reloadText()

# Создаем кнопку
button = tk.Button(root, text="Next Step", command=next_step)
button.grid(row=2, column=1, sticky="nsew")

# Запускаем главный цикл приложения
root.mainloop()