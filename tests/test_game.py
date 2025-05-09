from game import Game
import random

def test_results():
    random.seed(42)
    game = Game([1, 1, 1, 1, 1])
    player_points = game.get_results()
    assert player_points == [0, 33, 43, 38, 7]

def test_spumote():
    random.seed(42)
    game = Game([1, 1, 1, 1, 3])
    player_points = game.get_results()
    assert player_points == [0, 33, 43, 38, 7]
