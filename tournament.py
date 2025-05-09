import numpy as np

from game import Game
from strategies import STRATEGY_NAME

final_rating = np.array([0.0, 0.0, 0.0, 0.0, 0.0])
N = 10000

for i in range(N):
    game = Game([1, 1, 1, 1, 1])
    scores = game.get_results()
    player_scores = [(score, i) for i, score in enumerate(scores)]
    player_scores.sort()
    for i, [score, j] in enumerate(player_scores):
        final_rating[j] += 5 - i

final_rating -= final_rating.mean()
final_rating /= N

print(final_rating)