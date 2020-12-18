from dice import D6



class Hand(list):
    def __init__(self, size=0, die_class=None):
        if not die_class:
            raise ValueError("You must provide a type of die")
        super().__init__()

        for _ in range(size):
            self.append(die_class())
        self.sort()

    def _by_value(self, value):
        dice = []
        for die in self:
            if die == value:
                dice.append(die)
        return dice

    def _reroll_dice(self):
        from player import Player
        print(f"\n{self}\nAre the dice you have rolled, you may still reroll them, type 'score' to see your remaining "
              f"scores \n")

        roll = input(
            "Which dice would you like to reroll? \n(please type the numbers of the dice you would like to reroll. "
            "They must be in numerical form.)\n").split()
        roll = "".join(roll)

        if roll.lower() == 'score':
            print(Player.score_remaining(Player))
            self._reroll_dice()

        if roll.split not in self:
            print(
                "please enter a number of numbers in numerical form to reroll the corresponding dice, if you see this "
                "message you have entered too many numbers or they are not in numerical form")

        roll.split()
        for x in roll:
            i = self.index(int(x))
            self[i] = D6()




        return self.sort()


class YahtzeeHand(Hand):
    def __init__(self, *args, **kwargs):
        super().__init__(size=5, die_class=D6, *args, **kwargs)

    def reroll(self):
        for _ in range(2):
            self._reroll_dice()
        print(f'{self}\nIs your final result')

    @property
    def ones(self):
        return self._by_value(1)

    @property
    def twos(self):
        return self._by_value(2)

    @property
    def threes(self):
        return self._by_value(3)

    @property
    def fours(self):
        return self._by_value(4)

    @property
    def fives(self):
        return self._by_value(5)

    @property
    def sixes(self):
        return self._by_value(6)

    @property
    def _sets(self):
        return {
            1: len(self.ones),
            2: len(self.twos),
            3: len(self.threes),
            4: len(self.fours),
            5: len(self.fives),
            6: len(self.sixes)
        }
