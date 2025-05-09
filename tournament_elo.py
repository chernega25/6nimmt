from collections import defaultdict
import math

from game import Game
from strategies import STRATEGY_NAME

def compute_elo(strategy_ids, n_rounds, K=32, init_rating=1500):
    """
    strategy_ids  — список идентификаторов стратегий (может содержать дубликаты);
    n_rounds     — сколько раз прогонять Game;
    K            — константа Эло;
    init_rating  — стартовый рейтинг для каждой позиции.
    
    Возвращает словарь {strategy_id: avg_elo}.
    """
    n = len(strategy_ids)
    # рейтинг для каждой «позиции» (т. е. элемента списка)    
    ratings = [init_rating] * n

    for _ in range(n_rounds):
        game = Game(strategy_ids)
        points = game.get_results()  # список из n чисел
        
        # для каждой пары позиций i ≠ j
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                si, sj = points[i], points[j]
                # 1/0.5/0
                if   si >  sj: score = 1.0
                elif si == sj: score = 0.5
                else:          score = 0.0
                # ожидаемая
                exp_ij = 1 / (1 + 10 ** ((ratings[j] - ratings[i]) / 400))
                # обновляем
                ratings[i] += K * (score - exp_ij)

    return ratings


if __name__ == "__main__":
    strategies = [1, 1, 1, 1, 1]
    elo = compute_elo(strategies, n_rounds=1000, K=24)
    print(elo)
