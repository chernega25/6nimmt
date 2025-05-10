from .strategy import Strategy
from .card import Card
import math

class SpumoteStrategy1(Strategy):
    def __init__(self, hand, board, queue, discard, tactical = False, proffecional = False, player_number = 5):
        super().__init__(hand, board, queue, discard, tactical, proffecional, player_number)

    def chooseRow(self):
        return super().chooseRow()

    def cnt_other_players_card_in_hand(self, l=None, r=None):
        """
        Считает количество чисел из диапазона (l, r] (r по умолчанию = self.N),
        которые не встречаются ни в self.hand, ни в self.board, ни в self.discard.
        """
        # Задаём правый конец отрезка
        if l is None:
            l = 0
        if r is None:
            r = 104 if not self.tactical else self.player_number * 10 + 4

        # Общее количество чисел в отрезке
        total = max(0, r - l)

        # Собираем все "запрещённые" числа в одно множество
        used = set(self.hand_int) | {card for pile in self.board_int for card in pile} | set(self.discard_int)

        # Считаем, сколько из этих запрещённых попадают в [l, r]
        excluded_in_range = sum(1 for x in used if l < x <= r)

        # Разность — это те числа, которые остались
        return total - excluded_in_range
 
    
    def get_probability(self, cnt_all, k, m, n):
        if cnt_all < k:
            return 0
        if n < m:
            return 0
        res = math.comb(k - 1, m - 1) * math.comb(cnt_all - k, n - m) / math.comb(cnt_all, n - 1)
        return res
   
    def play(self):
        self.hand_int = [x.number for x in self.hand]
        self.board_int = [[x.number for x in str] for str in self.board]
        self.discard_int = [x.number for x in self.discard]

        intervals = [(0, 5, min([sum(self.board[x]) for x in range(4)]))]
        for i in range(4):
            intervals.append((self.board[i][-1].number, len(self.board[i]), sum(self.board[i]) + 5 - len(self.board[i])))
        intervals.sort()
        # print(intervals)
        e = []
        for i, x in enumerate(self.hand_int):
            for j in range(4, -1, -1):
                if x > intervals[j][0]:
                    break
            cnt_all = self.cnt_other_players_card_in_hand()
            k = self.cnt_other_players_card_in_hand(intervals[j][0], x)
            prob = self.get_probability(cnt_all, k + 1, 6 - intervals[j][1], self.player_number)

            # print(f'{x} {j} {intervals[j]} {cnt_all} before_us={k}, {prob:.3f} {prob * intervals[j][2]:.3f}')

            e.append(prob * intervals[j][2])


        res = e.index(min(e))
        return res
