from dice import D6


class Hand(list):
    def __init__(self, size=0, die_class=None, *args, **kwargs):
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
        
        print(f"\n{self}\nAre the dice you have rolled, you may still reroll them, type 'score' to see your remaining "
              f"scores \n")

        roll = input(
            "Which dice would you like to reroll? \n(please type a number of numbers between 1 and 6 corresponding to "
            "the dice themselves, each number rerolls the dice it corresponds to. If you are happy with this hand hit "
            "enter to skip your reroll )\n").split()

        roll = "".join(roll)

        if roll.lower() == 'score':
            from player import Player
            print Player.score_remaining(Player)
            return self
            

        for _ in roll:
            if _ not in str(self):
                print("oops, that's an invalid reroll. Please try to reroll the dice again, remember you can only use "
                      "the integers of 1-6 in numerical form and each one corresponds to one die you are trying to "
                      "reroll.")
                return self._reroll_dice()

        for i in roll:
            x = self.index(int(i))
            self[x] = D6()

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
