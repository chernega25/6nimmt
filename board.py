import random

from strategies import Card

class Board:
    def __init__(self, player_number: int = 5, tactical: bool = False):
        self.tactical = tactical
        self.player_number = player_number
        self.player_hands = []
        self.board = [[], [], [], []]
        self.queue = []
        self.discard = []

    def setUpDeck(self):
        card_number = self.player_number * 10 + 4 if self.tactical else 104
        cards = Card.createDeck(card_number)
        random.shuffle(cards)
        
        self.player_hands = [cards[i*10:(i+1)*10] for i in range(self.player_number)]
        for hand in self.player_hands:
            hand.sort()

        self.board = [[cards[-1]], [cards[-2]], [cards[-3]], [cards[-4]]]
        self.queue = []
        self.discard = []

    def playersChoice(self, choice):
        self.choice = choice

    def organizeQueue(self, moves: list[tuple[int, int]]):
        self.queue = []
        for j, i in moves:
            self.queue.append((self.player_hands[i][j], i))
            del self.player_hands[i][j]
        
        self.queue.sort()

    def qEmpty(self) -> bool:
        return not self.queue

    def cardProccessing(self) -> tuple[int, int]:
        m = -1
        points = 0
        card, i = self.queue[0]
        for j, row in enumerate(self.board):
            if row[-1] < card:
                if m == -1 or row[-1] > self.board[m][-1]:
                    m = j
        
        if m == -1:
            j = self.choice[i]()
            points = sum(self.board[j])
            self.discard.extend(self.board[j])
            self.board[j] = [card]
        elif len(self.board[m]) == 5:
            points = sum(self.board[m])
            self.discard.extend(self.board[m])
            self.board[m] = [card]
        else:
            self.board[m].append(card)

        del self.queue[0]
        return (i, points)