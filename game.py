from board import Board
from strategy import Strategy

class Game:
    def __init__(self, tactical: bool = False, proffecional: bool = False, player_number: int = 5):
        self.tactical = tactical
        self.proffecional = proffecional
        self.player_number = player_number
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
        self.board = Board()

    def startRound(self):
        self.board.setUpDeck()
        self.choosePlayers()
        self.board.playersChoice({i: player.chooseRow for i, player in enumerate(self.players)})

    def choosePlayers(self):
        self.players = [Strategy(hand, self.board.board, self.board.queue, self.board.discard, 
                                 self.tactical, self.proffecional, self.player_number) 
                        for hand in self.board.player_hands]

    def playerMove(self):
        moves = [(player.play(), i) 
                 for i, player in enumerate(self.players)]
        self.board.organizeQueue(moves)
        
    
        