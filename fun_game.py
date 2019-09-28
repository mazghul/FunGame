from models.Game import Game


def main():
    while True:
        print("Welcome to The Fun Game !!!\n")
        game = Game()
        game.rounds = 5
        print("1. Single player\n2. Double player\n3. Demo\n4. Exit")
        choice = input("Enter your option : ")
        if choice in ["1", "2", "3"]:
            game.initialize_options(int(choice))

        elif choice == "4":
            exit()
        else:
            print("Enter a valid option")


if __name__ == "__main__":
    main()
