from models.Players import Player
from models.KindBot import KindBot
from models.EvilBot import EvilBot
from models.CopyBot import CopyBot
from models.GrudgerBot import GrudgerBot
from models.Tour import Tour


class Game:
    def __init__(self, rounds=None):
        self.rounds = rounds
        self.p_1 = None
        self.p_2 = None
        self.option = None

    def single_player(self):  # player1 should always be player Player 2 can be evilbot/ kindbot/ copybot TODO check
        self.p_1 = Player()
        self.p_2 = GrudgerBot()  # TODO Get KindBOT / Evil bot / CopyBot from user
        self.initialize_players()

    def dual_player(self):
        self.p_1 = Player()
        self.p_2 = Player()
        self.initialize_players()

    def demo_game(self):
        self.p_1 = CopyBot()
        self.p_2 = EvilBot()

    def initialize(self, option):
        self.option = option
        if option == 1:
            self.single_player()
        elif option == 2:
            self.dual_player()
        else:
            self.demo_game()
        print("\n" + "-" * 20 + "Start Game" + "-" * 20 + "\n")
        self.start_game()
        self.print_results(self.p_1.score, self.p_2.score)

    @staticmethod
    def compare(x, y):
        if x == y:
            if x == 0:
                return [2, 2]
            else:
                return [0, 0]
        elif x < y:
            return [-1, 3]
        else:
            return [3, -1]

    def calculate(self):
        result = self.compare(self.p_1.get_choice(), self.p_2.get_choice())
        self.p_1.score += result[0]
        self.p_2.score += result[1]

    def start_game(self):
        for i in range(self.rounds):
            self.start_round()
            self.print_round_result()
            self.round_completed()

    def start_round(self):
        if self.option == 3:
            self.calculate()
        else:
            self.p_1.get_user_input()
            if self.option == 2:
                self.p_2.get_user_input()
            self.calculate()

    def print_round_result(self):
        print(
            "input\t {0} : {1}\t {2} : {3}".format(self.p_1.name, self.p_1.get_choice(), self.p_2.name,
                                                   self.p_2.get_choice()))
        print("score\t {0} : {1}\t {2} : {3}".format(self.p_1.name, self.p_1.score, self.p_2.name, self.p_2.score))
        print("-" * 50)

    def round_completed(self):
        self.p_1.round_completed(self.p_2.get_choice())
        self.p_2.round_completed(self.p_1.get_choice())

    def initialize_players(self):
        print("Player 1")
        self.p_1.get_user_name()

        if self.option == 2:
            print("Player 2")
            self.p_2.get_user_name()

    def print_results(self, p_1s, p_2s):
        print(
            "final score\t {0} : {1}\t {2} : {3}".format(self.p_1.name, self.p_1.score, self.p_2.name, self.p_2.score))
        print("-" * 50)
