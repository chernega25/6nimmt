import random

from card import Card

class Strategy:
    def __init__(self, 
                 hand: list[Card], board: list[list[Card]], 
                 queue: list[tuple[Card, int]], discard: list[Card],
                 tactical: bool = False, proffecional: bool = False, player_number: int = 5):
        self.hand = hand #ссылка, не менять
        self.board = board #ссылка, не менять
        self.queue = queue #ссылка, не менять
        self.discard = discard #ссылка, не менять
        self.tactical = tactical
        self.proffecional = proffecional
        self.player_number = player_number

    def play(self) -> int:
        k = random.randint(0, len(self.hand) - 1)
        return k
    # играет случайную карту из руки
    
    def chooseRow(self) -> int:
        m = [0, 0, 0, 0]
        for i in range(4):
            m[i] = sum(self.board[i])
        return m.index(min(m))
    # забирает наименьшее число очков