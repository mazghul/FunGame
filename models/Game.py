from models.Players import Player
from models.KindBot import KindBot
from models.EvilBot import EvilBot
from models.CopyBot import CopyBot

import random


class Game:
    def __init__(self, rounds=None):
        self.rounds = rounds
        self.p_1 = None
        self.p_2 = None

    def single_player(self):  # player1 will always be player .. Player 2 can be evilbot or kindbot or copybot
        self.p_1 = Player()
        self.p_2 = CopyBot()  # TODO: KindBOT / Evil bot

    def dual_player(self):
        self.p_1 = Player()
        self.p_2 = Player()

    def demo_game(self):
        self.p_1 = KindBot()
        self.p_2 = EvilBot()

    def initialize_options(self, option):
        if option != 3:
            if option == 1:
                self.single_player()
            else:
                self.dual_player()
            self.initialize_players(option)
        else:
            self.demo_game()
        print("\n" + "-" * 20 + "Start Game" + "-" * 20 + "\n")
        self.start_game(option)
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

    def calculate(self, p_1, p_2):
        result = self.compare(p_1.get_choice(), p_2.get_choice())
        p_1.score += result[0]
        p_2.score += result[1]

    @staticmethod
    def get_user_input(player):
        while True:
            choice =  input(player.name + " Enter your choice (0 for Co-operate, 1 for Cheat): ") # str(random.randint(0, 1))  #
            if choice in ["0", "1"]:
                player.choice = int(choice)
                player.choices.append(player.choice)
                break
            else:
                print("\nEnter a valid input either 0 or 1")

    def start_game(self, option):
        for i in range(self.rounds):
            if option == 3:
                self.calculate(self.p_1, self.p_2)
            else:
                self.get_user_input(self.p_1)
                if option == 2:
                    self.get_user_input(self.p_2)
                self.calculate(self.p_1, self.p_2)
            print(
                "input\t {0} : {1}\t {2} : {3}".format(self.p_1.name, self.p_1.get_choice(), self.p_2.name, self.p_2.get_choice()))
            print("score\t {0} : {1}\t {2} : {3}".format(self.p_1.name, self.p_1.score, self.p_2.name, self.p_2.score))
            print("-" * 50)
            if option == 1 and self.p_2.name == "Copy Cat Bot":
                self.p_2.previous_value = self.p_1.get_choice()

    @staticmethod
    def get_user_name(p):
        result = input("Enter your name : ")
        return result

    def initialize_players(self, options=1):
        print("Player 1")
        self.p_1.name = self.get_user_name(self.p_1)

        if options == 2:
            print("Player 2")
            self.p_2.name = self.get_user_name(self.p_2)

    def print_results(self, p_1s, p_2s):
        print(
            "final score\t {0} : {1}\t {2} : {3}".format(self.p_1.name, self.p_1.score, self.p_2.name, self.p_2.score))
        print("-" * 50)