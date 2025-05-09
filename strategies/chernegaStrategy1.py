from .strategy import Strategy
from .card import Card

class ChernegaStrategy1(Strategy):
    def __init__(self, hand, board, queue, discard, tactical = False, proffecional = False, player_number = 5):
        super().__init__(hand, board, queue, discard, tactical, proffecional, player_number)

    def chooseRow(self):
        return super().chooseRow()
    
    def play(self):
        return self.calculateBest()

    def chooseRowPrep(self, board):
        m = [0, 0, 0, 0]
        for i in range(4):
            m[i] = sum(board[i])
        return m.index(min(m))

    def queueScore(self, queue: list[tuple[Card, bool]]):
        board = [row.copy() for row in self.board]
        queue.sort()

        points = 0
        for card, p in queue:
            m = -1
            for j, row in enumerate(board):
                if row[-1] < card:
                    if m == -1 or row[-1] > board[m][-1]:
                        m = j
            
            if m == -1:
                j = self.chooseRowPrep(board)
                if p: points = sum(board[j])
                board[j] = [card]
            elif len(board[m]) == 5:
                if p: points = sum(board[m])
                board[m] = [card]
            else:
                board[m].append(card)

        return points
    
    def makeDeck(self):
        deck = Card.createDeck(self.player_number * 10 + 4 if self.tactical else 104)
        for card in self.hand:
            deck.remove(card)
        for card in self.discard:
            deck.remove(card)
        for row in self.board:
            for card in row:
                deck.remove(card)
        
        return deck
    
    def calculateBest(self):
        deck = self.makeDeck()
        n = len(deck)
        m = []
        for card in self.hand:
            p = 0
            for i in range(n):
                for j in range(i+1, n):
                    for k in range(j+1, n):
                        for l in range(k+1, n):
                            queue = [(card, True), 
                                     (deck[i], False), 
                                     (deck[j], False), 
                                     (deck[k], False), 
                                     (deck[l], False)]
                            p += self.queueScore(queue)
            m.append(p)
        return m.index(min(m))
