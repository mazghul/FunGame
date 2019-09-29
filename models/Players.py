import random


class Player:
    def __init__(self, name=None):
        self.name = name
        self.score = 0
        self.choice = None
        self.choices = []

    def get_choice(self):
        return self.choice

    def get_user_input(self):
        while True:
            choice = input(self.name + " Enter your choice (0 for Co-operate, 1 for Cheat): ")
            # choice = str(random.randint(0, 1))
            if choice in ["0", "1"]:
                self.choice = int(choice)
                self.choices.append(self.choice)
                break
            else:
                print("\nEnter a valid input either 0 or 1")

    def get_user_name(self):
        result = input("Enter your name : ")
        self.name = result

    def round_completed(self, value):
        pass
