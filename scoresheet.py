class ScoreSheet:

    def _score_pairs(self, hand, set_size):
        if set_size == 3 or set_size == 4:
            for worth, count, in hand._sets.items():
                if count == set_size:
                    return sum(hand)
        elif set_size == 5:
            for worth, count, in hand._sets.items():
                if count == set_size:
                    return sum(hand) + 50

    def _score_house(self, hand):
        for worth, count, in hand._sets.items():
            if count == 3:
                for value, repeat, in hand._sets.items():
                    if repeat == 2:
                        return sum(hand) + 25

       def _score_l_straight(self, hand):
        large_straight = []
        for worth, count, in hand._sets.items():
            if count == 1:
                large_straight.append(worth)
                if large_straight == [1, 2, 3, 4, 5] or large_straight == [2, 3, 4, 5, 6]:
                    return 40

    def _score_s_straight(self, hand):
        if hand._sets[4] == 1 and hand._sets[5] == 1 and hand.sixes != [] and hand.threes != []:
            return 30
        if hand._sets[3] == 1 and hand._sets[4] == 1 and hand.twos != [] and hand.fives != []:
            return 30
        elif hand._sets[2] == 1 and hand._sets[3] == 1 and hand.ones != [] and hand.fours != []:
            return 30

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
