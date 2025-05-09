class Card:
    def __init__(self, number):
        self.number = number
        self.points = 1
        if number % 5 == 0:
            self.points = 2
        if number % 10 == 0:
            self.points = 3
        if number % 11 == 0:
            self.points = 5
        if number == 55:
            self.points = 7

    @staticmethod
    def createDeck(card_number: int) -> list["Card"]:
        return [Card(i) for i in range(1, card_number + 1)]
    
    def __lt__(self, other: "Card") -> bool:
        return self.number < other.number
    
    def __gt__(self, other: "Card") -> bool:
        return self.number > other.number
    
    def __eq__(self, other: "Card") -> bool:
        return self.number == other.number
    
    def __ne__(self, other: "Card") -> bool:
        return self.number != other.number
    
    def __add__(self, other: "Card | int") -> int:
        if isinstance(other, Card):
            return self.points + other.points
        elif isinstance(other, int):
            return self.points + other
        return NotImplemented

    def __radd__(self, other: int) -> int:
        return self.points + other
    
    def __str__(self) -> str:
        return str(self.number)
    
    def __repr__(self) -> str:
        return str(self)
        