from board import Board
from strategies import STRATEGY_CLASS

class Game:
    def __init__(self, playerCallback, strategies, tactical: bool = False, proffecional: bool = False):
        self.tactical = tactical
        self.proffecional = proffecional
        self.strategies = strategies
        self.playerCallback = playerCallback
        self.player_number = len(strategies)
        self.startGame()

    def get_results(self):
        for _ in self.steps():
            pass
        return self.player_points

    def steps(self):
        yield
        while min(self.player_points) > 0:
            self.startRound()
            yield

            for _ in range(10):
                self.playerMove()
                yield

                while not self.board.qEmpty():
                    i, p = self.board.cardProccessing()
                    self.player_points[i] -= p
                    yield

        yield

    def startGame(self):
        self.player_points = [66] * self.player_number
        self.board = Board(self.player_number)

    def startRound(self):
        self.board.setUpDeck()
        self.choosePlayers()
        self.board.playersChoice({i: player.chooseRow for i, player in enumerate(self.players)})

    def choosePlayers(self):
        self.players = [STRATEGY_CLASS[self.strategies[i]]
                        (hand, self.board.board, self.board.queue, self.board.discard, 
                         self.tactical, self.proffecional, self.player_number) 
                         for i, hand in enumerate(self.board.player_hands)]
        
        if self.strategies[0] == 0:
            self.playerCallback()

    def playerMove(self):
        moves = [(player.play(), i) 
                 for i, player in enumerate(self.players)]
        self.board.organizeQueue(moves)
        
    
        