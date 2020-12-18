
class ScoreSheet:

    def _score_pairs(self, hand, set_size):
        # could split up the pair scores but it's fine. Maybe if I change the yahtzee scoring.
        if set_size == 3 or set_size == 4:
            for worth, count, in hand._sets.items():
                if count == set_size:
                    return sum(hand)
        if set_size == 5:
            for worth, count, in hand._sets.items():
                if count == set_size:
                    return sum(hand) + 50
        else:
            return 0

    def _score_house(self, hand):
        # it's fine, count is useful here.
        house = []
        for worth, count, in hand._sets.items():
            if count != 0:
                house.append(count)
        if max(house) == 3 and min(house) == 2:
            return sum(hand) + 25
        else:
            return 0

    def _score_l_straight(self, hand):
        # could also just say if hand == [1, 2, 3, 4, 5] lol
        large_straight = []
        for worth, count, in hand._sets.items():
            if count == 1:
                large_straight.append(worth)
                if large_straight == [1, 2, 3, 4, 5] or large_straight == [2, 3, 4, 5, 6]:
                    return 40
            else:
                return 0

    def _score_s_straight(self, hand):
        # could modify hand directly but probably better to use a separate list
        small_straight = []
        for worth, count in hand._sets.items():
            if count >= 1:
                small_straight.append(worth)
        for _ in range(1, 7):
            x = small_straight.count(_)
            if x >= 2:
                small_straight.remove(x)
        small_straight.sort()
        if small_straight == [1, 2, 3, 4] or small_straight == [2, 3, 4, 5] or small_straight == [3, 4, 5, 6]:
            return 30
        else:
            return 0




    def _score_chance(self, hand):
        return sum(hand)

    def score_ones(self, hand):
        return sum(hand.ones)

    def score_twos(self, hand):
        return sum(hand.twos)

    def score_threes(self, hand):
        return sum(hand.threes)

    def score_fours(self, hand):
        return sum(hand.fours)

    def score_fives(self, hand):
        return sum(hand.fives)

    def score_sixes(self, hand):
        return sum(hand.sixes)

    def score_three_kind(self, hand):
        return self._score_pairs(hand, 3)

    def score_four_kind(self, hand):
        return self._score_pairs(hand, 4)

    def score_yahtzee(self, hand):
        return self._score_pairs(hand, 5)

    def score_full_house(self, hand):
        return self._score_house(hand)

    def score_large_straight(self, hand):
        return self._score_l_straight(hand)

    def score_small_straight(self, hand):
        return self._score_s_straight(hand)

    def score_chance(self, hand):
        return self._score_chance(hand)
