from .strategy import Strategy
from .playerStrategy import PlayerStrategy
from .chernegaStrategy1 import ChernegaStrategy1
from .spumoteStrategy1 import SpumoteStrategy1
from .card import Card

STRATEGY_NAME = [
    "Player",
    "Random Strategy",
    "Chernega Strategy 1",
    "Spumote Strategy 1"

]

STRATEGY_CLASS = [
    PlayerStrategy,
    Strategy,
    ChernegaStrategy1,
    SpumoteStrategy1
    
]