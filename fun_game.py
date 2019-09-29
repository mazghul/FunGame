from models.Game import Game
from models.Players import Player
from models.KindBot import KindBot
from models.EvilBot import EvilBot
from models.CopyBot import CopyBot
from models.GrudgerBot import GrudgerBot
from models.Tour import Tour

def main():
    while True:
        print("Welcome to The Fun Game !!!\n")
        game = Game()
        game.rounds = 5
        print("1. Single player (Player vs Bot)\n2. Double player (Player vs Player)\n"
              "3. Demo (KindBot vs Evil Bot)\n4. Exit\n5. Bots Tournament")
        choice = input("Enter your option : ")
        if choice in ["1", "2", "3"]:
            game.initialize(int(choice))

        elif choice == "4":
            exit()
        if choice == "5":
            t1 = KindBot()
            t2 = EvilBot()
            t3 = CopyBot()
            t4 = GrudgerBot()
            tour = Tour(t1, t2, t3, t4)
            game.option = 3  # TODO add scores
            tour.start_tour(game)
        else:
            print("Enter a valid option")


if __name__ == "__main__":
    main()
