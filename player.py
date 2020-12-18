from scoresheet import ScoreSheet
from hands import YahtzeeHand


class Player:

    def __init__(self, name):
        self.name = name
        

    x = 13
    points = []
    lower = []

    diction = {'ones': ScoreSheet().score_ones, 'twos': ScoreSheet().score_twos,
               'threes': ScoreSheet().score_threes, 'fours': ScoreSheet().score_fours,
               'fives': ScoreSheet().score_fives, 'sixes': ScoreSheet().score_sixes,
               'three of a kind': ScoreSheet().score_three_kind, 'four of a kind': ScoreSheet().score_four_kind,
               'yahtzee': ScoreSheet().score_yahtzee, 'full house': ScoreSheet().score_full_house,
               'small straight': ScoreSheet().score_small_straight,
               'large straight': ScoreSheet().score_large_straight, 'chance!': ScoreSheet().score_chance
               }
    dictionary = diction.copy()

    def turn(self):
        pass

    def game(self):

        while self.x > 0:
            hand = YahtzeeHand()
            hand.reroll()

            score = input(
                "score this hand, if you want to see which scoring methods you have not used type 'score' instead.\n").lower()

            if score == 'score':
                self.score_remaining()
                print(hand)
                score = input(
                    "\nscore this hand, by typing one of the scores above\n").lower()

            if score == 'stop':
                break

            if len(score) <= 6:
                self.lower.append(self.dictionary[score](hand))

            if score in self.dictionary:
                self.points.append(self.dictionary[score](hand))
                if score != 'yahtzee':
                    del self.dictionary[score]



            else:
                for key, value in self.dictionary.items():
                    print(key)
                print("are the remaining scoring methods you may use, please properly score it next time")

            self.x -= 1
            print(self.points)
        if sum(self.lower) >= 63:
            self.points.append(35)
            print("you get a bonus of 35 points for scoring high enough in ones through sixes!")
        print(f'{self.name} has a total of {sum(self.points)}, the game has ended!')

    def score_remaining(self):
        for key, value in Player.dictionary.items():
            print(key)


player = Player("player1")
player.game()
