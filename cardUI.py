import tkinter as tk

from strategies import Card

class CardUI(tk.Frame):
    def __init__(self, master, card: Card, color: str = "white", command=None, **kwargs):
        super().__init__(master, width=50, height=60, bd=2, relief="raised", **kwargs)
        self.card = card
        self.color = color
        self.command = command

        self.configure(bg=color)
        self._create_widgets()
        self._layout_widgets()
        if self.command:
            self._bind_clicks()

    def _create_widgets(self):
        self.number_label = tk.Label(self, text=str(self.card.number), font=("Helvetica", 16, "bold"), bg=self.color)
        self.bonus_label = tk.Label(self, text=str(self.card.points), font=("Helvetica", 8), bg=self.color, fg="gray")

    def _layout_widgets(self):
        self.number_label.place(relx=0.5, rely=0.4, anchor="center")
        self.bonus_label.place(relx=0.5, rely=0.8, anchor="center")

    def _bind_clicks(self):
        self.bind("<Button-1>", self._on_click)
        self.number_label.bind("<Button-1>", self._on_click)
        self.bonus_label.bind("<Button-1>", self._on_click)

    def _on_click(self, event):
        if self.command:
            self.command()